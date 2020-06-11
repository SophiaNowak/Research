import scipy.io
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, scatter, imshow, colorbar
import os

# TODO: figure out if it is loading everything it needs to in, and check how to get it to only care about the data files.
#  Be more specific in the directory?

class GraphData:
    def get_first_two(string):
        return string[:2]

    def get_filenames(self, filepath):
        filepath = filepath.strip()
        # Split the filepath by '/', storing each element in a list
        filepath_list = filepath.split('/')
        # Get the filepath as a list and print it
        print(filepath_list)
        # Return the last element in the list
        return filepath_list[-1]


    def walk_filepath(self):
        rootdir = '/media/sophianowak/My Passport/AsymmetricScan400' # Write in the directory needed? Or have it as an input
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                # Get all of the directory addresses (how do I say that???)
                dirString = os.path.join(subdir, file)
                # From the directory string, get the file name
                file = self.get_filenames(dirString)
                # Load in the file
                data = scipy.io.loadmat(file)
                # Print to see what you are dealing with, as well as the the variable type
                print(data)
                print(type(data))
                # The data is a dictionary so we use data.keys to find where the data is?
                print(data.keys())
                # Find the type of data that is being stored and how much of it there is
                print(type(data[self.get_first_two()]), data[self.get_first_two()].shape)
                # Check what type each entry in the array is
                print(type(data[self.get_first_two()][0][0]), data[self.get_first_two()][0][0].shape)
                # Make a color graph of the correct data in the file
                imshow(data[self.get_first_two()], cmap="jet")

                colorbar()
                show()

if __name__ == '__main__':
    f = GraphData()
    f.walk_filepath()
