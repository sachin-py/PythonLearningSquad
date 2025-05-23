"""
Description:
    Resizes an input image to the specified width and height using the Pillow library.

Requirements:
    - Python 3.x
    - Pillow library

Install dependencies:
    pip install pillow

Usage:
    1. Place the image in the same directory as this script.
    2. Run the script and provide inputs
    3. The resized image will be saved to the specified output path.

Notes:
    - Supports only raster formats (e.g., PNG, JPG).
    - You can adjust the dimensions or add user input support if desired.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py
"""

from PIL import Image
import os


def resize_image(input_path: str, output_path: str, width: int, height: int) -> None:
    """Resize an image to the given width and height.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the resized image.
        width (int): Desired width.
        height (int): Desired height.
    """
    if not os.path.exists(input_path):
        print(f"Input file '{input_path}' not found.")
        return

    try:
        with Image.open(input_path) as image:
            resized = image.resize((width, height))
            resized.save(output_path)
            print(f"Image resized successfully and saved to '{output_path}'")
    except Exception as e:
        print(f"Failed to resize image: {e}")


if __name__ == "__main__":

    input_path = 'Photo.jpg'
    output_path = 'resizedPhoto.jpg'
    new_width = 200
    new_height = 200

    resize_image(input_path, output_path, new_width, new_height)
