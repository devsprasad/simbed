class ManchesterCoder(object):

	Encoder = True

	Data = []

	def __init__(self):
		super(Encoder, self).__init__()
	
	def __encode(self,t):
		return 0

	def __decode(self,t):
		return 0 

	def Output(self,t):
		if 	self.Encoder: return self.__encode(t) 
		return self.__decode(t)