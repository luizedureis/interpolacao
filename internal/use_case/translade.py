import numpy as np

class Translacao:
    def __init__(self):
        pass

    def translada_imagem(self, imagem, desloc_x, desloc_y):
        altura, largura, canais = imagem.shape

        # Criar uma nova imagem azul (fundo azul)
        imagem_translada = np.zeros_like(imagem)
        imagem_translada[:] = (83, 83, 236)

        # Para cada pixel na imagem original, calcular a nova posição
        for y in range(altura):
            for x in range(largura):
                # Calcular a nova posição
                novo_x = x + desloc_x
                novo_y = y + desloc_y

                # Verificar se a nova posição está dentro dos limites da imagem
                if 0 <= novo_x < largura and 0 <= novo_y < altura:
                    # Copiar o valor do pixel para a nova posição
                    imagem_translada[novo_y, novo_x] = imagem[y, x]

        return imagem_translada
