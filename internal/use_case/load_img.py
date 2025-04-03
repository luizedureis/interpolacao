import numpy as np
from PIL import Image

from internal.model.image import ImageModel


class Load_Image:
    def __init__(self):
        pass

    def run(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.convert('RGB')  # Garantir que a imagem esteja no formato RGB
            return ImageModel(np.array(img))  # Converter para um array NumPy
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            return None