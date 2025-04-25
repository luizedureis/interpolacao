import numpy as np
import matplotlib.pyplot as plt

class Show_Image:
    def __init__(self):
        pass

    def run(self, rgb_array: np.ndarray):
        plt.imshow(rgb_array)  # Usando Matplotlib para exibir a imagem
        plt.axis('off')  # Para remover os eixos
        plt.show()
