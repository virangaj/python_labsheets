import math
import matplotlib.pyplot as plt
import numpy as np

def create_graph():
    x = np.arange(0, math.pi/2, 0.1)
    print(x)
  
    print(y)
    y = np.sin(x) * 5 - 12
    plt.subplot(1,2,1)
    plt.plot(x,y, color='b', label='y=5sin(x)-12')
    
    
    t = np.arange(0, 5, 0.1)
    print(t)
    f = 2*t+3
    plt.subplot(1,2,2)

    plt.plot(t,f, color='r', label='f=2t+3')
    plt.legend()
    plt.show()
create_graph()