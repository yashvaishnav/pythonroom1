# author: yashvaishnav

import turtle

n = 8
length = 70
angle = 180 - (180 * (n - 2) / n)
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

t = turtle.Turtle()

for number in numbers:
	t.forward(length)
	t.left(angle)
	
