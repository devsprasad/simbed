class TypeArithmetic(object):
	# attribs
	constant = 0

	# inputs
	X = 0
	Y = 1

	def __init__(self):
		super(TypeArithmetic, self).__init__()
	def Add(self,t):
		return self.X+self.Y
	def Sub(self,t):
		return self.X-self.Y
	def Mul(self,t):
		return self.X*self.Y
	def Square(self,t):
		return pow(self.X,2)
	def Cube(self,t):
		return pow(self.X,3)
	def Div(self,t):
		return self.X/self.Y
	def Constant(self,t):
		return self.constant



