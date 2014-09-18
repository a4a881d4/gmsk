import pilot
import xcorr

def sync(c,os):
	aX = xcorr.xcorr( os, pilot.pilot(1) )
	
	ret = []
	
	for i in range( os*60 ):
		ret.append( aX.ce(c[i]) )
		
	pos = ret.index(max(ret))
	return ( pos, ret )
	
