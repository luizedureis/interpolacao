import numpy as np


class Deblur:
    def __init__(self):
        pass
    def unsharp_mask_manual(self,image,amount):
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

    def run(self, image,amount):
        return self.unsharp_mask_manual(image.image,amount)


