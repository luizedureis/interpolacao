# Filtragem de Wiener:
#
# O filtro de Wiener é amplamente utilizado para restaurar imagens borradas. Ele trabalha estimando o espectro de potência da imagem original e da imagem borrada e tenta "desfazer" o efeito de borramento com base nesses espectros.
#
# Métodos de Desconvolução:
#
# O processo de desconvolução é utilizado para reverter o borramento. Ele tenta resolver uma equação onde a imagem borrada é o resultado de uma convolução da imagem original com um kernel de borramento. Algoritmos como Lucy-Richardson e blind deconvolution são comuns nesse tipo de abordagem.
#
# Redes Neurais (Deep Learning):
#
# Redes neurais convolucionais (CNNs) podem ser treinadas para restaurar imagens borradas. Algumas abordagens, como autoencoders e redes adversariais generativas (GANs), podem ser treinadas para aprender como restaurar imagens de maneira mais eficaz.


import numpy as np

from internal.use_case.rotacionar import Rotacao_Imagem
from PIL import Image



# img_rgb = np.array(img)
#
# rotacao = Rotacao_Imagem(img_rgb, 2)
# imagem_rotacionada_rgb = rotacao.rotacionar()
#
# imagem_rotacionada = Image.fromarray(imagem_rotacionada_rgb)
# imagem_rotacionada.show()
#
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float
from skimage.restoration import wiener
from internal.use_case.load_img import Load_Image
from internal.use_case.resize import Zoom

# Carregar a imagem
image_path = 'diego.png'
print("lendo mensagem")
li = Load_Image()
img_original = li.run(image_path)
print("aplicando zoom")
zo = Zoom(img_original,3)
image=  img_as_float(zo.redimensionar())

# Definir um kernel de borramento simples (por exemplo, uma média 5x5)
kernel = np.ones((5, 5)) / 25

# Inicializar a imagem restaurada com o mesmo formato da imagem original
image_restaurada = np.zeros_like(image)

# Aplicar o filtro de Wiener separadamente para cada canal (R, G, B)
for i in range(image.shape[2]):  # Para cada canal (RGB)
    image_restaurada[..., i] = wiener(image[..., i], kernel, balance=0.2)

# Normalizar a imagem restaurada para o intervalo [0, 1]
image_restaurada = np.clip(image_restaurada, 0, 1)

# Exibir a imagem restaurada
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(img_original)
ax[0].set_title("Imagem Original")
ax[0].axis('off')

ax[1].imshow(image)
ax[1].set_title("Imagem zoom 3x")
ax[1].axis('off')

ax[2].imshow(image_restaurada)
ax[2].set_title("Imagem Restaurada")
ax[2].axis('off')

plt.show()

