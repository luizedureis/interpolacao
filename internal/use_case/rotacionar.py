import numpy as np
import math
from PIL import Image


# Função para aplicar a rotação com interpolação bilinear
def rotacionar_imagem(rgb_lista, largura, altura, angulo):
    # Converter o ângulo de graus para radianos
    angulo_rad = math.radians(angulo)

    # Calcular o centro da imagem
    cx, cy = largura / 2, altura / 2

    # Criar a lista RGB para a imagem rotacionada
    rgb_rotacionada = np.zeros_like(rgb_lista)

    # Definir as coordenadas dos pixels na imagem original
    for y in range(altura):
        for x in range(largura):
            # Subtrair o centro para a rotação
            x_shifted = x - cx
            y_shifted = y - cy

            # Aplicar a rotação
            x_rot = int(x_shifted * math.cos(angulo_rad) - y_shifted * math.sin(angulo_rad) + cx)
            y_rot = int(x_shifted * math.sin(angulo_rad) + y_shifted * math.cos(angulo_rad) + cy)

            # Verificar se as coordenadas resultantes estão dentro dos limites da imagem
            if 0 <= x_rot < largura and 0 <= y_rot < altura:
                # Atribuindo o valor do pixel
                rgb_rotacionada[y, x] = rgb_lista[y_rot, x_rot]

    return rgb_rotacionada


# Classe para carregar e rotacionar a imagem
class Rotacao_Imagem:
    def __init__(self):
        pass

    def rotacionar(self,imagem_rgb, angulo):
        self.imagem_rgb = imagem_rgb
        self.angulo = angulo
        self.altura, self.largura, _ = imagem_rgb.shape

        return rotacionar_imagem(self.imagem_rgb, self.largura, self.altura, self.angulo)
