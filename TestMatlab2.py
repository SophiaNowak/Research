import scipy.io
import os
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar, savefig, close, pcolor, gca, axis


class StoreData(object):
    def getData(self):
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
            self.calculations(data, folder, time)

    def calculations(self, data, folder, time):
        # For each folder perform calculations.  np.multiply(a, b)
        # print((data[13]).shape)
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
        znormo = znormz * neg / nig

        [T0, T1, T2, T3, sqrtW] = self.contractT(data);
        denom = sqrtW * (ni ** 2 - nix ** 2 - niy ** 2 - niz ** 2) + ...
        (T0 * ni - T1 * nix - T2 * niy - T3 * niz);

        self.plot(znormz, folder, time)
        self.plot(znormo, folder, time)

    def contractT(self, data):
        Sx = data[7] * data[5] - data[8] * data[4]
        Sy = data[8] * data[3] - data[6] * data[5]
        Sz = data[6] * data[4] - data[7] * data[3]
        T00 = .5 * (data[6] ** 2 + data[7] ** 2 + data[8] ** 2) + .5 * (data[3] ** 2 + data[4] ** 2 + data[5] ** 2)
        edu = data[6] * data[0] + data[7] * data[1] + data[8] * data[2]
        bdu = data[3] * data[0] + data[4] * data[1] + data[5] * data[2]

        T0 = T00 * u0 - (Sx * data[0] + Sy * data[1] + Sz * data[2])
        T1 = Sx * u0 - T00 * data[0] + data[6] * edu + data[3] * bdu
        T2 = Sy * u0 - T00 * data[1] + data[7] * edu + data[4] * bdu
        T3 = Sz * u0 - T00 * data[2] + data[8] * edu + data[5] * bdu

        sqrtW = np.sqrt(T00 ** 2 - Sx ** 2 - Sy ** 2 - Sz ** 2);

    def plot(self, toPlot, folder, time):
        # Plotting z normal z and z normal o
        fig = imshow(toPlot, cmap="bwr")
        title(" " + folder + '_' + str(time))
        colorbar()
        # savefig('/media/sophianowak/My Passport/Python Graphs/' + item + '_' + str(time) + '.png')
        # close()
        show()

    # delta = .5 * ((data[3] ** 2 + data[4] ** 2 + data[5] ** 2) - (data[6] ** 2 + data[7] ** 2 + data[8] ** 2))
    # pi =  (data[6] * data[3] + data[7] * data[4] + data[8] * data[5]) ** 2
    # lambda_squared = -nabla + np.sqrt(nabla ** 2 + pi ** 2)

    # # Ploting lambda squared
    # fig3 = pcolor(lambda_squared, cmap = "bwr")
    # title(r'$\lambda^2$' + folder + '_' + str(time))
    # colorbar()
    # # savefig('/media/sophianowak/My Passport/Python Graphs/' + item + '_' + str(time) + '.png')
    # # close()
    # show()



if __name__ == '__main__':
    S = StoreData()
    S.getData()
