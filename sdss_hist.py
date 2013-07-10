import Sdssplots, readfitstable, argparse_example
# Standard library
import sys
import math
from argparse import ArgumentParser
import logging


""" 
	Plots histogram(s) of column(s) requested from filename
	================
	input parameters
	=================
	filename: str
	col_list: list
"""

if __name__ == "__main__":
    # create logger
    logger = logging.getLogger(__name__)
 # define a handler to write log messages to stdout
    sh = logging.StreamHandler(stream=sys.stdout)

    # define the format for the log messages, here: "level name: message"
    formatter = logging.Formatter("[%(levelname)s]: %(message)s")
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    # create a parser object for understanding command-line arguments
    parser = ArgumentParser(description="Describe the script")

    # add two boolean arguments: 'verbose' for dumping debug messages and
    #   highers, and 'quiet' for restricting to just error messages

    # add a required, integer argument
    parser.add_argument("-file", dest="filename", required=True, type=str,
                        help="File to be read")
    parser.add_argument("-list", dest="col_list", required=True, nargs="*",
                        help="List of columns")

    args = parser.parse_args()



#read out the required columns
rtn_col_list = readfitstable.read_table(args.filename,fields=args.col_list)

#Pass the columns to be plotted
Sdssplots.easy_hist(rtn_col_list, args.col_list)
