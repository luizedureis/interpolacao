import numpy as np

# Função para interpolação bilinear
def interpolacao_bilinear(x, y, imagem):
    altura, largura, _ = imagem.shape
    x1 = int(x)
    y1 = int(y)
    x2 = min(x1 + 1, largura - 1)
    y2 = min(y1 + 1, altura - 1)

    # Pegando os valores dos 4 pixels próximos
    A = imagem[y1, x1]
    B = imagem[y1, x2]
    C = imagem[y2, x1]
    D = imagem[y2, x2]

    def inter_bili(A, B, C, D, x, x1, x2, y, y1, y2):
        r1 = (x2 - x) * A + (x - x1) * B
        r2 = (x2 - x) * C + (x - x1) * D
        r = (y2 - y) * r1 + (y - y1) * r2
        return r

    return tuple(int(inter_bili(A[i], B[i], C[i], D[i], x, x1, x2, y, y1, y2)) for i in range(3))


class Resize:
    def __init__(self, imagem, largura, altura):
        self.largura, self.altura = imagem.shape[1], imagem.shape[0]
        self.nova_largura = largura
        self.nova_altura = altura

        # Inicializa a imagem redimensionada (em formato de array NumPy)
        self.imagem_redimensionada = np.zeros((self.nova_altura, self.nova_largura, 3), dtype=np.uint8)
        self.imagem = imagem

    def cal_coordenadas(self, i, j):
        # Calculando as coordenadas correspondentes na imagem original
        x = i * (self.largura / self.nova_largura)
        y = j * (self.altura / self.nova_altura)
        cor = interpolacao_bilinear(x, y, self.imagem)

        # Atribui a cor ao pixel correspondente
        self.imagem_redimensionada[j, i] = cor

    def redimensionar(self):
        # Redimensiona a imagem calculando as coordenadas para cada pixel
        [self.cal_coordenadas(i, j) for i in range(self.nova_largura) for j in range(self.nova_altura)]
        return self.imagem_redimensionada
