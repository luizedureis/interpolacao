from typing import Any
import numpy as np

class Zoom:

    def __init__(self, matriz):
        self.matriz: np.ndarray[Any, np.dtype] = matriz

    def zoom3(self):
        qnt_lin, qnt_col = self.matriz.shape
        qnt_lin_new = round(qnt_lin * 0.3)
        qnt_col_new = round(qnt_col * 0.3)

        return self.matriz[qnt_lin_new:qnt_lin - qnt_lin_new, qnt_col_new:qnt_col - qnt_col_new]
