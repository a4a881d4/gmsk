class Fir:
	def __init__(self,coef,len):
		self.coef = coef
		self.buf = [ 0. for i in range(len) ]
		self.pos = 0
		self.len = len
		
	def ce(self,d):
		self.buf[self.pos] = d
		self.pos = ( self.pos + 1 ) % self.len
		sum = 0.
		for i in range( self.len ):
			sum = sum + self.coef[i]*self.buf[self.pos-i]
		return sum
		
if __name__=='__main__':
	coef = [ float(i) for i in range(16) ]
	aFir = Fir( coef, 16 )
	r = []
	r.append( aFir.ce(0.) )
	r.append( aFir.ce(1.0) )
	for i in range(32):
		r.append( aFir.ce(0.) )
	print r
	