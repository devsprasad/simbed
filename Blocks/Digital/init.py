class DigitalBasic(object):

	# attribs 
	__Value = None

	@property
	def Value(self):
	    return self.__Value

	@Value.setter
	def Value(self,value):
		self.__Value = value

	# inputs
	A = False
	B = False

	def __init__(self):
		super(DigitalBasic, self).__init__()
		self.Value = False
		self.A = False
		self.B = False
		
	def logic_buffer(self,t):
		return self.Value

	def logic_high(self,t):
		return True

	def logic_low(self,t):
		return False

	def logic_AND(self,t):
		if self.A in [True,False] and self.B in [True,False]:
			return self.A & self.B

	def logic_OR(self,t):
		if self.A in [True,False] and self.B in [True,False]:
			return self.A | self.B

	def logic_NOT(self,t):
		if self.A in [True,False]:
			return not self.A

	def logic_XOR(self,t):
		if self.A in [True,False] and self.B in [True,False]:
			return self.A ^ self.B

	def logic_XNOR(self,t):
		if self.A in [True,False] and self.B in [True,False]:
			return ~(self.A ^ self.B)

	def logic_NOR(self,t):
		if self.A in [True,False] and self.B in [True,False]:
			return ~(self.A | self.B)

	def logic_NAND(self,t):
		if self.A in [True,False] and self.B in [True,False]:
			return ~(self.A & self.B)	


class DelayObject(object):
	
	__value_old = 0
	__value_new = False
	
	@property
	def Initial(self):
		return self.__value_old

	@Initial.setter
	def Initial(self,value):
		self.__value_old = value
		self.__value_new = value

	@property
	def Input(self):
	    return self.__value_new
	
	@Input.setter
	def Input(self,value):
		self.__value_old = self.__value_new
		self.__value_new = value

	def __init__(self):
		super(DelayObject, self).__init__()

	def generic_delay(self,t):
		return self.__value_old


