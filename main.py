from internal.controllers.main_controller import MainController

ctrl = MainController()
image_path = 'diego.png'

ctrl.carregarImg(image_path)
ctrl.deblurImg(printImg=True)
#
ctrl.rotacionarImg(90,printImg=True)
#
# ctrl.zoomImg(2)




