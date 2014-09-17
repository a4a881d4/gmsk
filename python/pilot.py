import mseq
def pilot(s):
	r = [0,1,0,1,0,1,0,1,0]
	aS = mseq.mseq(0x25)
	aS.set(s)
	for x in range(31):
		r.append(aS.ce())
	return r
	