#
#   Author: Gabriel Previato
#   Version: 0.1.0
#
#   Purpose: This project is made to solve some small challenges proposed in "Trabalho 0"
#   with the intention to get the students used to the frameworks and tools that will be used
#   in the course.
#   More informations: https://github.com/gabrielpreviato/mc920-2019s1-unicamp/blob/master/trabalho-0/trabalho0.pdf
#
import itertools
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
    # Arguments: gama
    # gama will be a numpy array
    gama = np.array([0.25, 0.5, 2.0, 4.0])

    work_images = np.repeat(images[np.newaxis, :, :, :], gama.size, axis=0)

    # First step, convert the images from a [0, 255] range of uint8 to a [0, 1] range of float64
    work_images = work_images / 255.0

    # Second step, apply the equation B = A^(1/gama)
    work_images = np.power(work_images, 1/gama[:])

    # Final step, convert the image back to a [0, 255] range of uint8
    work_images = work_images * 255.0
    work_images = np.asarray(work_images, dtype=np.uint8)

    # Path operations to create image directory if it doesn't exist
    work_path = file_path / "gen_images_1.1"
    if not work_path.is_dir():
        work_path.mkdir()

    # Save the images
    [imageio.imsave(work_path / img_name / "gama-" + str(gama), img) for img_name, img, gama in zip([filenames_last.split('/')[-1] for filenames_last in filenames]
                                                                                          , [img for img in work_images]
                                                                                          , itertools.repeat(gama, images.size))]

    pass


if __name__ == "__main__":
    main(sys.argv)
