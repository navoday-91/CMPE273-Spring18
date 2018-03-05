import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import time, json

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

def animate(i):
    f = open("/Users/nitomar/PycharmProjects/SP-18/Sithu - CMPE 273/Assignment-1/.ipynb_checkpoints/serverdata.json",
             "r")
    pullData = json.load(f)
    xar = []
    yar = []
    zar = []
    ax1.clear()
    for drone in pullData:
        list_of_points = pullData[drone]
        xar = []
        yar = []
        zar = []
        for coordinates in list_of_points:
            xar.append(int(coordinates[0]))
            yar.append(int(coordinates[1]))
            zar.append(int(coordinates[2]))
        ax1.plot(xar, yar, zar)
ani = animation.FuncAnimation(fig, animate, interval=400)
plt.show()
