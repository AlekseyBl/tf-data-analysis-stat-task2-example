import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 6130040059 # Ваш chat ID, не меняйте название переменной


    def solution(p: float, x: np.array) -> tuple:
    mean1 = 2 / 59 ** 2 * (gamma.ppf((1 - p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    mean2 = 2 / 59 ** 2 * (gamma.ppf((1 + p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    return mean1, mean2
