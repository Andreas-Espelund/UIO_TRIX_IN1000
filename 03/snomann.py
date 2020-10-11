from ezgraphics import GraphicsWindow
win = GraphicsWindow()
win.setTitle("Snømann")
canvas = win.canvas()
canvas.drawOval(170,20,50,50)
canvas.drawOval(145,70,100,100)
canvas.drawOval(125,170,150,150)


win.wait()
