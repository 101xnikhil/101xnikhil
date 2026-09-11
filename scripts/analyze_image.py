from PIL import Image, ImageChops
import cv2
import numpy as np

image = Image.open("source-prepped.png")
print(image.size)

new_width = 80
new_height = int(image.height * new_width / image.width)

print(new_width, new_height)

small_image = image.resize((new_width, new_height))
small_image.save("ascii-source.png")

alpha = image.getchannel("A")

print("Alpha range:", alpha.getextrema())

for threshold in [50, 100, 150, 200, 250]:
    test_alpha = alpha.point(lambda p: 255 if p > threshold else 0)
    bbox = test_alpha.getbbox()
    print("Threshold:", threshold, "Bounding box:", bbox)

cropped_image = image.crop((3, 37, 1077, 1541))
cropped_image.save("cropped-source.png")
mask = np.array(alpha)
_, mask = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
print("Contours found:", len(contours))
largest_contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest_contour)
print("Largest contour:", x, y, w, h)
gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2GRAY)
print("Brightness range:", gray.min(), gray.max())

for threshold in [20, 40, 60, 80, 100]:
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        largest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest)
        print(f"Brightness threshold {threshold}: {x}, {y}, {w}, {h}")


        threshold = 80

_, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

cv2.imwrite("mask-80.png", mask)

print("Saved mask-80.png")



# Convert cropped image to ASCII
chars = "@%#*+=-:. "

ascii_image = Image.open("cropped-source.png").convert("L")
ascii_image = ascii_image.resize((80, 40))

for y in range(ascii_image.height):
    line = ""

    for x in range(ascii_image.width):
        pixel = ascii_image.getpixel((x, y))
        index = pixel * (len(chars) - 1) // 255
        line += chars[index]

    print(line)

