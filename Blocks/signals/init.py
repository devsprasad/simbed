clr.AddReference("System")
clr.AddReference("mscorlib")

import math
import clr
import System
import alglib

alglib = alglib()

def pad(x,max_len,pad_with = 0):
	if isinstance(x,list):
		while len(x) < max_len:
			x.append(pad_with)
	return x

class SigConv(object):
	_x = System.Array[float]([])
	_y = System.Array[float]([])

	# attribs
	n = -1
	m = -1

	def __init__(self):
		super(SigConv, self).__init__()
	
	@property
	def X(self):
		return self._x
	@X.setter
	def X(self,value):
		self._x	= System.Array[float]([float(x) for x in value])	

	@property
	def Y(self):
		return self._y
	@Y.setter
	def Y(self,value):
		self._y	= System.Array[float]([float(y) for y in value])	

	def block_conv(self,t):
		"""Convolution of x and y
	Syntax: x (+) y = block_conv(x,y)"""
		if self.n == -1: self.n = len(self._x)
		if self.m == -1: self.m = len(self._y)
		return list(alglib.convr1d(self._x,self.n,self._y,self.n))

	def block_xcorr(self,t):
		"""Cross-Correlation of two sequences. 
	Syntax x = xcorr(x,y)"""
		if self.n == -1: self.n = len(self._x)
		if self.m == -1: self.m = len(self._y)
		l = list(alglib.corrr1d(self._y,self.n,self._x,self.m))
		f = l[:self.n][::-1]
		s = l[self.n:][::-1]
		return f+s

	def block_autocorr(self,t):
		"""Auto-Correlation of a sequence
	Syntax: c = autocorr(x) 
	Example: c = autocorr(sinusoid(10,2))"""
		self._y = self._x
		return block_xcorr(t)



class SignalGenerator(object):

	# attribs 
	__f = 1
	__fs = 30

	def __init__(self):
		super(SignalGenerator, self).__init__()
	
	def block_sinusoid(self,t):
		return math.sin(2.0*math.pi*(t/self.__fs)*self.__f)


class SignalProcessor(object):

	Xf = []
	xt = []
	N = 1024

	def __init__(self):
		super(SignalProcessor, self).__init__()
		

	def block_fft(self,t):
		"""Fast-Fourier Transform of xt. N is by default is 1024"""
		xt = pad(self.xt,self.N)
		c = alglib.fftr1d(System.Array[float](xt),self.N)
		ret = [complex(n.x,n.y) for n in c]
		return ret

	def block_ifft(self,t):
		"""Inverse of Fast-Fourier Transform of Xf. N is by default 1024"""
		Xf = System.Array[alglib.complex]([alglib.complex(c.real,c.imag) for c in self.Xf])
		return alglib.fftr1dinv(Xf,self.N)



	def fftshift(self,t):
		"""Shifts the Xf vector to center"""
		l = len(self.Xf)
		l2 = l/2
		xf1 = self.Xf[0:l2]
		xf2 = self.Xf[l2:]
		xf = xf2 + xf1
		return xf


	# def freqvalues(self,t):
	# 	# xt,N = 1024,fs = -1,PSD = False
	# 	if fs == -1 : fs = param("fs")
	# 	if fs is None: fs = 1000
	# 	Px = abs((fft(xt,N)))
	# 	if PSD : Px = [10*math.log10(x/(N*len(xt))) for x in Px]	
	# 	else: Px = [x/(N*len(xt)) for x in Px]	
	# 	Tf = base.div(range(0,N/2),N)
	# 	Tf = base.mul(Tf,fs)
	# 	return (Px[0:N/2],Tf)


