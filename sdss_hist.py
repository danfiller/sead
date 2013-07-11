import Sdssplots, readfitstable, argparse_example
import dist_conv
# Standard library
import sys
import math
from argparse import ArgumentParser
#import logging


""" 
	Plots histogram(s) of column(s) requested from filename
	================
	input parameters
	=================
	filename: complete file path
	col_list: columns not separated by commmas
	flag: -galactic if galactic coords needed
	flag: -height is plotted
"""

if __name__ == "__main__":
    # create logger
 #   logger = logging.getLogger(__name__)
 # define a handler to write log messages to stdout
 #   sh = logging.StreamHandler(stream=sys.stdout)

    # define the format for the log messages, here: "level name: message"
  #  formatter = logging.Formatter("[%(levelname)s]: %(message)s")
   # sh.setFormatter(formatter)
   # logger.addHandler(sh)

    # create a parser object for understanding command-line arguments
    parser = ArgumentParser(description="Describe the script")

    # add two boolean arguments: 'verbose' for dumping debug messages and
    #   highers, and 'quiet' for restricting to just error messages

    # add a required, integer argument
    parser.add_argument("-file", dest="filename", required=True, type=str,
                        help="File to be read")
    parser.add_argument("-cols", dest="col_list", required=True, nargs="*",
                        help="List of columns")
    parser.add_argument("-galactic",  dest="gal_coords",action='store_true', default=False, required=False)
    parser.add_argument("-height",  dest="plot_height",action='store_true', default=False, required=False)
    parser.add_argument("-split_Fe",  dest="split",type=float, required=False)
                        
    args = parser.parse_args()

    if args.gal_coords == True:
    	args.col_list.append("L")
	args.col_list.append("B")
	if "DIST_ADOP" in args.col_list:
		args.col_list.remove("DIST_ADOP") # if user specified DIST_ADOP we want to move this to be last in the list
		args.col_list.append("DIST_ADOP") #now DIST_ADOP will be the last i.e. rtn_col_list[-1]
	if "DIST_ADOP"  not in args.col_list:
		args.col_list.append("DIST_ADOP")
	
    print "Reading the following columns from file:", args.col_list 
    
    #read out the required columns
    rtn_col_list = readfitstable.read_table(args.filename,fields=args.col_list)
    
    if args.gal_coords == True:
        g_distance, x_above, y_above, height_above_disc = dist_conv.easy_con(rtn_col_list[-3],rtn_col_list[-2],rtn_col_list[-1])
        #Edit the list of arrays passed to plot fn
        rtn_col_list.pop(-2)  #remove "B" data
        rtn_col_list.pop(-3)  #remove "L" data
        rtn_col_list.pop(-1)  #remove "DIST_ADOP" data
        rtn_col_list.append(g_distance)  
        #Edit the list of columns
        args.col_list.remove("L")  
        args.col_list.remove("B")  
        args.col_list.remove("DIST_ADOP")  
        args.col_list.append("Galactic distance")
        #plot hight above disc
        if args.plot_height == True:
	    rtn_col_list.append(height_above_disc)  
            args.col_list.append("Height")  
        print " Plotting:", args.col_list 

   

    #Pass the columns to be plotted
    Sdssplots.easy_hist(rtn_col_list, args.col_list, args.split = [-999.])
