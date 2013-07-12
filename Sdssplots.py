##  This is a plotting module for the plotting of data in Scicoder 2013.
#

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import matplotlib

def easy_hist(data,col_names, split_value):
    """ This is a function that will create plots for various types of data:
    
    Parameters
    ----------
    data: list of float arrays
    col_names: string list
    """

    
    length=len(col_names) #this determines the number of plots to be made
    plt.subplots_adjust(hspace=10.)
    plt.subplots_adjust(hspace=10.)
    

    try:
	metin= col_names.index("FEH_ADOP")
    	metals=data[metin]
    	print split_value
        print "metals max:",str(np.max(metals))
        print "metals min:",str(np.min(metals))
	highmet=metals[metals > split_value]
    	lowmet=metals[metals <= split_value]        
    except:
	print 'oops, not plotting metallicity'

    font = {'size'   : 8}

    matplotlib.rc('font', **font)

    for i in xrange(length):
        idx=101+10*length+i
        plt.subplot(idx)            
        plt.title(col_names[i])
       	if i == metin:
           print "in metin if statement" 
	   plt.hist(highmet,log=True)
           print "lowmet length is:",len(lowmet), "size is", str(lowmet.size)
	   if len(lowmet) >= 1: 
              print "in lowmet if statement" 
	      plt.hist(lowmet,log=True,alpha=0.5,color="orchid")
	      print "Plotting the red one ..."
   	else:
		plt.hist(data[i],log=True)
	
    plt.savefig('test.png')
    plt.show()
