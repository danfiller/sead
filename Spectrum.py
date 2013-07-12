from __future__ import print_function, division
import json, urllib2
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

def coadd():
    choice1=raw_input("Would you like to look at globular clusters or Galaxies? \nPlease enter 'gc' for now. \n")
    if choice1 == 'gc':
        print("You have chosen globular clusters, way to go! \nThe available choice (for now is only m13, please type 'm13'. ")
        gc=raw_input('What cluster would you like to look at? \n')
        if gc=='m13':
            sdss_api_url='http://api.sdss3.org/spectrumQuery?ra=250.496720585d&dec=36.4623929501&radius=360'
            
    if choice1 == 'GAL':
        print("You have chosen to look at galaxies the choices are the Hercules cluster or some other one that I have not loaded yet. \n")
        url='http://api.sdss3.org/spectrumQuery?ra=241.302908975d&dec=17.7324625433&radius=360'
##########################################################################################################
##########################################################################################################

# well ok, what is going on is that we are going to get a list of stars to open from the sdss api by querying the databast around a given ra and dec 

#sdss_api_url='http://api.sdss3.org/spectrumQuery?ra=250.496720585d&dec=36.4623929501&radius=360'
    response=urllib2.urlopen(sdss_api_url)
    data_dict=json.load(response)

#Now we are going to pull spectra for the elements in the downloaded list
    spectra=[]
    for line in data_dict: #This has been truncated. 
        spectrum_url='http://api.sdss3.org/spectrum?id='+line+'&format=json'
        spectrum_file=urllib2.urlopen(spectrum_url)
        spectrum=json.load(spectrum_file)
        spectra.append(spectrum)
        print(spectrum.keys())
#here I am going to assign the first spectra to be reference spectra, upon which all else will be interpolated
#print('I made it through the for loop')
#print(spectra[0].keys())
#print(spectra[0].keys()[0])
    name1=spectra[0].keys()[0]

    ref_wave=spectra[0][name1]['wavelengths']
    ref_flux=spectra[0][name1]['flux']

#go through each and interpolate the following spectra onto the reference spectra. 
#for stars in spectrum[1:*]:
#temp_spectra=np.array([])
    temp_spectra=[]
    for star in spectra:
        tmp_spec_name=star.keys()[0]
        print(tmp_spec_name)
        tmp_flux=star[tmp_spec_name]['flux']
        tmp_wave=star[tmp_spec_name]['wavelengths']
        int_funct=interpolate.interp1d(tmp_wave,tmp_flux,bounds_error=False,fill_value=0.)
        int_wave=int_funct(ref_wave)
        print('I gathered flux and lambda for '+tmp_spec_name+'and then I interpolated onto wavelength '+name1)
        summed_waved=int_wave
        temp_spectra.append(int_wave)
            
    new_flux=sum(temp_spectra)/len(spectra)
    plt.plot(ref_wave,new_flux)
    plt.xlabel(r'Wavelength $\AA$')
    plt.ylabel('Intensity')


    plt.show()



