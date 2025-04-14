from matplotlib import pyplot as plt

from internal.controllers.main_controller import MainController

ctrl = MainController()
image_path = 'diego.png'
ctrl.carregarImg(image_path)

print("zomm")
ctrl.zoomImg(2,printImg=False)
print("rotacionar")
ctrl.rotacionarImg(20,printImg=True)
print("deblur")
ctrl.deblurImg(0.5,printImg=True)
