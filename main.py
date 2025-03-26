from internal.use_case.load_img import Load_Image
from internal.use_case.zoom import Zoom  # Importando dentro da função

image_path = 'img.png'
li = Load_Image()
img = li.run(image_path)

def aplicar_zoom():
    zo = Zoom(img, 5)
    zo.redimensionar().show()

aplicar_zoom()