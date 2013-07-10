import sdssplot, readfitstable, argparse_example

""" 
	Plots histogram of column requested from filename
	input
	=================
	filename: str
	col_list: list
"""

# Standard library
import sys
import math
from argparse import ArgumentParser
import logging


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
    parser.add_argument("-list", dest="col_list", required=True, type=list,
                        help="List of columns")

    args = parser.parse_args()


#read out the required columns
rtn_col_list = readfitstable(args.filename,args.col_list)

#Pass the columns to be plotted
sdssplot(rtn_col_list)
