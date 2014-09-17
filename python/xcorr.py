class xcorr:
	def __init__(self,OS,seq):
		self.seq = seq
		self.os = OS
		self.pos = 0
		self.buf = [ 0 for i in range(OS*len(seq))]
		self.size = OS*len(seq)
		
	def ce(self,din):
		self.buf[self.pos]=din
		p = self.pos
		r = 0.
		for s in self.seq:
			d = 1-2*s
			r = r + d * self.buf[p]
			p = ( p + self.os ) % self.size
			
		self.pos = (self.pos+1)%self.size
		return r
		