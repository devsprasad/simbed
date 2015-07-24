import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *

class QueueType:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
    	if len(self.items) == 0:
    		return None
    	return self.items.pop()

    def size(self):
        return len(self.items)

class UnitDelayType(object):
	delay = 1
	__queue = None

	def __init__(self):
		super(UnitDelayType, self).__init__()
		self.__queue = QueueType()
		for i in range(self.delay):
			self.__queue.enqueue(None)
	
	@property
	def Initial(self):
		return self.__queue.items[-1]

	@Initial.setter
	def Initial(self,value):
		self.__queue.items = []
		for i in range(self.delay):
			self.__queue.enqueue(value)
	
	@property
	def Input(self,value):
		return self.__queue.items[-1]
	
	@Input.setter
	def Input(self,value):
	    self.__queue.enqueue(value)

	def generic_delay(self,t):
		return self.__queue.dequeue()

class DelayType(object):
	__init = None
	delay = 1
	__queue = None

	def __init__(self):
		super(DelayType, self).__init__()
		self.__queue = QueueType()
		for i in range(self.delay):
			self.__queue.enqueue(self.__init)
	
	@property
	def Initial(self):
		return self.__queue.items[-1]

	@Initial.setter
	def Initial(self,value):
		self.__queue.items = []
		self.__init = value
		for i in range(self.delay):
			self.__queue.enqueue(value)
	
	@property
	def Input(self,value):
		return self.__queue.items[-1]
	
	@Input.setter
	def Input(self,value):
	    self.__queue.enqueue(value)

	@property
	def DelayTime(self):
		return self.delay

	@DelayTime.setter
	def DelayTime(self,value):
		self.delay = int(value)
		self.Initial = self.__init

	def generic_delay(self,t):
		return self.__queue.dequeue()





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
	__queue = None

	def __init__(self):
		super(Generic, self).__init__()
		self.__queue = QueueType()
		
	def generic_Queue(t):
		if self.__queue.size() > 0:
			return self.__queue.dequeue()
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

