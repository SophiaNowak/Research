import scipy.io
import os
import time
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar, savefig, close, pcolor, gca, axis


class MakeDataPlots(object):
    def get_data(self):
        # Change the file directory variable depending on where the data is currently stored.
        folder_dir = '/media/sophianowak/My Passport/AsymmetricScan400/'
        file_list = ['uix', 'uiy', 'uiz', 'bx', 'by', 'bz', 'ex', 'ey', 'ez', 'jx', 'jy', 'jz', 'ne', 'ni']
        folder_list = ['d10-gf0']  # , 'd10.5-gf0', 'd11-gf0', 'd12-gf0', 'd74-gf4'
        time = 80

        for folder in folder_list:
            # initialize a 3-D array, to the size of the data stored in each file
            data = np.zeros((14, 1680, 3360))

            # Get the correct address to the folder.
            dir = folder_dir + folder
            print(dir)
            # Counter for taking care of what variable we are working with
            counter = 0

            # Loop for finding the files.
            # for time in range(0,102):
            for item in file_list:
                current_dir = dir + '/' + item + '_' + str(time) + '.mat'
                # Check if the file exists, if it does store the data at that file to to the data 3-D array.
                if os.path.isfile(current_dir):
                    raw_data = scipy.io.loadmat(current_dir)
                    # print(type(rawData[item]))
                    # Store the data from mat lab
                    data[counter, :, :] = raw_data[item]
                counter = counter + 1
            self.calculations(data, folder, time)

    def calculations(self, data, folder, time):
        # For each folder perform calculations.
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

        [T0, T1, T2, T3, sqrtW] = self.contractT(data, nix, niy, niz)
        denom = sqrtW * (data[13] ** 2 - nix ** 2 - niy ** 2 - niz ** 2) + (T0 * data[13] - T1 * nix - T2 * niy - T3 * niz)

        Us0 = (sqrtW * data[13] + T0) / denom
        Us1 = (sqrtW * nix + T1) / denom
        Us2 = (sqrtW * niy + T2) / denom
        Us3 = (sqrtW * niz + T3) / denom
        GAM = 1. / np.sqrt(Us0 ** 2 - Us1 ** 2 - Us2 ** 2 - Us3 ** 2)

        Us0 = nig * GAM * Us0
        Us1 = nig * GAM * Us1
        Us2 = nig * GAM * Us2
        Us3 = nig * GAM * Us3

        znormz = (data[13] * Fe0 - nix * Fe1 - niy * Fe2 - niz * Fe3) / neg
        onormz = (Us0 * Fe0 - Us1 * Fe1 - Us2 * Fe2 - Us3 * Fe3) / neg
        znormo = znormz * neg / nig
        onormo = onormz * neg / nig

        delta = .5 * ((data[3] ** 2 + data[4] ** 2 + data[5] ** 2) - (data[6] ** 2 + data[7] ** 2 + data[8] ** 2))
        pi =  (data[6] * data[3] + data[7] * data[4] + data[8] * data[5]) ** 2
        lambda_squared = -delta + np.sqrt(delta ** 2 + pi)

        self.plot(znormz, folder, time, "znormz ")
        self.plot(onormz, folder, time, "onormz ")
        self.plot(znormo, folder, time, "znormo ")
        self.plot(onormo, folder, time, "onormo ")
        self.plot(lambda_squared, folder, time, r'$\lambda^2$ ')

    def contractT(self, data, nix, niy, niz):
        Sx = data[7] * data[5] - data[8] * data[4]
        Sy = data[8] * data[3] - data[6] * data[5]
        Sz = data[6] * data[4] - data[7] * data[3]
        T00 = .5 * (data[6] ** 2 + data[7] ** 2 + data[8] ** 2) + .5 * (data[3] ** 2 + data[4] ** 2 + data[5] ** 2)
        edu = data[6] * nix + data[7] * niy + data[8] * niz
        bdu = data[3] * nix + data[4] * niy + data[5] * niz

        T0 = T00 * data[13] - (Sx * nix + Sy * niy + Sz * niz)
        T1 = Sx * data[13] - T00 * nix + data[6] * edu + data[3] * bdu
        T2 = Sy * data[13] - T00 * niy + data[7] * edu + data[4] * bdu
        T3 = Sz * data[13] - T00 * niz + data[8] * edu + data[5] * bdu

        sqrtW = np.sqrt(T00 ** 2 - Sx ** 2 - Sy ** 2 - Sz ** 2)
        return T0, T1, T2, T3, sqrtW

    def plot(self, plot_data, folder, time, plot_data_str):
        val = np.amax(plot_data)
        fig = imshow(plot_data, cmap="bwr", clim = (-val, val))
        title(plot_data_str + folder + '_' + str(time))
        colorbar()
        # savefig('/media/sophianowak/My Passport/Python Graphs/' + plot_data_str + folder + '_' + str(time) + '.png')
        # close()
        show()


if __name__ == '__main__':
    start = time.time()

    S = MakeDataPlots()
    S.get_data()

    end = time.time()
    print(end - start) # In seconds.
