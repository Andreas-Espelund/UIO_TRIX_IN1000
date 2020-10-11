from ezgraphics import GraphicsWindow
from ezgraphics import GraphicsMenu
import time
win = GraphicsWindow()
men = GraphicsMenu()
canvas = win.canvas()
inter = men.inter()
inter.addCheckButton(test,test)


for x in range(50):
    canvas.drawOval(10*x,20,20*x,20*x)
    i = input("")

win.wait()
