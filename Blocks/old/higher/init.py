class Calculus(object):
	# inputs
	fxValues = []
	LowerLimit = 0
	UpperLimit = 0

	def __init__(self):
		super(Calculus, self).__init__()
		
	def calc_integrator(self,t):
		return Basic.trapz(self.fxValues,self.LowerLimit,self.UpperLimit)
