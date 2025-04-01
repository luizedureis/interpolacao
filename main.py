from internal.controllers.main_controller import MainController

ctrl = MainController()
image_path = 'diego.png'

ctrl.carregarImg(image_path)
ctrl.deblurImg()
ctrl.zoomImg()
ctrl.rotacionarImg(90)





