from functools import wraps

from internal.use_case.load_img import Load_Image
from internal.use_case.rotacionar import Rotacao_Imagem
from internal.use_case.show_img import Show_Image


def verificar_imagem_carregada(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if type(self.img)==bool:
            print(f"{func.__name__}: Nenhuma imagem foi carregada.")  # Exibe o nome da função
            return
        return func(self, *args, **kwargs)
    return wrapper

class MainController:
    __loadImage:Load_Image
    __rotacionar:Rotacao_Imagem
    __showImage:Show_Image

    def __init__(self):
        self.__loadImage = Load_Image()
        self.__rotacionar = Rotacao_Imagem()
        self.__showImage = Show_Image()
        self.img = False

    def carregarImg(self, img_path:str):
        self.img = self.__loadImage.run(img_path)

    @verificar_imagem_carregada
    def printImg(self):
        self.__showImage.run(self.img)

    @verificar_imagem_carregada
    def rotacionarImg(self,angulo:int):
        self.img = self.__rotacionar.rotacionar(self.img,angulo)