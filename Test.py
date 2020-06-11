import scipy.io
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, scatter, imshow, colorbar
# Load the .mat file in
data = scipy.io.loadmat('bx_0.mat')
# Print to see what you are dealing with, as well as the the variable type
print(data)
print(type(data))
# The data is a dictionary so we use data.keys to find where the data is?
print(data.keys())
# Find the type of data that is being stored and how much of it there is
print(type(data['bx']), data['bx'].shape)
# Check what type each entry in the array is
print("Hello")
print(type(data['bx'][0][0]),data['bx'][0][0].shape)
# Make a color graph of the correct data in the file
# imshow(data['bx'],cmap= "jet")
print("wow")
print(data['bx'])
# colorbar()
# show()


