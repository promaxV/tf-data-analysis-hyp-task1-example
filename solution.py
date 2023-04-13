import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 664256606  # Ваш chat ID, не меняйте название переменной
alpha = 0.02


def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    statistic, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative="larger")

    return p_value < alpha
