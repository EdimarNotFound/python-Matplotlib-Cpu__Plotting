#importing module
#please install matplotlib first
#use pip install matplotlib to install library

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style
import psutil
import time

#we are using the bmh style
style.use("bmh")

#lets create a figuee
#you can modify the figsize
#figsize means figure figsize
Figure = plt.figure(figsize=(5,5))

#I'm adding subplot
ax=fig.add_subplot(111)
fig.show()

#creating the plot title
#you can modify it
plt.title("Real Time CPU Info")

#creating variable for i
i = 0
x, y = [], []
while True:
	x.append(i)
	y.append(psutil.cpu_percent())
	ax.plot(x,y,color="C1")
	fig.canvas.draw()
	ax.set_xlim(left=max(0,i-20), right=i+20)
	time.sleep(0.1)
	i+=1