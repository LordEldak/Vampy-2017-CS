import turtle
def star(n,k, size):
	angle = k*360/n
	for i in range(n):
		turtle.forward(size)
		turtle.right(angle)

def spiro(n,size):

