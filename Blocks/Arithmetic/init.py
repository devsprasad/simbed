import math
class TypeArithmetic(object):
	# attribs
	constant = 0

	# inputs
	N = 1
	X = 0
	Y = 1
	Base = 0

	def __init__(self):
		super(TypeArithmetic, self).__init__()
	def Add(self,t):
		if isinstance(self.X,list) or isinstance(self.Y,list):
			if isinstance(self.Y,list) and isinstance(self.X,list):
				if len(self.X)!=len(self.Y):
					raise Exception("length of the lists must be same")
				return [self.X[i] + self.Y[i] for i in range(len(self.X))]
			if isinstance(self.Y,list):
				return [self.X + self.Y[i] for i in range(len(self.X))]				
			else:
				return [self.X[i] + self.Y for i in range(len(self.X))]				
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
	def log(self,t):
		return math.log(self.X,self.Base)
	def antilog(self,t):
		return pow(self.Base,self.X)
	def absolute(self,t):
		return abs(self.X)
	def factorial(self,t):
		return math.factorial(self.N)
	def Exponential(self,t):
		return pow(self.Y,self.X)

