import scipy.io
import os
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar, savefig, close, pcolor, gca, axis

# Change the file directory variable depending on where the data is currently stored.
folder_dir = '/media/sophianowak/My Passport/AsymmetricScan400/'
fileList = ['uix', 'uiy', 'uiz', 'bx', 'by', 'bz', 'ex', 'ey', 'ez', 'jx', 'jy', 'jz', 'ne', 'ni']
folderList = ['d10-gf0']  # , 'd10.5-gf0', 'd11-gf0', 'd12-gf0', 'd74-gf4'
folders_in_dir = []
time = 62

for folder in folderList:
    # initialize a 3-D array, to the size of the data stored in each file
    data = np.zeros((14, 1680, 3360))

    # Get the correct address to the folder.
    dir = folder_dir + folder
    print(dir)
    # Counter for taking care of what variable we are working with
    counter = 0

    # Loop for finding the files.
    # for time in range(0,102,1):
    for item in fileList:
        current_dir = dir + '/' + item + '_' + str(time) + '.mat'
        # print(current_dir)
        # print(time)
        # Check if the file exists, if it does store the data at that file to to the data 3-D array.
        if os.path.isfile(current_dir):
            rawData = scipy.io.loadmat(current_dir)
            # print(type(rawData[item]))
            # Store the data from mat lab
            data[counter, :, :] = rawData[item]
        counter = counter + 1

    # For each folder perform calculations.  np.multiply(a, b)
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

    nabla = (data[3] ** 2 + data[4] ** 2 + data[5] ** 2) - (data[6] ** 2 + data[7] ** 2 + data[8] ** 2)
    pi =  (data[6] * data[3] + data[7] * data[4] + data[8] * data[5]) ** 2
    lambda_squared = -nabla + np.sqrt(nabla ** 2 + pi ** 2)

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

    # Ploting lambda squared
    fig3 = pcolor(lambda_squared, cmap = "bwr")
    title("lambda_squared" + folder + '_' + str(time))
    colorbar()
    # savefig('/media/sophianowak/My Passport/Python Graphs/' + item + '_' + str(time) + '.png')
    # close()
    show()






