from typing import Any

from PIL import Image
import numpy as np
from numpy import ndarray, dtype


class Load_Image:
    def __init__(self):
        pass

    # def run(self,image_path:str)-> ndarray[Any, dtype[Any]]:
    #     img = Image.open(image_path)
    #     rgb_img = img.convert('RGB')
    #     width, height = rgb_img.size
    #     rgb_array = np.array(rgb_img).reshape((height, width, 3))
    #
    #     return rgb_array


    def run(self, image_path):
        # Verifique se o caminho da imagem é válido
        try:
            img = Image.open(image_path)
            return img  # Retorna a imagem como um objeto PIL.Image
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            return None