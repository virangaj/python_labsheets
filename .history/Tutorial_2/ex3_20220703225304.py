import math
import matplotlib.pyplot as plt
import numpy as np

def create_graph():
    x = np.arange(0, math.pi/2, 0.1)
    print(x)
    y = np.sin(x) *5 -12
    print(y)
    

create_graph()