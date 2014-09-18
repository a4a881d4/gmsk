import pilot
import xcorr
import nrf24l01tx
import math

def sync(c,os):
	aX = xcorr.xcorr( os, pilot.pilot(1) )
	
	ret = []
	
	for i in range( os*60 ):
		ret.append( aX.ce(c[i]) )
		
	pos = ret.index(max(ret))
	return ( pos, ret )
	
def syncBeforeDemod(c,OS,h):
	p = pilot.pilot(1)
	W = 256
	aTx = nrf24l01tx.Tx(OS,256,h)
	p.append(0)
	p.append(1)
	ps = aTx.modu(p)
	ss = []
	for p in ps:
		s = complex(math.cos(2.*p*math.pi/(1<<8)),math.sin(2.*p*math.pi/(1<<8)))
		ss.append(s)
	pos = 0
	buf = [ complex(0.,0.) for i in range(len(ss)) ]
	ret = []
	for din in c:
		buf[pos]=din
		p = pos
		r = 0.
		for s in ss:
			r = r + buf[p]*s.conjugate()
			p = ( p + 1 ) % len(ss)
		ret.append(r)	
		pos = (pos+1)%len(ss)
	
	aret = []	
	for r in ret:
		aret.append( (r*r.conjugate()).real )
	
	pos = aret.index(max(aret))
	return ( pos, ret, aret )
		
	