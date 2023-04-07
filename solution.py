import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 6130040059 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = (2/59**2)*x.mean()
    scale = (2/59**2)*(np.sqrt(np.var(x))-0.5) / np.sqrt(len(x))
    return loc - scale * expon.ppf(1 - alpha / 2), \
           loc - scale * expon.ppf(alpha / 2)
