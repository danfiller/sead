# This is a module to convert the galactic longitude, galactic latitude and 
# heliocentric distance to Galactic coordinates.  

import numpy as np
import astropy.units as u

def easy_con(l,b,d):
    """This is a simple module that will convert to Galactic Coords:

    Parameters:
    l : the galactic longitude
    b : the galactic lattitude
    d : the heliocentric distance

    This assumes that you have passed this module the requested arrays correctly
    as such I will be assigning the arrays units.  I am going to give back 
    four items.  I will yield the galactic distance glc_dist, the x, y and 
    z coordinates in 
    """
    l=l*u.degree
    l=l+180*u.degree
    d=d*u.kpc
    b=b*u.deg
#
    b=b.to(u.radian).value
    l=l.to(u.radian).value

    x = d*np.sin(b)*np.cos(l)-8*u.kpc
    y = d*np.sin(b)*np.sin(l)
    z = d*np.cos(b)
    glc_dist=np.sqrt((x**2)+(y**2)+(z**2))
    return[glc_dist, x, y, z]
