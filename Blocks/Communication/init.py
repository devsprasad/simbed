import math
def nsinusoid(f,time_end = 1.0,phase = 0.0,sample_rate = -1):
	"""Generates a sinusoid of given length in time scale"""
	overSampRate=31.5
	if sample_rate == -1:
		sample_rate = overSampRate * f 
	tmp = 0
	t = []
	while tmp < time_end:
		t.append(tmp)
		tmp += (1.0/sample_rate)
	x = [math.sin(2.0*math.pi*f*ti+phase) for ti in t]
	return (x,t)

class Channels(object):

	Tx = []
	def __init__(self):
		super(Channels, self).__init__()
	
	def Ideal(self,t):
		return self.Tx

	def AWGN(self,t):
		return self.Tx



class Modulator(object):

	__data = []
	Carrier_Frequency = 1
	Bit_Duration = 1
	sample_rate = 100



	def __init__(self):
		super(Modulator, self).__init__()

	def TimeScale(self,t):
		t = []
		tmp = 0.0
		step = 1.0/(self.Carrier_Frequency * self.sample_rate)
		while tmp < (self.Bit_Duration * len(self.__data)):
			t.append(tmp)
			tmp += step
		return t

	def Output(self,t):
		"""modulator for Amplitude Shift Keying(ASK) scheme"""
		modulated = []
		ct_one = nsinusoid(self.Carrier_Frequency,self.Bit_Duration,0,self.sample_rate)[0]
		ct_zro = [0 for i in range(len(ct_one))]
		for bit in self.__data:
			bit = int(bit)
			if bit == 1: modulated.extend(ct_one)
			else: modulated.extend(ct_zro)
		return modulated
	
	@property
	def Data(self):
	    return self.__data
	@Data.setter
	def Data(self,value):
		if isinstance(value,str) : value = list(value)
		self.__data = value

	