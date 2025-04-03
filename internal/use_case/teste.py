import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def unsharp_mask_manual(image, amount=1.5):
    height, width, _ = image.shape
    blurred = np.zeros_like(image, dtype=np.float32)

    # Aplicar um filtro de desfoque (média simples)
    kernel_size = 3
    pad = kernel_size // 2
    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            blurred[i, j] = np.mean(image[i - pad:i + pad + 1, j - pad:j + pad + 1], axis=(0, 1))

    # Aplicar máscara de nitidez
    sharpened = image + amount * (image - blurred)
    sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
    return sharpened


def laplacian_sharpen_manual(image):
    height, width, _ = image.shape
    sharpened = np.zeros_like(image, dtype=np.float32)

    # Filtro Laplaciano
    kernel = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])
    pad = 1

    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            region = image[i - pad:i + pad + 1, j - pad:j + pad + 1]
            sharpened[i, j] = np.sum(region * kernel[..., np.newaxis], axis=(0, 1))

    sharpened = np.clip(image - sharpened, 0, 255).astype(np.uint8)
    return sharpened


def wiener_deconvolution_manual(image, kernel_size=3, noise_power=0.01):
    height, width, _ = image.shape
    restored = np.zeros_like(image, dtype=np.float32)

    # Criar kernel de desfoque (média)
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    pad = kernel_size // 2

    # Aplicar deconvolução simplificada
    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            region = image[i - pad:i + pad + 1, j - pad:j + pad + 1]
            conv = np.sum(region * kernel[..., np.newaxis], axis=(0, 1))
            restored[i, j] = image[i, j] / (conv + noise_power)

    restored = np.clip(restored * 255, 0, 255).astype(np.uint8)
    return restored


def load_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Garantir que a imagem esteja no formato RGB
    return np.array(img)


# Carregar imagem
image_path = 'diego.png'  # Substitua pelo caminho da sua imagem
image = load_image(image_path)

# Aplicar filtros
unsharp_result = unsharp_mask_manual(image)
laplacian_result = laplacian_sharpen_manual(image)
wiener_result = wiener_deconvolution_manual(image)

# Mostrar imagens
fig, ax = plt.subplots(1, 4, figsize=(15, 5))
ax[0].imshow(image)
ax[0].set_title('Original')
ax[1].imshow(unsharp_result)
ax[1].set_title('Unsharp Mask')
ax[2].imshow(laplacian_result)
ax[2].set_title('Laplacian')
ax[3].imshow(wiener_result)
ax[3].set_title('Wiener Deconvolution')
for a in ax:
    a.axis('off')
plt.show()