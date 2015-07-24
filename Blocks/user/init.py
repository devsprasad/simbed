class HalfAdderType(object):
    sum = None
    carry = None
    A = None
    B = None
    def __init__(self):
        super(HalfAdderType,self).__init__()
        self.sum = DigitalBasic()
        self.carry = DigitalBasic()
        self.A = DigitalBasic()
        self.B = DigitalBasic()
    def init(self,t):
        self.sum.A = self.A.logic_buffer(t)
        self.sum.B = self.B.logic_buffer(t)
        self.carry.A = self.A.logic_buffer(t)
        self.carry.B = self.B.logic_buffer(t)
    @property
    def A_Value(self):
        return self.A.Value

    @A_Value.setter
    def A_Value(self,value):
        self.A.Value = value
        self.init(0)

    @property
    def B_Value(self):
        return self.B.Value

    @B_Value.setter
    def B_Value(self,value):
        self.B.Value = value
        self.init(0)

    def sum_Y(self,t):
        return self.sum.logic_XOR(0)
    def carry_Y(self,t):
        return self.carry.logic_AND(0)
class FullAdderType(object):
    HA1 = None
    HA2 = None
    A = None
    B = None
    Cin = None
    Cout = None
    def __init__(self):
        super(FullAdderType,self).__init__()
        self.HA1 = HalfAdderType()
        self.HA2 = HalfAdderType()
        self.A = DigitalBasic()
        self.B = DigitalBasic()
        self.Cin = DigitalBasic()
        self.Cout = DigitalBasic()
    def init(self,t):
        self.HA1.A_Value = self.A.logic_buffer(t)
        self.HA1.B_Value = self.B.logic_buffer(t)
        self.HA2.A_Value = self.HA1.sum_Y(t)
        self.HA2.B_Value = self.Cin.logic_buffer(t)
        self.Cout.A = self.HA1.carry_Y(t)
        self.Cout.B = self.HA2.carry_Y(t)
    @property
    def A_Value(self):
        return self.A.Value

    @A_Value.setter
    def A_Value(self,value):
        self.A.Value = value
        self.init(0)

    @property
    def B_Value(self):
        return self.B.Value

    @B_Value.setter
    def B_Value(self,value):
        self.B.Value = value
        self.init(0)

    @property
    def Cin_Value(self):
        return self.Cin.Value

    @Cin_Value.setter
    def Cin_Value(self,value):
        self.Cin.Value = value
        self.init(0)

    def HA2_sum_Y(self,t):
        return self.HA2.sum_Y(0)
    def Cout_Y(self,t):
        return self.Cout.logic_OR(0)
