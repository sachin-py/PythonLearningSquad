"""
A simple script to rotate an image by 90 degrees clockwise using the Pillow library.

Requirements:
    - Python 3.x
    - Pillow (PIL fork) library

Install Pillow using:
    pip install pillow

Usage:
    1. Place your image file in the same directory as this script.
    2. Rename the image to 'PhotoToInvert.jpg' or change the 'input_path' below accordingly.
    3. Run the script:
        python rotate_image.py
    4. The rotated image will be saved as 'InvertedPhoto.jpg' in the same directory.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py
"""

from PIL import Image


def rotate_image(input_path='PhotoToInvert.jpg', output_path='InvertedPhoto.jpg'):
    """
    Opens an image, rotates it 90 degrees clockwise, and saves it.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the rotated image.
    """
    try:
        with Image.open(input_path) as image:  # Open the original image
            # Rotate the image 90 degrees clockwise
            rotated = image.rotate(90, expand=True)
            rotated.save(output_path)  # Save the rotated image
            print(f"Image rotated and saved as '{output_path}'")
    except FileNotFoundError:
        print(f"Input file '{input_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    rotate_image()
