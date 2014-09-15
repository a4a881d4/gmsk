import constants
import POSC
import OSC
import GMSKBB

class GMSK:
	def __init__(self,gmskR,carrierF,Fs):
		( Hf, Lf ) = divmod(carrierF,Fs/constants.HighOSCF)
		self.posc = POSC.POSC(Hf*Fs/constants.HighOSCF,Fs)
		self.osc = OSC.OSC(Lf,Fs/constants.OverSampleRate)
		self.bb = GMSKBB.GMSKBB(gmskR,Fs/constants.OverSampleRate)
		self.mask = constants.HighOSCF-1
		self.oscShift = constants.OSCWidth-constants.HighOSCWidth
		self.bbShift = constants.GMSKPW+2-constants.HighOSCWidth
		
	def ce(self,inD):
		d = 0
		if self.bb.newD()==1:
			d = inD.pop(0)
		phase = self.bb.ce(d)>>self.bbShift
		phase = phase + (self.osc.ce()>>self.oscShift)
		phase = phase & self.mask
		ret = self.posc.ce(phase)
		return ret
import spectrum
from pylab import *
import random
		
if __name__=='__main__':
	for f in range(15):
	
		tut = GMSK(16e6,4500e6+40e6/3.*f,12800e6)
	
		data = []
		aPxx = spectrum.spectrum(12800)
	
		for i in range(0,11520):
			d = random.randint(0,1)
			data.append(d)
		while data:
			ret = tut.ce(data)
			for i in range(0,len(ret)):
				aPxx.push(ret[i])
		print "*"
		pxx = aPxx.out()	
		plot(10./log(10.)*log(pxx))
	show()		
		