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

    # Interpolação bilinear para cada componente de cor (R, G, B)
    r1 = (x2 - x) * A[0] + (x - x1) * B[0]
    g1 = (x2 - x) * A[1] + (x - x1) * B[1]
    b1 = (x2 - x) * A[2] + (x - x1) * B[2]

    r2 = (x2 - x) * C[0] + (x - x1) * D[0]
    g2 = (x2 - x) * C[1] + (x - x1) * D[1]
    b2 = (x2 - x) * C[2] + (x - x1) * D[2]

    r = (y2 - y) * r1 + (y - y1) * r2
    g = (y2 - y) * g1 + (y - y1) * g2
    b = (y2 - y) * b1 + (y - y1) * b2

    # Retorna a cor como uma tupla (R, G, B)
    return (int(r), int(g), int(b))


# Função para redimensionar a imagem
def redimensionar(imagem, fator_zoom,largura, altura):

    nova_largura = int(largura * fator_zoom)
    nova_altura = int(altura * fator_zoom)

    largura, altura = imagem.size
    imagem_redimensionada = Image.new("RGB", (nova_largura, nova_altura))

    for i in range(nova_largura):
        for j in range(nova_altura):
            # Calculando as coordenadas correspondentes na imagem original
            x = i * (largura / nova_largura)
            y = j * (altura / nova_altura)
            cor = interpolacao_bilinear(x, y, imagem)
            imagem_redimensionada.putpixel((i, j), cor)

    return imagem_redimensionada