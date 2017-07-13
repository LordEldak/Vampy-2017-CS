import turtle as t
t.shape("turtle")
t.forward(1)
t.speed(1)


def square(size):

	t.forward(size)
	t.right(90)
	t.forward(size)
	t.right(90)
	t.forward(size)
	t.right(90)
	t.forward(size)
	t.backward(size)
	
square(100)
def rectangle():

	t.right(270)
	t.forward(300)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(300)
	t.left(90)
	t.forward(100)
	t.backward(200)
	t.forward(100)
	t.left(90)
	t.forward(25)
	t.left(90)
	t.forward(100)
		

rectangle()
t.exitonclick()
