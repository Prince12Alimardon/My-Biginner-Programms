import turtle
t= turtle.Pen()
t.width(5)

t.circle(100)

t.left(360)

import turtle
t= turtle.Pen()
t.width(5)
colors=['red', 'blue', 'green', 'violet', 'purple']
t.circle(100)
t.left(360)

for x in range(1):
	t.pencolor(colors[x%3])
	t.circle(100)
	t.left(180)

for a in range(8):
	t.pencolor(colors[x%3])
	t.circle(100)
	t.left(90)

for b in range(10):
	t.pencolor(colors[x%3])
	t.circle(100)
	t.left(45)	

