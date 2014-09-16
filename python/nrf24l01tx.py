import Qfunc
import math

class Tx:
	def __init__(self,OS,W,h):
		self.table = Qfunc.Fserial(0.5,OS,1,float(W/2)*h) # W->pi
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
import nrfChan	
import nrf24l01rx

if __name__ == '__main__':
	aTx = Tx(32,1<<16,0.32)
	aPxx = spectrum.spectrum(1024)
	bPxx = spectrum.spectrum(1024)
	
	
	aCh = nrfChan.nrf24l01Channel(0.002) # Eb/N0=27dB
	
	aRx = nrf24l01rx.nrf24l01rx(32)
	
	data = []
	for i in range(0,1024):
		d = random.randint(0,1)
		data.append(d)
	r = aTx.modu(data)
	c = []
	
	phase = 0
	for p in r:
		#phase = phase + (1<<13)
		#phase = phase % (1<<16)
		p = p + phase
		s = complex(math.cos(2.*p*math.pi/(1<<16)),math.sin(2.*p*math.pi/(1<<16)))
		cs = aCh.ce(s)
		rx = aRx.ce(cs)
		#aPxx.push(s)
		#bPxx.push(cs)
		c.append(rx)
		
		
	#apxx = aPxx.out()
	#bpxx = bPxx.out()

	#plot(10./log(10.)*log(apxx))
	#plot(10./log(10.)*log(bpxx))
	#show()
	
	e = [0 for i in range(96)]
	for d in data:
		for i in range(32):
			e.append((1-2*d)*0.01)
			
	plot(e)
	plot(c)
	
	show()
	grid('on')
	

	