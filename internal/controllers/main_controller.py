from functools import wraps

from internal.use_case.Zoom import Zoom
from internal.use_case.deblur import Deblur
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

def verificar_print_flag(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Obtém o argumento printImg da função (se estiver presente)
        print_flag = kwargs.get('printImg', False)

        # Chama a função original primeiro
        resultado = func(self, *args, **kwargs)

        # Se printImg for True, chama printImg automaticamente
        if print_flag:
            self.printImg()

        return resultado
    return wrapper

class MainController:
    def __init__(self):
        self.__loadImage:Load_Image = Load_Image()
        self.__rotacionar:Rotacao_Imagem = Rotacao_Imagem()
        self.__showImage:Show_Image = Show_Image()
        self.__zoomImg: Zoom = Zoom()
        self.__deblurImg: Deblur = Deblur()
        self.img = False

    def carregarImg(self, img_path:str):
        '''
        :param img_path: String
        :return: Retorna imagem carregada para a classe principal
        '''
        self.img = self.__loadImage.run(img_path)

    @verificar_print_flag
    @verificar_imagem_carregada
    def zoomImg(self,zoom_factor:int,printImg:bool=False):
        '''
        Função utilizada para dar zoom em imagens
        :param zoom_factor:int
        :param printImg: bool = False
        :return: retorna a imagem para classe principal
        '''
        self.img = self.__zoomImg.run(self.img,zoom_factor)

    @verificar_imagem_carregada
    def printImg(self):
        self.__showImage.run(self.img)

    @verificar_print_flag
    @verificar_imagem_carregada
    def rotacionarImg(self,angulo:int,printImg:bool=False):
        '''
        :param angulo:int
        :param printImg: Boolean = False
        :return: retorna a imagem para classe principal
        '''
        self.img = self.__rotacionar.rotacionar(self.img,angulo)

    @verificar_print_flag
    @verificar_imagem_carregada
    def deblurImg(self,printImg:bool=False):
        '''
        :param printImg: Boolean = False
        :return: retorna a imagem para classe principal
        '''
        self.img = self.__deblurImg.run(self.img)