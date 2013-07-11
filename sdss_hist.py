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
    #parser.add_argument("-galactic", dest="gal_coords", required=False, type=bool,
    #                    help="if user wants to plot galactic coords")
    parser.add_argument("-galactic",  dest="gal_coords",action='store_true', default=False, required=False)
    parser.add_argument("-height",  dest="plot_height",action='store_true', default=False, required=False)
                        
    args = parser.parse_args()

    if args.gal_coords == True:
    	args.col_list.append("L")
	args.col_list.append("B")
	if "DIST_ADOP" in args.col_list:
		args.col_list.remove("DIST_ADOP") # if user specified DIST_ADOP we want to move this to be last in the list
		args.col_list.append("DIST_ADOP") #now DIST_ADOP will be the last array in list retrieved from file, i.e. rtn_col_list[-1]
	if "DIST_ADOP"  not in args.col_list:
		args.col_list.append("DIST_ADOP") #now DIST_ADOP will be the last array in list retrieved from file, i.e. rtn_col_list[-1]
	
    print "Reading  the following columns from file", args.col_list 
    
    #read out the required columns
    rtn_col_list = readfitstable.read_table(args.filename,fields=args.col_list)
    
    if args.gal_coords == True:
        g_distance, x_above, y_above, height_above_disc = dist_conv.easy_con(rtn_col_list[-3],rnt_col_list[-2],rtn_col_list[-1])
        rtn_col_list.remove(-2)  #remove "L" data
        rtn_col_list.remove(-3)  #remove "B" data
        args.col_list.remove("L")  #remove "L" data
        args.col_list.remove("B")  #remove "B" data
        args.col_list.remove("DIST_ADOP")  #remove "B" data
        rtn_col_list.append(g_dist)  #remove "B" data
        args.col_list.append("Galactic distance")  #remove "B" data
        if args.plot_height == True:
	    rtn_col_list.append(height_above_disc)  
            args.col_list.append("Height")  
        print " Will be plotting", args.col_list 

   

    #Pass the columns to be plotted
    Sdssplots.easy_hist(rtn_col_list, args.col_list)
