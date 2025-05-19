"""
A simple script to convert a color image to black and white (grayscale)
using the Pillow library.

Requirements:
    pip install pillow

Usage:
    1. Place your image in the same directory and name it 'Photo.jpg'
    2. Run the script:
        python bw_converter.py
    3. The grayscale image will be saved as 'bw_image.jpg'

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

"""

from PIL import Image


def convert_to_black_and_white(input_path='Photo.jpg', output_path='bw_image.jpg'):
    """Convert an image to black and white and save it."""
    try:
        with Image.open(input_path) as image:  # Open the input image
            bw_image = image.convert('L')  # Convert the image to grayscale
            bw_image.save(output_path)  # Convert the image to grayscale
            print(f"Black and white image saved as '{output_path}'")
    except FileNotFoundError:
        print(f"File '{input_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    convert_to_black_and_white()
