##  This is a plotting module for the plotting of data in Scicoder 2013.
#

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
def easy_hist(data,col_names):
    """ This is a function that will create plots for various types of data:
    
    Parameters
    ----------
    data: list of float arrays
    col_names: string list
    """
    length=size(data) #this determines the number of plots to be made
    plt.subplots_adjust(hspace=.4)
    plt.subplots_adjust(hspace=.4)

    for i in xrange(length):
        idx=131+i
        plt.subplot(idx)            
        plt.title(col_names[i])
        plt.hist(data[i])
#plt.savefig(sometitlethatwillbefilledinlater.png)
    plt.show()
