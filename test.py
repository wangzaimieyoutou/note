import cv2
import matplotlib_inline.backend_inline
import numpy as np
import matplotlib as plt
import pandas as pd

data=pd.read_excel("gong.xlsx", usecols=['W001'])
print(data)
data.sort_index()
stock_rise=data['W001']
stock_rise.cumsum
stock_rise.cumsum().plot()

