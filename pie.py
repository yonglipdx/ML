import numpy as np
import Tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

d1 = input('enter denomitor: ')
n1 = input('enter numerator: ')
print "%d/%d" % (d1, n1)

d2 = input('enter denomitor: ')
n2 = input('enter numerator: ')
print "%d/%d" % (d2, n2)

root = tk.Tk()
plt.ion()

fig1 = plt.figure(1)
fig2 = plt.figure(2)

def pie_parameters(denomitor, numerator):
  d=1
  sizes = []
  labels = []
  colors= []
  explode= []
  while d<=numerator:
    sizes.append(1)
    labels.append(d)
    if d<=denomitor:
      colors.append("gold")
      explode.append(-0.1)
    else:
      colors.append("green")
      explode.append(0)
    d+=1
  return sizes, labels, colors, explode

sizes, labels, colors, explode = pie_parameters(d1, n1)
explode=tuple(explode)
plt.figure(1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=False)
plt.axis('equal')

sizes, labels, colors, explode = pie_parameters(d2, n2)
explode=tuple(explode)
plt.figure(2)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=False)
plt.axis('equal')

canvas1 = FigureCanvasTkAgg(fig1, master=root)
plot_widget1 = canvas1.get_tk_widget()

canvas2 = FigureCanvasTkAgg(fig2, master=root)
plot_widget2 = canvas2.get_tk_widget()

def update_1():
  update_1.count_1 += d1
  update_1.count_2 += n1
  sizes, labels, colors, explode = pie_parameters(update_1.count_1, update_1.count_2)
  explode=tuple(explode)
  plt.figure(1)
  plt.cla()
  plt.clf()
  plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=False)
  plt.axis('equal')
  fig1.canvas.draw()
update_1.count_1=d1
update_1.count_2=n1

def update_2():
  update_2.count_1 += d2
  update_2.count_2 += n2
  sizes, labels, colors, explode = pie_parameters(update_2.count_1, update_2.count_2)
  explode=tuple(explode)
  plt.figure(2)
  plt.cla()
  plt.clf()
  plt.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=False)
  plt.axis('equal')
  fig2.canvas.draw()
update_2.count_1=d2
update_2.count_2=n2

plot_widget1.grid(row=0, column=0)
plot_widget2.grid(row=0, column=1)

fraction1 = "%d/%d Next equivalent" % (d1, n1)
tk.Button(root,text=fraction1,command=update_1).grid(row=1, column=0)

fraction2 = "%d/%d Next equivalent" % (d2, n2)
tk.Button(root,text=fraction2,command=update_2).grid(row=1, column=1)

root.mainloop()
