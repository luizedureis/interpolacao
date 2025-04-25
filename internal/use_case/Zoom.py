import numpy as np

from internal.use_case.resize import Resize


class Zoom:
    def __init__(self):
        pass

    # Função para dar zoom em uma área central da imagem
    def run(self, img_np_array, zoom_factor, offset_x=0, offset_y=0):
        # Dimensões da imagem
        width, height, _ = img_np_array.shape

        # Determinar a nova largura e altura com base no fator de zoom
        zoom_width = int(width / zoom_factor)
        zoom_height = int(height / zoom_factor)

        # Definir o centro da área de zoom com deslocamento
        center_x = width // 2 + offset_x
        center_y = height // 2 + offset_y

        # Garantir que o deslocamento não faça o recorte ultrapassar os limites da imagem
        left = max(center_x - zoom_width // 2, 0)
        top = max(center_y - zoom_height // 2, 0)
        right = min(center_x + zoom_width // 2, width)
        bottom = min(center_y + zoom_height // 2, height)

        # Cortar a imagem para obter a região do zoom
        cropped_img = img_np_array[top:bottom, left:right]

        # Redimensionar ao tamanho original
        resized_img = Resize(cropped_img, width, height).redimensionar()

        return np.array(resized_img)