import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

x = [x / 10.0 for x in range(-250, 250, 1)]
b = [x / 10.0 for x in range(-250, 5000, 4)]
dist = [math.cos(x[i]) for i in range(len(x))]

upDist = []

x_up = []
y_up = []
for i in range(len(x)):
    -1 * math.tan(b[i]) * x[i]
    x_up.append(dist[i]/math.sqrt(1+math.pow(math.tan(b[i]), 2)))
    ee = -math.tan(b[i])
    eee = dist[i]/math.sqrt(1+math.pow(math.tan(b[i]), 2))
    y_up.append(ee * eee)


plt.axhline(0, color='black',linewidth=0.5) 
plt.axvline(0, color='black',linewidth=0.5) 

plt.axhline(0, color='gray',linewidth=0.5, linestyle='--') 
plt.axvline(0, color='gray',linewidth=0.5, linestyle='--')  

plt.scatter(x_up, y_up, c="r")

plt.show()