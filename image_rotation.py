"""
A simple script to rotate an image by 90 degrees using the Pillow library.

Requirements:
    pip install pillow

Usage:
    1. Make sure Pillow is installed.
    2. Place your image in the same directory and name it 'PhotoToInvert.jpg'
    3. Run this script:
        python rotate_image.py
    4. The rotated image will be saved as 'InvertedPhoto.jpg'

Author: Sachin Kumar
GitHub: https://github.com/sachin-py
"""

from PIL import Image

input_path = 'PhotoToInvert.jpg'
output_path = 'InvertedPhoto.jpg'

image = Image.open(input_path)
rotate_image = image.rotate(90)
rotate_image.save(output_path)
print('Image Rotated')
image.close()
