import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y = np.array([1,2,3,4])

#plt.plot(x,y)
#simple graph
plt.xlabel('x-axis', fontsize = 14, color='r')
plt.ylabel('y-axis')

plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.plot(x,y)


plt.show()


