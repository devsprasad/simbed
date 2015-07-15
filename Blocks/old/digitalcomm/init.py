

def logic_gray(t,bit):
	global ReferenceBit
	ref = bool(ReferenceBit)
	bit = bool(bit)
	ref = ref ^ bit
	return ref