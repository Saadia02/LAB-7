from astropy.io import fits

# Open a FITS file
hdulist = fits.open(r'D:\image processing\myenv\M51\M51\blue.fits')

# Access the data in the primary HDU (Header Data Unit)
data = hdulist[0].data
hdulist.close()  # Close the FITS file


header = hdulist[0].header

# Print the header information
print(header)