import scipy.io
import os
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar, savefig, close, pcolor, gca, axis

# Change the file directory variable depending on where the data is currently stored.
folder_dir = '/media/sophianowak/My Passport/AsymmetricScan400/'
fileList = ['uix', 'uiy', 'uiz', 'bx', 'by', 'bz', 'ex', 'ey', 'ez', 'jx', 'jy', 'jz', 'ne', 'ni']
folderList = ['d10-gf0'] # , 'd10.5-gf0', 'd11-gf0', 'd12-gf0', 'd74-gf4'
folders_in_dir = []
time = 62

for folder in folderList:
    # intitalize a 3-D array
    x = np.zeros((1680, 3360, 13))  # Make a 10 by 20 by 30 array


    # Get the correct address to the folder.
    dir = folder_dir + folder
    print(dir)
    # Create empty list to later store data from each folder in.
    data = []
    # Loop for finding the files.
    # for time in range(0,102,1):
    for item in fileList:
        current_dir = dir + '/' + item + '_' + str(time) + '.mat'
        # print(current_dir)
        # print(time)
        # Check if the file exists, if it does append the data at that file to the data list.
        if os.path.isfile(current_dir):
            rawData = scipy.io.loadmat(current_dir)
            print(type(rawData[item]))
            data.append(rawData[item])


    # For each folder perform calculations.
    nix = data[13] * data[0]
    niy = data[13] * data[1]
    niz = data[13] * data[2]
    nig = data[13] * np.sqrt(1 - data[0] ** 2 - data[1] ** 2 - data[2] ** 2)
    nex = nix - data[9]
    ney = niy - data[10]
    nez = niz - data[11]
    neg = np.sqrt(data[12] ** 2 - nex ** 2 - ney ** 2 - nez ** 2)

    Fe0 = nex * data[6] + ney * data[7] + nez * data[8]
    Fe1 = data[12] * data[6] + ney * data[5] - nez * data[4]
    Fe2 = data[12] * data[7] - nex * data[5] + nez * data[3]
    Fe3 = data[12] * data[8] + nex * data[4] - ney * data[3]

    znormz = (data[13] * Fe0 - nix * Fe1 - niy * Fe2 - niz * Fe3) / neg
    znormo = znormz * neg / nig;

    # Plotting z normal z and z normal o
    fig = pcolor(znormz, cmap="bwr")
    title("znormz " + folder + '_' + str(time))
    colorbar()
    # savefig('/media/sophianowak/My Passport/Python Graphs/' + item + '_' + str(time) + '.png')
    # close()
    show()

    fig2 = pcolor(znormo, cmap="bwr")
    title("znormo " + folder + '_' + str(time))
    colorbar()
    # savefig('/media/sophianowak/My Passport/Python Graphs/' + item + '_' + str(time) + '.png')
    # close()
    show()




