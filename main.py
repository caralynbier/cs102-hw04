import math
import sys
from PIL import Image

input_path = sys.argv[1]  # input img
output_path = sys.argv[2]  # output img

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

# TODO: Replace this with your own filter!
# Median pixel filter, taken from https://note.nkmk.me/en/python-opencv-pillow-image-size

for i in range(0, width - 1):
    for j in range(0, height - 1):
        r, g, b = img.getpixel((i, j))
        r1, g1, b1 = img.getpixel((i + 1, j + 1))
        edge = math.sqrt(
            ((r - r1) * (r - r1)) + ((g - g1) * (g - g1)) + ((b - b1) * (b - b1))
        )

        if edge >= 25:
            new_img.putpixel((i, j), (0, 0, 0))
        else:
            new_img.putpixel((i, j), (255, 255, 255))

new_img.save(output_path)