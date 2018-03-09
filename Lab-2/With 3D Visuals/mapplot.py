import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import time

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

def animate(i):
    pullData = open("/Users/nitomar/PycharmProjects/SP-18/Sithu - CMPE 273/Assignment-1/.ipynb_checkpoints/example.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    zar = []
    l = 0
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y,z = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
            zar.append(int(z))
#            if l == 0:
#                markers_on = [xar[0],yar[0],zar[0]]
#                l += 1
    ax1.clear()
#    if l > 0:
#        ax1.plot(xar,yar,zar,'-rD', markevery=markers_on)
#    else:
    ax1.plot(xar, yar, zar)
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
