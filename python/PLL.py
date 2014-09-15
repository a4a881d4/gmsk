class PLL:
	def __init__(self,f,Fs,W):
		self.Full = 1<<W
		self.mask = self.Full
		self.acc = int(f/Fs*self.Full+.5)
		self.state = 0
		self.s0 = 0
		self.odd = 0
		self.center = int(Fs/f+0.5)
		self.V = self.center

		
	def _tick(self,phase):
		self.state = self.state + self.acc*self.V - self.Full
		return self.state+phase
		
	def _output(self):
		ret = []
		half = self.V/2
		for i in range(0,half):
			ret.append(1)
		if (self.V%2)!=0:
			if self.odd == 0:
				self.odd = 1
				ret.append(1)
			else:
				self.odd = 0
				ret.append(-1)
		for i in range(0,half):
			ret.append(-1)
		return ret
		
	def _judge(self,e):
		r = self.center
		if e<-self.Full/32:
			r = self.center+1
		if e>self.Full/32:
			r = self.center-1
		return r
		
	def center(self):
		return self.center
	
	def ce(self,phase):
		err = self._tick(phase)
		self.s0 = self.s0 + err
		self.V = self._judge(err+0*self.s0)
		return self._output()

import spectrum
import GMSKBB
		
def aTest(f,data):
	Fs = 6400e6
	W = 24
	apll = PLL(f,Fs,W)
	gmsk = GMSKBB.GMSKBB(16e6,f)
	aPxx = spectrum.spectrum(64000)
	while data:
		if gmsk.newD()==1:
			phase = gmsk.ce(data.pop(0))
		else:
			phase = gmsk.ce(0)
		o = apll.ce(phase<<6)
		for i in range(0,len(o)):
			aPxx.push(o[i])
	pxx = aPxx.out()
	return pxx
		
from pylab import *
import random
	
if __name__=='__main__':
	f = 340e6
	data = []
	for i in range(0,520):
		d = random.randint(0,1)
		data.append(d)
	pxx = aTest(f,data)
	plot(10./log(10.)*log(pxx))
	show()
					