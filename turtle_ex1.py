import turtle


wn = turtle.Screen()
wn.title("New")
wn.setup(width=600, height=500, startx=0, starty=0)
t = turtle.Turtle()


t.width(0.1)

for c in ['red', 'blue', 'yellow', 'black']: # 'red', '#00ff00', '#fa0', 'rgb(0,0,200)'
    t.color(c)
    t.forward(200)
    t.left(90)

wn.reset()


wn.setup(width=600, height=500, startx=None, starty=None)
t1 = turtle.Turtle()
t1.color('red', 'yellow')
t1.begin_fill()
while True:
    t1.forward(200)
    t1.left(170)
    if abs(t1.pos()) < 1:
        break
t1.end_fill()
wn.mainloop()
