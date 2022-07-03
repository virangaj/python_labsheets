import math
import matplotlib.pyplot as plt
import numpy as np

def create_graph():
    x = np.arange(0, math.pi/2, 0.1)
    print(x)
    y = np.sin(x) *5 - 12
    print(y)
    plt.plot(x,y,color='r')
    
    
    t = np.arange(0, 5, 0.1)
    print(t)
    f = 2*t+3
    plt.plot(t,f, color='r')

    plt.show()
create_graph()