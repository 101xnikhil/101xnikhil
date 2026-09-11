from rembg import remove, new_session
from PIL import Image

session = new_session("u2netp")

input_image = Image.open("source-photo.jpg")
output_image = remove(input_image, session=session)
output_image.save("source-prepped.png")