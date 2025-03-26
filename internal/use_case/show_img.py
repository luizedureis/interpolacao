from typing import Any

from PIL import Image
import numpy as np


class Show_Image:
    def __init__(self):
        pass
    def run(self, rgb_array: np.ndarray[Any, np.dtype[Any]]) -> None:
        image = Image.fromarray(rgb_array.astype('uint8'))
        image.show()