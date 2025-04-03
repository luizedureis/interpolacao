from matplotlib import pyplot as plt

from internal.controllers.main_controller import MainController

ctrl = MainController()
image_path = 'diego.png'
ctrl.carregarImg(image_path)


ctrl.zoomImg(2,printImg=True)
ctrl.zoomImg(1,printImg=True)
ctrl.zoomImg(0.67,printImg=True)
