from internal.controllers.main_controller import MainController

ctrl = MainController()
image_path = 'diego.png'

img = ctrl.carregarImg(image_path)
img_rotacionado = ctrl.rotacionarImg(img,20)
ctrl.printImg(img_rotacionado)
