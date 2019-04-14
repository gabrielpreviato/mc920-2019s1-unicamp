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

from config import get_config

from SaveConfig import SaveConfig


def main(args, config):
    # SaveConfig does the configurations for saving the ouputs of the problems
    save_config = SaveConfig(config.path, config.clean_at_init, config.is_save)
    save_config.execute()

    # First let's load all images and put them in an numpy array of images
    filenames = glob.glob("../images/*.png")

    # images is an array of shape (number_of_images, width, height)
    images = np.array([imageio.imread(img) for img in filenames])

    # Problem 1.1
    # Bright adjustment
    # Arguments: gama (np.array). Default is [0.25, 0.5, 2.0, 4.0]
    gama = np.array(config.gama)

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

    # Calling save_images
    save_config.save_images(work_images, gama, filenames, "1.1")

    # End of Problem 1.1

    # Problem 1.2
    # Bits planes
    # Arguments: bits (np.array). Default is [0, 1, 2, 3, 4, 5, 6, 7]
    bits = np.array(config.bits)

    # Create blocks of gama's size of images, in other words, an array of shape (gama's size, number_of_images, width,
    # height)
    work_images = np.repeat(images[np.newaxis, :, :, :], bits.size, axis=0)

    # First step, create a mask to segment the image's bits planes
    bits_mask = np.left_shift(1, bits)

    # Final step, do bitwise_and between the images and the mask
    binary_images = np.bitwise_and(work_images, bits_mask[:, None, None, None])
    binary_images = np.where(binary_images > 0, 255, binary_images)

    # Calling save_images
    save_config.save_images(binary_images, bits, filenames, "1.2")

    # End of problem 1.2

    # Problem 1.3
    # Mosaic
    # Arguments: mosaic_order (np.array)
    mosaic_order = np.array([[6, 11, 13, 3], [8, 16, 1, 9], [12, 14, 2, 7], [4, 15, 10, 5]])

    work_images = images[0]
    work_images.reshape(16, 128, 128)

    pass


if __name__ == "__main__":
    config, unparsed = get_config()

    main([sys.argv[0]] + unparsed, config)
