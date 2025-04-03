from matplotlib import pyplot as plt

from internal.controllers.main_controller import MainController

ctrl = MainController()
image_path = 'diego.png'
ctrl.carregarImg(image_path)


ctrl.rotacionarImg(90,printImg=True)
ctrl.zoomImg(4,350,430,printImg=True)
ctrl.rotacionarImg(90,printImg=True)
ctrl.zoomImg(1,350,430,printImg=True)