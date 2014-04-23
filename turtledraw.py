# author: yashvaishnav

import turtle

n = 100
length = 112
#angle = 180 - (180 * (n - 2) / n)
colors = ["red", "blue", "green", "yellow"]
numbers = range(0, 100)

t = turtle.Turtle()

for number in numbers:
	t.forward(number)
	t.left(25)
