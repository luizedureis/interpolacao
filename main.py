
from internal.use_case.load_img import Load_Image
from internal.use_case.show_img import Show_Image

image_path = 'img.png'
li = Load_Image()
img = li.run(image_path)

si = Show_Image()
si.run(img)