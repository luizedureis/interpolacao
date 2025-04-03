import numpy as np
class ImageModel:
    def __init__(self, image: np.ndarray, zoom_factor: int = 0):
        self.image = image
        self.zoom_factor = zoom_factor
