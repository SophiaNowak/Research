import scipy.io
import os
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar

# Change the file directory variable depending on where the data is currently stored
folder_dir = '/media/sophianowak/My Passport/AsymmetricScan400/'
fileList = ['bx', 'by', 'bz', 'ex', 'ey', 'ez', 'jx', 'jy', 'jz', 'ne', 'ni', 'uix', 'uiy', 'uiz'] #, 'uix', 'uiy', 'uiz'
time = 0

# Get and store as a list the folders
folders_in_dir = []
for r in os.listdir(folder_dir):
    if 'gf' in r:
        folders_in_dir.append(r)
print(folders_in_dir)

# Loop through the folders, then the files in the folders by time interval
for folder in folders_in_dir:
    dir = folder_dir + folder
    print(dir)
    for file in os.listdir(folder_dir):
        for item in fileList:
            current_dir = dir + '/' + item + '_' + str(time) + '.mat'
            # If the file exists load it in, else break
            if os.path.isfile(current_dir):
                # Load the .mat file in
                data = scipy.io.loadmat(current_dir)
                # Print for debug
                print(item + '_' + str(time))
                # imshow(data[item], cmap="jet")
                #
                # title(item + '_' + str(time))
                # colorbar()
                # show()

            else:
                continue
        time = time + 1


        # if time != 101:
        #     time = time + 1
        # else:
        #     break
        # if os.path.isfile(current_dir):
        #     time = time + 1
        # else:
        #     break


