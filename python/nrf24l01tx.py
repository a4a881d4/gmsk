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
import sync
import pilot

if __name__ == '__main__':
	
	Frames = 100
	errorA = 0
	
	aTx = Tx(32,1<<16,0.32)
	
	aCh = nrfChan.nrf24l01Channel(0.5) # Eb/N0=27dB
	
	aRx = nrf24l01rx.nrf24l01rx(2)
	
	for frame in range(Frames):
		data = pilot.pilot(1)
		for i in range(0,256):
			d = random.randint(0,1)
			data.append(d)
			
		data.append(0)
		data.append(1)
		data.append(0)
		
		r = aTx.modu(data)
		c = []
		
		phase = 0
		k = 1
		for p in r:
			p = p + phase
			phase = phase + 0
			s = complex(math.cos(2.*p*math.pi/(1<<16)),math.sin(2.*p*math.pi/(1<<16)))
			cs = aCh.ce(s)
			if k==16:
				k = 0
				rx = aRx.ce(cs)
				c.append(rx)
			k = k + 1
			
		
		( pos, ret ) = sync.sync(c[0:2*60],2)
		
		print pos
		
		pos = pos - 2*40
		
		rec = []
		for i in range(256+40):
			cd = c[pos]
			if cd<0:
				rec.append(1)
			else:
				rec.append(0)
			pos = (pos + 2) % len(c)
			
		error = 0
		for i in range(256):
			if data[i+40]!=rec[i+40]:
				error = error + 1
		print 'fn=',frame,' err=',error
		errorA = errorA + error
		
	print "Error Rate = ",float(errorA)/Frames/256
	
			
	
	
	

	