import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *

class DelayObject(object):
	
	__value_old = 0
	__value_new = 0
	t = -1
	
	@property
	def Initial(self):
		return self.__value_old

	@Initial.setter
	def Initial(self,value):
		self.__value_old = value

	@property
	def Input(self):
	    return self.__value_new
	
	@Input.setter
	def Input(self,value):
		self.__value_old = self.__value_new
		self.__value_new = value

	def __init__(self):
		super(DelayObject, self).__init__()
		self.t = sim.SimTime.Start

	def generic_delay(self,t):
		return self.__value_old

class GenericDisplay(object):
	__displyForm = None
	__rtfBox = None
	_Text = ""

	# Attribs
	Title = "Display"

	@property
	def Text(self):
	    return self._Text
	@Text.setter
	def Text(self,value):
		self._Text = str(value)

	def __setup(self):
		self.__displyForm = Form()
		self.__rtfBox = RichTextBox()
		self.__rtfBox.Dock = DockStyle.Fill
		self.__displyForm.Controls.Add(self.__rtfBox)

	def __init__(self):
		super(GenericDisplay, self).__init__()
		self.__setup()

	def Show(self,t):
		self.__displyForm.Text = self.Title
		if self.__displyForm.IsDisposed: self.__setup()
		if not self.__displyForm.Visible: self.__displyForm.Show()
		self.__rtfBox.AppendText(self.Text + "\n")
		return self.Text

class Generic(object):
	# attributes
	Value = None
	Queue = []

	def __init__(self):
		super(Generic, self).__init__()
		
	def generic_Queue(t):
		if len(self.Queue) > 0:
			return self.Queue.pop(0)
		else:
			raise Exception("Queue empty") 

	def generic_print(self,t):
		print(str(self.Value))

	def generic_Buffer(self,t):
		return self.Value

	def TrueOrFalse(self,t):
		if eval(condition):
			return T
		else:
			return F

