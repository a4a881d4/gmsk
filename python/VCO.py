import spectrum

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
		
	def center(self):
		return self.center
	
def aTest(f):
	Fs = 6400e6
	W = 24
	aVCO = VCO(f,Fs,W)
	V = aVCO.center
	
	s0 = 0
	s1 = 0
	aPxx = spectrum.spectrum(64000)
	for T in range(0,100000):
		state = aVCO.ce(V,0)
		s0 = s0 + state
		#s1 = s1 + s0
		V = aVCO.judge(state+s0*0.75+s1/8)
		#print "#",state,V
		o = aVCO.output(V)
		for i in range(0,len(o)):
			aPxx.push(o[i])
	pxx = aPxx.out()
	return pxx
		
from pylab import *
	
if __name__=='__main__':
	fs = [345e6,346e6,347e6,348e6,349e6]
	
	for f in range(20):
	    
	    pxx = aTest(f*1e6+340e6)
	    plot(10./log(10.)*log(pxx))
	show()
	    
					