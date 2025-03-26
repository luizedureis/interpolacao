#
# from internal.use_case.load_img import Load_Image
# from internal.use_case.show_img import Show_Image
#
# image_path = 'img.png'
# li = Load_Image()
# img = li.run(image_path)
#
# altura, largura, _ = img.shape
# altura = round(altura*0.3)
# largura = round(largura*0.3)
# print(altura,largura)
# img[:,0] = 2
# for linha in img:
#     print(" ".join(map(str, linha)))
#
# si = Show_Image()
# si.run(img)

import numpy as np
from internal.use_case.zoom import Zoom

matriz = [
    [1,2,3,4,5,6,7,8,9,10],
    [2,2,3,4,5,6,7,8,9,10],
    [3,2,3,4,5,6,7,8,9,10],
    [4,2,3,11,11,11,11,8,9,10],
    [5,2,3,11,11,11,11,11,9,10],
    [6,2,3,11,11,11,11,11,9,10],
    [7,2,3,11,11,11,11,8,9,10],
    [8,2,3,4,5,6,7,8,9,10],
    [9,2,3,4,5,6,7,8,9,10],
    [10,2,3,4,5,6,7,8,9,10],
]
for linha in matriz:
    print(" ".join(map(str, linha)))
matriz_numpy = np.array(matriz)
zoom = Zoom(matriz_numpy)
print(zoom.zoom3())

matriz = [
    [1,2,3,4,5,6,7,8,9,10,11,12],
    [2,2,3,4,5,6,7,8,9,10,11,12],
    [3,2,3,4,5,6,7,8,9,10,11,12],
    [4,2,3,4,20,20,20,20,9,10,11,12],
    [5,2,3,4,20,20,20,20,9,10,11,12],
    [6,2,3,4,20,20,20,20,9,10,11,12],
    [7,2,3,4,20,20,20,20,9,10,11,12],
    [8,2,3,4,20,20,20,20,9,10,11,12],
    [9,2,3,4,5,6,7,8,9,10,11,12],
    [10,2,3,4,5,6,7,8,9,10,11,12],
    [11,2,3,4,5,6,7,8,9,10,11,12],
]
for linha in matriz:
    print(" ".join(map(str, linha)))

matriz_numpy = np.array(matriz)
zoom = Zoom(matriz_numpy)
print(zoom.zoom3())
