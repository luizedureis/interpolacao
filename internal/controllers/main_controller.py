
from internal.use_case.load_img import Load_Image
from internal.use_case.rotacionar import Rotacao_Imagem
from internal.use_case.show_img import Show_Image


class MainController:
    __loadImage:Load_Image
    __rotacionar:Rotacao_Imagem
    __showImage:Show_Image

    def __init__(self):
        self.__loadImage = Load_Image()
        self.__rotacionar = Rotacao_Imagem()
        self.__showImage = Show_Image()

    def carregarImg(self, img_path:str):
        return self.__loadImage.run(img_path)

    def printImg(self,img_rgb_format):
        return self.__showImage.run(img_rgb_format)

    def rotacionarImg(self,img,angulo:int):
        return self.__rotacionar.rotacionar(img,angulo)