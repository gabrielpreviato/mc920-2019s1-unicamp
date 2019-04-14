import glob
from pathlib import Path
import shutil
import imageio
import numpy as np


class SaveConfig:

    def __init__(self, path_root, clean_at_init=True, is_save=False):
        self.path_root = Path(path_root)
        self.clean_at_init = clean_at_init
        self.is_save = is_save

    def execute(self):
        if self.clean_at_init:
            self.clean_gen_images()

    def clean_gen_images(self):
        dirs = glob.glob("gen_images*/")

        for dir in dirs:
            shutil.rmtree(dir)

    def save_images(self, images, appends, filenames, problem):
        if self.is_save:
            # Path operations to create image directory if it doesn't exist
            work_path = self.path_root / ("gen_images_" + problem)
            if not work_path.is_dir():
                work_path.mkdir()

            # Save the images
            [imageio.imsave(work_path / (problem + "p-" + str(append) + "-" + img_name), img) for img_name, img, append in
             zip(
                np.tile(np.array([filenames_last.split('/')[-1] for filenames_last in filenames]), appends.size),
                images.reshape((images.shape[0] * images.shape[1], 512, 512)).astype(dtype=np.uint8),
                np.repeat(appends, images.shape[1])
                )
            ]
