class VCO:
	def __init__(self,f,Fs,W):
		self.Full = 1<<W
		self.mask = self.Full
		self.acc = int(f/Fs*self.Full+.5)
		self.state = 0
		self.odd = 0
		self.center = int(Fs/f)
		# print self.acc
		
	def ce(self,V,phase):
		self.state = self.state + self.acc*V - self.Full
		return self.state+phase
		
	def output(self,V):
		ret = []
		half = V/2
		for i in range(0,half):
			ret.append(1)
		if (V%2)!=0:
			if self.odd == 0:
				self.odd = 1
				ret.append(1)
			else:
				self.odd = 0
				ret.append(-1)
		for i in range(0,half):
			ret.append(-1)
		return ret
		
	def judge(self,e):
		r = self.center
		if e<-self.Full/32:
			r = self.center+1
		if e>self.Full/32:
			r = self.center-1
		return r
		
		
if __name__=='__main__':
	f = 350e6
	Fs = 6144e6
	W = 24
	aVCO = VCO(f,Fs,W)
	V = 18
	odd = 0
	s0 = 0
	for T in range(0,100000):
		state = aVCO.ce(V,0)
		s0 = (1-1/128.)*s0 + state
		V = aVCO.judge(s0)
		# print "#",state,V
		o = aVCO.output(V)
		for i in range(0,len(o)):
			print o[i]
					