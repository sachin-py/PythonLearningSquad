"""
Black and White Image Converter 🖤🤍

This script converts a color image to black and white (grayscale)
using the Python Imaging Library (PIL / Pillow).

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

"""

from PIL import Image

photo_path = 'Photo.jpg'  # Define the path to the input image
image = Image.open(photo_path)  # Open the image file

# Convert the image to grayscale (mode 'L' stands for luminance)
bw_image = image.convert('L')


bw_image.save('bw_image.jpg')  # Save the converted black and white image

print('Black and White Image generated')
image.close()  # Close the original image file
