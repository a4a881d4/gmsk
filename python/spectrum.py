import numpy.fft
import math

class spectrum:
	def __init__(self,N):
		self.N = N
		self.pxx = [ 0. for i in range(N) ]
		self.frame = 0
		self.buf = [ 0. for i in range(N) ]
		self.pos = 0
			
	def push(self,d):
		self.buf[self.pos] = d
		self.pos = self.pos + 1
		if self.pos==self.N:
			self.pos = 0
			f = numpy.fft.fft(self.buf,self.N)
			for i in range(self.N):
				self.pxx[i] = self.pxx[i] + f[i]*f[i].conjugate()
			self.frame = self.frame + 1
	
	def normalize(self,p):
		ret = p/self.frame/self.N
		return ret.real
				
	def out(self):
		if self.frame==0:
			return []
		else:
			ret = [ 0. for i in range(self.N/2+1) ]
			for i in range(len(ret)):
				if i==0:
					a = self.normalize(self.pxx[i])
				else:
					a = self.normalize(self.pxx[i]+self.pxx[self.N-i])
				ret[i] = a #10.*math.log(a+1e-30,10)
			return ret
		 