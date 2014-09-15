import Qfunc
import math

class Tx:
	def __init__(self,OS,W,h):
		self.table = Qfunc.Fserial(0.5,OS,1,float(W/2)*h) # W->pi
		print len(self.table)
		self.os = OS
		self.w = W
		self.h = h
		
	def modu(self,d):
		r = [ 0 for i in range(self.os)]
		
		p = 0
		for x in d:
			for i in range(self.os):
				r.append(p)
			for i in range(2*self.os):
				r[i-2*self.os] = r[i-2*self.os]+(1-2*x)*self.table[i]
				r[i-2*self.os] = r[i-2*self.os] % self.w
			p = p + int((1-2*x)*float(self.w/2)*self.h)
			p = p % self.w
			
		return r
from matplotlib.pylab import *
import spectrum
import random
	
if __name__ == '__main__':
	aTx = Tx(32,1<<16,0.32)
	aPxx = spectrum.spectrum(1024)

	data = []
	for i in range(0,3840):
		d = random.randint(0,1)
		data.append(d)
	r = aTx.modu(data)
	x = []
	y = []
	phase = 0
	for p in r:
		phase = phase + (1<<13)
		phase = phase % (1<<16)
		p = p + phase
		x.append(math.cos(2.*p*math.pi/(1<<16)))
		y.append(math.sin(2.*p*math.pi/(1<<16)))
		aPxx.push(math.cos(2.*p*math.pi/(1<<16)))
		
	pxx = aPxx.out()

	plot(10./log(10.)*log(pxx))
	show()

	