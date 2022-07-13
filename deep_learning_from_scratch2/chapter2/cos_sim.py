import numpy as np


def cos_similarity(x, y, eps=1e-8):  # 분모가 0이 나오면 나눗셈이 안되어서 epsilon을 설정해 작은 값을 더해줌.
    nx = x / (np.sqrt(np.sum(x ** 2)) + eps)
    ny = y / (np.sqrt(np.sum(y ** 2)) + eps)

    return np.dot(nx, ny)
