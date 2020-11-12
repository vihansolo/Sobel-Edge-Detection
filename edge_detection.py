"""Python Edge Detection Using Sobel Operator

@2020 Created by Vihang Garud
"""

# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import math


def sobel_detection(original_image):
    """
    Creating a Sobel Edge Detection algorithm

    :param original_image: Get the original image
    :return: parser: image with detected sobel edges
    """

    # Creating a parser (piece of the image) for the operation
    parser = np.copy(original_image)
    size = parser.shape

    # Implementing Gx and Gy
    for x in range(1, size[0] - 1):

        for y in range(1, size[1] - 1):

            # -1	 0	   1
            # -2	 0	   2
            # -1	 0	   1

            Gx = (original_image[x - 1][y + 1] + 2 * original_image[x][y + 1] + original_image[x + 1][y + 1]) - (
                        original_image[x - 1][y - 1] + 2 * original_image[x][y - 1] + original_image[x + 1][y - 1])

            #   1	  2	    1
            #   0	  0	    0
            #  -1	 -2	   -1

            Gy = (original_image[x - 1][y - 1] + 2 * original_image[x - 1][y] + original_image[x - 1][y + 1]) - (
                        original_image[x + 1][y - 1] + 2 * original_image[x + 1][y] + original_image[x + 1][y + 1])

            # Generating combined image
            parser[x][y] = math.sqrt(Gx ** 2 + Gy ** 2)

    # Returning the operated image
    return parser


if __name__ == '__main__':

    # Reading the image
    image = plt.imread('test-pattern.tif')

    # Applying Sobel Operator
    edge_detected_image = sobel_detection(image)

    # Output the image with detected edges
    plt.imshow(edge_detected_image, cmap='gray')
    plt.show()
