# this will read a fits table and return the columns
# that the user specifies
# Written by alex hagen (hagen@psu.edu) at scicoder 2013

from astropy.io import fits

def read_table(filenamepath,fields=['RV_ADOP'],extension_num=1,memmap=True,cleanup=(True,-9999)):
    """
    This will open the fits file located at filenamepath
    fields is a list containing the names of the columns
    that should be returned
    extension_num is the extension number for the fits table
    memmap sets the memmap setting for fits.open
    cleanup is a tuple that sets whether or not values need to be cleaned up
    the second value in the tuple is the value of bad columns this is set to the sdss default of
    -9999
    """
    
    hdulist = fits.open(filenamepath,memmap=memmap)
    cols = hdulist[extension_num].columns
    for i in fields:
        assert i in cols.names, "{0} is not a column name".format(i)
    
    print "Reading in the table data...Please be patient"
    tbdata = hdulist[extension_num].data #this is expensive
    output = []
    for i fields:
        output.append(tbdata.field(i))
    
    if cleanup[0]:
        

    return output
    
    
    
    
    
    
    
