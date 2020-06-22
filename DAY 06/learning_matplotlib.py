import numpy as np
from matplotlib import pyplot as plt

# x = np.array([1,2,3,4])
# y = np.array([5,6,7,8])


# plt.style.use('fivethirtyeight')
plt.xkcd()

x=np.arange(0,3*np.pi,0.1)
y1=np.sin(x)
y2=np.cos(x)


plt.xlabel('value of theta')
plt.ylabel('value of sin theta')
plt.title('values of sin and cos')


plt.plot(x, y1, label="sin graph")
plt.plot(x, y2, label="cos graph")
plt.legend()
plt.savefig('plot.png')
plt.show()


