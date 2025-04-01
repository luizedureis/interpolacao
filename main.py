# # Carregar a imagem
# image_path = 'diego.png'
# print("lendo mensagem")
# li = Load_Image()
# img_original = li.run(image_path)
# print("aplicando zoom")
# zo = Zoom(img_original,3)
# image= zo.redimensionar()
# image.show()
# img_original.show()

from internal.use_case.Zoom import zoom_in
# Abrir a imagem

imgs = zoom_in(zoom_factor=3,image_path='diego.png')
imgs.show()


# Exibir a imagem com zoom
