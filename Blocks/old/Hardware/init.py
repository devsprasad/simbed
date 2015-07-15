from System.IO.Ports import *
import threading


class Arduino(object):
	# attributes
	PortName = None

	__SERIAL_OBJ = None

	def __init__(self):
		super(Arduino, self).__init__()
		
	def serial_read(t,portName):
		global SerialObject
		if SerialObject is None:
			SerialObject = SerialPort(str(portName))
			SerialObject.Open()
		return SerialObject.ReadLine()

