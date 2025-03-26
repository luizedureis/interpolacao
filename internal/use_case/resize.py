from PIL import Image


# Função para interpolação bilinear
def interpolacao_bilinear(x, y, imagem):
    largura, altura = imagem.size
    x1 = int(x)
    y1 = int(y)
    x2 = min(x1 + 1, largura - 1)
    y2 = min(y1 + 1, altura - 1)

    # Pegando os valores dos 4 pixels próximos
    A = imagem.getpixel((x1, y1))
    B = imagem.getpixel((x2, y1))
    C = imagem.getpixel((x1, y2))
    D = imagem.getpixel((x2, y2))

    def inter_bili(A, B, C, D, x, x1, x2, y, y1, y2):
        r1 = (x2 - x) * A + (x - x1) * B
        r2 = (x2 - x) * C + (x - x1) * D
        r = (y2 - y) * r1 + (y - y1) * r2
        return r

    return tuple(int(inter_bili(A[i], B[i], C[i], D[i], x, x1, x2, y, y1, y2)) for i in range(3))


class Zoom:
    def __init__(self, imagem, fator_zoom):
        largura, altura = imagem.size
        self.fator_zoom = fator_zoom
        self.largura = largura
        self.altura = altura
        self.nova_largura = int(largura * fator_zoom)
        self.nova_altura = int(altura * fator_zoom)

        # Inicializa a imagem redimensionada
        self.imagem_redimensionada = Image.new("RGB", (self.nova_largura, self.nova_altura))
        self.imagem = imagem

    def cal_coordenadas(self, i, j):
        # Calculando as coordenadas correspondentes na imagem original
        x = i * (self.largura / self.nova_largura)
        y = j * (self.altura / self.nova_altura)
        cor = interpolacao_bilinear(x, y, self.imagem)

        # Atribui a cor ao pixel correspondente
        self.imagem_redimensionada.putpixel((i, j), cor)

    def redimensionar(self):
        # Redimensiona a imagem calculando as coordenadas para cada pixel
        [self.cal_coordenadas(i, j) for i in range(self.nova_largura) for j in range(self.nova_altura)]
        return self.imagem_redimensionada