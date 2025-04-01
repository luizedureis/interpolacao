import numpy as np
from skimage.restoration import wiener


#TODO implementar o filtro do wiener
class Deblur:
    def __init__(self):
        pass

    def run(self, img):
        img = np.array(img)
        img = img / 255.0

        # Se a imagem estiver em formato RGB, divide em canais
        if img.ndim == 3 and img.shape[2] == 3:
            image_restaurada = np.zeros_like(img)

            # Definir um kernel de borramento simples (exemplo: média 5x5)
            kernel = np.ones((5, 5)) / 25.0

            # Aplica o filtro de Wiener separadamente para cada canal RGB
            for i in range(img.shape[2]):  # Para cada canal (R, G, B)
                image_restaurada[..., i] = wiener(img[..., i], kernel, balance=0.1)
        else:
            # Se não for RGB, aplica o Wiener na imagem em tons de cinza
            kernel = np.ones((5, 5)) / 25.0
            image_restaurada = wiener(img, kernel, balance=0.1)

        # Garante que a imagem restaurada esteja no intervalo [0, 1]
        image_restaurada = np.clip(image_restaurada, 0, 1)

        # Converte para o formato uint8 (0-255) antes de retornar
        return (image_restaurada * 255).astype(np.uint8)
