#
#   Author: Gabriel Previato
#   Version: 0.1.0
#
#   Purpose: This project is made to solve some small challenges proposed in "Trabalho 0"
#   with the intention to get the students used to the frameworks and tools that will be used
#   in the course.
#   More informations: https://github.com/gabrielpreviato/mc920-2019s1-unicamp/blob/master/trabalho-0/trabalho0.pdf
#
import sys
import glob
from pathlib import Path
import numpy as np
import imageio


def main(argv):
    # Path variable that will be used to save the generated images
    file_path = Path('.')

    # First let's load all images and put them in an numpy array of images
    filenames = glob.glob("../images/*.png")

    # images is an array of shape (number_of_images, width, height)
    images = np.array([imageio.imread(img) for img in filenames])

    # Problem 1.1
    # Bright adjustment
    # Arguments: gama (np.array)
    gama = np.array([0.25, 0.5, 2.0, 4.0])

    # Create blocks of gama's size of images, in other words, an array of shape (gama's size, number_of_images, width,
    # height)
    work_images = np.repeat(images[np.newaxis, :, :, :], gama.size, axis=0)

    # First step, convert the images from a [0, 255] range of uint8 to a [0, 1] range of float64
    work_images = work_images / 255.0

    # Second step, apply the equation B = A^(1/gama)
    work_images = work_images ** (1 / gama[:, None, None, None])

    # Final step, convert the image back to a [0, 255] range of uint8
    work_images = work_images * 255.0
    work_images = np.asarray(work_images, dtype=np.uint8)

    # Path operations to create image directory if it doesn't exist
    work_path = file_path / "gen_images_1.1"
    if not work_path.is_dir():
        work_path.mkdir()

    # Save the images
    [imageio.imsave(work_path / ("gama-" + str(gama) + "-" + img_name), img) for img_name, img, gama in zip(
        np.tile(np.array([filenames_last.split('/')[-1] for filenames_last in filenames]), gama.size),
        work_images.reshape((20, 512, 512)),
        np.repeat(gama, images.shape[0])
    )
     ]

    # End of Problem 1.1

    # Problem 1.2
    # Bits planes
    # Arguments: bits (np.array)
    bits = np.array([0, 1, 2, 3, 4, 5, 6, 7])

    # Create blocks of gama's size of images, in other words, an array of shape (gama's size, number_of_images, width,
    # height)
    work_images = np.repeat(images[np.newaxis, :, :, :], bits.size, axis=0)

    # First step, create a mask to segment the image's bits planes
    bits_mask = np.left_shift(1, bits)

    # Final step, do bitwise_and between the images and the mask
    binary_images = np.bitwise_and(work_images, bits_mask[:, None, None, None])
    binary_images = np.where(binary_images > 0, 255, binary_images)

    # Path operations to create image directory if it doesn't exist
    work_path = file_path / "gen_images_1.2"
    if not work_path.is_dir():
        work_path.mkdir()

    # Save the images
    [imageio.imsave(work_path / ("bit-" + str(bit) + "-" + img_name), img) for img_name, img, bit in zip(
        np.tile(np.array([filenames_last.split('/')[-1] for filenames_last in filenames]), bits.size),
        binary_images.reshape(
            (binary_images.shape[0] * binary_images.shape[1], binary_images.shape[2], binary_images.shape[3])).astype(
            np.uint8),
        np.repeat(bits, images.shape[0])
    )
     ]

    # End of problem 1.2

    # Problem 1.3
    # Mosaic
    # Arguments: mosaic_order (np.array)
    mosaic_order = np.array([[6, 11, 13, 3], [8, 16, 1, 9], [12, 14, 2, 7], [4, 15, 10, 5]])

    work_images = images[0]
    work_images.reshape(16, images.shape[2] / 4, images.shape[2] / 4)

    pass


if __name__ == "__main__":
    main(sys.argv)
