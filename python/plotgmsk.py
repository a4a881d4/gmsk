import GMSK
from matplotlib.pylab import *

import random

import spectrum

tut = GMSK.GMSK(5e6,340e6,6400e6)
aPxx = spectrum.spectrum(64000)
	
data = []
for i in range(0,11520):
	d = random.randint(0,1)
	data.append(d)
while data:
	ret = tut.ce(data)
	for i in range(0,len(ret)):
		if ret[i]>0:
			aPxx.push(1)
		else:
			aPxx.push(-1)

pxx = aPxx.out()

plot(10./log(10.)*log(pxx))
show()
			
			