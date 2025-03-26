import numpy as np

from internal.use_case.load_img import Load_Image
from internal.use_case.rotacionar import Rotacao_Imagem
from internal.use_case.zoom import Zoom
from PIL import Image


image_path = 'img.png'
li = Load_Image()
img = li.run(image_path)
img_rgb = np.array(img)

rotacao = Rotacao_Imagem(img_rgb, 2)
imagem_rotacionada_rgb = rotacao.rotacionar()

imagem_rotacionada = Image.fromarray(imagem_rotacionada_rgb)
imagem_rotacionada.show()

