import numpy as np
import math
from PIL import Image

def convert_to_grayscale(image: Image.Image) -> Image.Image:
    # Parameter:
    # image: This parameter is expected to be a color image object (from the Pillow library).
    #        It represents the image that you want to convert to grayscale.

    """Convert a color image to grayscale using Pillow."""
    return image.convert('L')  # Convert to grayscale mode 'L'

def adjust_brightness(pixel_array: np.ndarray, brightness_factor: float) -> np.ndarray:
    # Parameters:
    # pixel_array: This is a 2D NumPy array that contains pixel values of the image.
    #              Each value represents the intensity of a pixel in the range of 0 to 255.
    # brightness_factor: This is a scalar value (float) that determines how much to
    #                    adjust the brightness. A value greater than 1 increases
    #                    brightness, while a value less than 1 decreases it.
    # Note: You ARE NOT ALLOWED to use any loops for this task!

    """TODO: Adjust the brightness of a 2D NumPy array of pixel values."""
    # Your code here
    pixel_array = pixel_array.astype(np.float64)
    pixel_array = pixel_array * brightness_factor
    pixel_array = np.clip(pixel_array, 0, 255)
    pixel_array = pixel_array.astype(np.uint8)
    return pixel_array


def otsu_thresholding(pixel_array: np.ndarray) -> tuple[np.ndarray, float]:
    # Parameter:
    # pixel_array: This is a 2D NumPy array of pixel values representing
    #              a grayscale image. The function uses this array to compute
    #              an optimal threshold for converting the image into a binary format.

    """TODO: Perform Otsu's thresholding on a 2D NumPy array of pixel values."""
    # Your code here
    optimize = pixel_array.copy()
    x: float = np.mean(optimize)
    while True:
        x1: float = np.mean(optimize[optimize > x])
        x2: float = np.mean(optimize[optimize <= x])
        x_new: float = (x1+x2) / 2
        if math.isclose(x, x_new):
            break
        x = x_new
    optimize[optimize > x] = 255
    optimize[optimize <= x] = 0
    return optimize, x

def median_filter(pixel_array: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    # Parameters:
    # pixel_array: This is a 2D NumPy array of pixel values representing the image
    #              to which the median filter will be applied.
    # kernel_size: This is an optional parameter (default value is 3) that specifies
    #              the size of the square kernel used for the median filtering.
    #              The kernel size determines the area around each pixel that will be
    #              considered when calculating the median value. It should be an odd
    #              integer (e.g., 3, 5, 7) to ensure a center pixel.
    # Note: You can assume the kernel_size is always an odd number.
    
    """TODO: Apply median filtering to a NumPy array of pixel values using a specified kernel size."""
    edge: int = (kernel_size-1)//2
    mod = np.zeros_like(pixel_array)
    pixel_array = np.pad(pixel_array, edge, mode = "edge")
    for i in range(len(pixel_array)):
        if i < edge or (len(pixel_array)-i) <= edge:
            continue
        for j in range(len(pixel_array[i])):
            if j < edge or (len(pixel_array[i])-j) <= edge:
                continue
            cal: np.ndarray = pixel_array[i-edge:i+edge+1, j-edge:j+edge+1]
            mod[i-edge,j-edge] = np.median(cal)
    return mod
            