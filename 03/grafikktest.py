from ezgraphics import GraphicsWindow
win = GraphicsWindow(1200,200)
canvas = win.canvas()
# canvas.drawRectangle(20,20,50,75)
# canvas.drawOval(40,40,30,30)
for i in range(1,10):
    canvas.drawOval(40,40,i**3+2*i,i**2)
win.wait()
