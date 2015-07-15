import re

class InvalidMAC(Exception):
	def __init__(self,msg = ""):
		super(InvalidMAC, self).__init__()
		self.arg = msg

	def __str__(self):
		return self.arg
		
class MAC(object):
	__addr = ""
	_patrn = r"^([A-F0-9][A-F0-9])\:([A-F0-9][A-F0-9])\:([A-F0-9][A-F0-9])"+\
				"\:([A-F0-9][A-F0-9])\:([A-F0-9][A-F0-9])\:([A-F0-9][A-F0-9])$"
	def __init__(self, arg):
		super(MAC, self).__init__()
		m = re.match(self._patrn,\
					arg, re.IGNORECASE)
		if arg == "" or m is None:
			raise InvalidMAC("mac address is not valid")
		else: 
			self.__addr = arg

	def Address(self):
		return self.__addr

class EthernetFrame(object):

	__preamble = "10101010"*7
	__sof = "1"

	def __init__(self,dst_mac,src_mac,ether_type):
		super(EthernetFrame, self).__init__()


class DeviceNode(object):

	def __init__(self):
		super(DeviceNode, self).__init__()

	def Output(self,t):
		pass
		