import pilot
import xcorr

def sync(c):
	aX = xcorr.xcorr( 32, pilot.pilot(1) )
	
	ret = []
	
	for i in range( 32*60 ):
		ret.append( aX.ce(c[i]) )
		
	pos = ret.index(max(ret))
	return pos
	
