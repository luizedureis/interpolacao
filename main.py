from argparse import ZERO_OR_MORE

import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float
from skimage.restoration import wiener
from internal.use_case.load_img import Load_Image
from internal.use_case.resize import Zoom
from PIL import Image
from internal.use_case.rotacionar import Rotacao_Imagem
from internal.use_case.show_img import Show_Image



# Carregar a imagem
image_path = 'diego.png'
print("lendo mensagem")
li = Load_Image()

rotacao = Rotacao_Imagem(li.run(image_path),20).rotacionar()

Show_Image().run(rotacao)