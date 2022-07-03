import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y = np.array([1,2,3,4])


x1 = np.array([1,4,6,8])
y1 = np.array([1,2,6,8])

plt.title('Growth')
plt.plot(x,y,'gs')  #fromatters -> ro, b-, gs
plt.plot(x1,y1, color='y', label='growth')
#simple graph
plt.xlabel('x-axis', fontsize = 14, color='r')
plt.ylabel('y-axis', fontsize = 14, color='r')

plt.legend()

'''
plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.plot(x,y)
'''

plt.show()


