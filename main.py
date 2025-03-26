from internal.use_case.load_img import Load_Image
from internal.use_case.zoom import redimensionar

image_path = 'img.png'
li = Load_Image()
img = li.run(image_path)

imagem_com_zoom = redimensionar(img,10,*img.size)

imagem_com_zoom.show()