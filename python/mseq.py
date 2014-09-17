class mseq:
	def __init__(self,poly):
		self.p = poly
		self.a = 1
		for i in range(32):
			if poly!=1 :
				poly = poly/2
				self.a = self.a * 2
			else:
				break
		self.s = 1
		self.p = self.p - self.a
	
	def set(self,s):
		self.s = s
	
	def _count(self,k):
		ma = self.a
		r = 0
		while(ma!=0):
			if ma&k!=0:
				r = r^1
			ma=ma/2
		return r
		 			
	def ce(self):
		r = self._count(self.s&self.p)
		self.s = self.s>>1
		if r!=0:
			self.s = self.s+self.a/2
		return r
		
if __name__=='__main__':
	aS = mseq(0x25)
	m=[]
	for i in range(64):
		m.append(aS.ce())
		print aS.s
		 