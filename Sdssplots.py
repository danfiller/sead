##  This is a plotting module for the plotting of data in Scicoder 2013.
#

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
def easy_hist(data,col_names, split_value):
    """ This is a function that will create plots for various types of data:
    
    Parameters
    ----------
    data: list of float arrays
    col_names: string list
    """
    length=len(col_names) #this determines the number of plots to be made
    plt.subplots_adjust(hspace=1.1)
    plt.subplots_adjust(hspace=1.1)

    for i in xrange(length):
        idx=101+10*length+i
        plt.subplot(idx)            
        plt.title(col_names[i])
        plt.hist(data[i],log=True)
	
    plt.savefig('test.png')
    plt.show()
