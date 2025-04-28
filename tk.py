import tkinter as tk
import threading

# def start_tkinter():
#     def valor_soltado(event):
#         valor = slider.get()
#         print(f"Valor selecionado: {valor}")

#     root = tk.Tk()
#     root.title("Selecionar Valor")
#     root.geometry("300x120")

#     tk.Label(root, text="Deslize a barra e solte:").pack(pady=10)

#     global slider
#     slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250)
#     slider.pack()

#     # Evento que dispara quando o botão do mouse é solto
#     slider.bind("<ButtonRelease-1>", valor_soltado)

#     root.mainloop()

# # Inicia o Tkinter em uma thread separada
# threading.Thread(target=start_tkinter).start()

# print("[Main] Interface iniciada. Ajuste o slider para ver o valor.")

import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import threading
import math

from fontTools.unicodedata import block

from internal.controllers.main_controller import MainController

class IDE:
    def __init__(self):
        self.ctrl = MainController()
        self.imagem_atual_path = "diego.png"
        self.imagem_np = None  # Armazenar a imagem em formato numpy array
        self.imagem_pil = None  # Armazenar a imagem no formato PIL
        self.img_label = None  # Label onde a imagem será exibida
        self.imagem_exibida = None

    def zoom(self, img_np_array, zoom_factor, offset_x=0, offset_y=0):
        # Dimensões da imagem
        width, height, _ = img_np_array.shape

        # Determinar a nova largura e altura com base no fator de zoom
        zoom_width = int(width / zoom_factor)
        zoom_height = int(height / zoom_factor)

        # Definir o centro da área de zoom com deslocamento
        center_x = width // 2 + offset_x
        center_y = height // 2 + offset_y

        # Garantir que o deslocamento não faça o recorte ultrapassar os limites da imagem
        left = max(center_x - zoom_width // 2, 0)
        top = max(center_y - zoom_height // 2, 0)
        right = min(center_x + zoom_width // 2, width)
        bottom = min(center_y + zoom_height // 2, height)

        # Cortar a imagem para obter a região do zoom
        cropped_img = img_np_array[top:bottom, left:right]
        return np.array(cropped_img)

    def valor_rotacao(self, event):
        angulo = slider_rotacao.get()
        def process(angulo):
            self.ctrl.rotacionarImg(angulo)
            self.atualizar_imagem(self.ctrl.img.image)
        threading.Thread(target=process, args=(angulo,), daemon=True).start()

    def valor_zoom(self, event):
        valor = slider_zoom.get()
        def process(valor):
            self.ctrl.img.image = self.zoom(self.ctrl.img.image, valor)
            self.atualizar_imagem(self.ctrl.img.image)
        threading.Thread(target=process, args=(valor,), daemon=True).start()

    def carregar_imagem(self, caminho):
        try:
            img = Image.open(caminho).convert("RGB")
            self.imagem_pil = img
            self.imagem_np = np.array(img)  # Converte para numpy array para manipulação
            print(f"Imagem carregada com sucesso: {caminho}")
            return ImageTk.PhotoImage(img.resize((200, 200)))  # Retorna uma versão redimensionada para exibição
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            return None

    def atualizar_imagem(self, image):
        # Converte a imagem NumPy para PIL, redimensiona e converte para PhotoImage
        img_tk = ImageTk.PhotoImage(Image.fromarray(self.ctrl.img.image).resize((200, 200)))
        # Atualiza a imagem no Label existente
        self.imagem_exibida = img_tk
        self.img_label.config(image=self.imagem_exibida)

    def executar_deblur(self):
        def process():
            self.botao_deblur.config(bg="yellow", state="disabled")
            slider_rotacao.config(state="disabled")
            slider_zoom.config(state="disabled")
            self.reset_button.config(state="disabled")
            self.ctrl.deblurImg(8)
            self.atualizar_imagem(self.ctrl.img.image)
            print("Deblur executado!")
            self.botao_deblur.config(bg="green", state="normal")
            slider_rotacao.config(state="normal")
            slider_zoom.config(state="normal")
            self.reset_button.config(state="normal")

        threading.Thread(target=process,daemon=True).start()
    def reset(self):
        self.ctrl.carregarImg("diego.png")
        self.atualizar_imagem(self.ctrl.img.image)
        slider_zoom.set(0)
        slider_rotacao.set(0)

    def run(self):
        root = tk.Tk()
        root.title("App de Imagens")
        root.geometry("600x350")

        frame_esquerdo = tk.Frame(root)
        frame_esquerdo.pack(side="left", padx=10, pady=10)

        self.frame_direito = tk.Frame(root)
        self.frame_direito.pack(side="right", padx=10, pady=10)

        tk.Label(frame_esquerdo, text="Controles", font=("Arial", 12)).pack(pady=5)

        # Controle de rotação
        tk.Label(frame_esquerdo, text="Controle de rotação", font=("Arial", 10)).pack(pady=5)
        global slider_rotacao
        slider_rotacao = tk.Scale(frame_esquerdo, from_=0, to=360, orient="horizontal", length=250)
        slider_rotacao.pack(pady=5)
        slider_rotacao.bind("<ButtonRelease-1>", self.valor_rotacao)

        # Controle de zoom
        tk.Label(frame_esquerdo, text="Controle de Zoom", font=("Arial", 10)).pack(pady=5)
        global slider_zoom
        slider_zoom = tk.Scale(frame_esquerdo, from_=1, to=3, resolution=1, orient="horizontal", length=250)
        slider_zoom.pack(pady=5)
        slider_zoom.bind("<ButtonRelease-1>", self.valor_zoom)

        # Botão Deblur
        tk.Label(frame_esquerdo, text="Controle de Deblur", font=("Arial", 10)).pack(pady=5)
        self.botao_deblur = tk.Button(frame_esquerdo, text="Executar Deblur", command=self.executar_deblur)
        self.botao_deblur.pack(pady=5)

        self.reset_button = tk.Button(frame_esquerdo, text="Reset", command=self.reset)
        self.reset_button.pack(pady=5)

        # Carregar e mostrar imagem inicial
        self.ctrl.carregarImg(self.imagem_atual_path)
        img_tk = ImageTk.PhotoImage(Image.fromarray(self.ctrl.img.image).resize((200, 200)))
        self.imagem_exibida = img_tk
        self.img_label = tk.Label(self.frame_direito, image=self.imagem_exibida)
        self.img_label.pack()

        root.mainloop()


# Iniciar interface em uma thread separada
# start_tkinter
# threading.Thread(target=start_tkinter).start()
IDE().run()