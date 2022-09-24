# Draw squares

import turtle
skk = turtle.Turtle()

for j in range(20):
	for i in range(4):
		skk.forward(5 + 3*j)
		skk.left(90)
	
turtle.done()