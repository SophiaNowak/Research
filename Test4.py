import scipy.io
import os
import pandas as pd
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar, savefig, close

# Change the file directory variable depending on where the data is currently stored
folder_dir = '/media/sophianowak/My Passport/AsymmetricScan400/'
fileList = ['uix', 'uiy', 'uiz'] # 'bx', 'by', 'bz', 'ex', 'ey', 'ez', 'jx', 'jy', 'jz', 'ne', 'ni',
folderList = ['d10', 'd10.5', 'd11', 'd12', 'd14','d16', 'd20', 'd27', 'd74', 'd200']

# Get and store as a list the folders
# Play with only one file for testing purposes, search for specific folder
folders_in_dir = []
for r in os.listdir(folder_dir):
    for dnum in folderList:
        for gfnum in  range(0, 12, 2):
            folder_name = str(dnum) + '-gf' + str(gfnum)
            if folder_name in r:
                folders_in_dir.append(r)
print(folders_in_dir)
print(len(folders_in_dir))
time = 0

# Loop through the folders, then the files in the folders by time interval
# Loop for folders
for folder in folders_in_dir:
    dir = folder_dir + folder
    print(dir)
    # Loop for finding the files
    for time in range(0, 1):
        for item in fileList:
            current_dir = dir + '/' + item + '_' + str(time) + '.mat'
            if os.path.isfile(current_dir):
                data = scipy.io.loadmat(current_dir)
                # Print for debug
                print(item + '_' + str(time))
                fig = imshow(data[item], cmap="jet")
                title(item + '_' + str(time))
                colorbar()
                # savefig('/media/sophianowak/My Passport/Python Graphs/' + item + '_' + str(time) + '.png' )
                close()





