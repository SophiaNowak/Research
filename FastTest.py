import scipy.io
import os
import time
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar, savefig, close, pcolor, gca, axis, xlim, ylim


class MakeDataPlots():
    def __init__(self, folder_dir, file_list, folder_list, time_step, dim1, dim2):
        self.folder_dir = folder_dir
        self.file_list = file_list
        self.folder_list = folder_list
        self.time_step = time_step
        self.dim1 = dim1
        self.dim2 = dim2

    def get_data(self):

        # initialize a 3-D array, to the size of the data stored in each file
        # print(self.folder_dir, self.file_list, self.folder_list, self.time_step, self.dim1, self.dim2)
        data = np.zeros((len(file_list), dim1, dim2))

        # Get the correct address to the folder.
        dir = folder_dir + folder
        print(dir)
        # Counter for taking care of what variable we are working with
        counter = 0

        # Loop for finding the files.
        for item in file_list:
            current_dir = dir + '/' + item + '_' + str(time_step) + '.mat'
            print(current_dir)
            # Check if the file exists, if it does store the data at that file to to the data 3-D array.
            pList =['Pperp1e', 'Pperp2e', 'Ppare']
            if os.path.isfile(current_dir):
                if counter == 14:
                    raw_data = scipy.io.loadmat(current_dir)
                    print("FUCK HELLO?")
                    # print(type(rawData[item]))
                    # Store the data from mat lab
                    data[counter, :, :] = raw_data[pList[0]]
                elif counter == 15:
                    raw_data = scipy.io.loadmat(current_dir)
                    # print(type(rawData[item]))
                    # Store the data from mat lab
                    data[counter, :, :] = raw_data[pList[1]]
                elif counter == 16:
                    raw_data = scipy.io.loadmat(current_dir)
                    # print(type(rawData[item]))
                    # Store the data from mat lab
                    data[counter, :, :] = raw_data[pList[2]]
                else:
                    raw_data = scipy.io.loadmat(current_dir)
                    # print(type(rawData[item]))
                    # Store the data from mat lab
                    data[counter, :, :] = raw_data[item]

            counter = counter + 1

        temperature = (data[14] + data[15] + data[16]) / (data[12] * 3)
        self.plot(temperature, folder, time_step, "temperature", data)
        # self.plot(data[14], folder, time_step, " ", data)
        # self.plot(data[15], folder, time_step, " ", data)
        # self.plot(data[16], folder, time_step, " ", data)



    def findCenter(self, data):
        abs_data = np.absolute(data[3])
        xval_sum = np.sum(abs_data, 0)  # line of x vals,
        # print(abs_data.shape)
        # print(xval_sum.shape)
        x_pos_of_xline = np.argmin(xval_sum)  # first index
        zcut_of_xline = abs_data[:, x_pos_of_xline]
        z_pos_of_xline = np.argmin(zcut_of_xline)  # zeroth index

        return x_pos_of_xline, z_pos_of_xline

    def plot(self, plot_data, folder, time_step, plot_data_str, data):
        [xpos, zpos] = self.findCenter(data)
        print(xpos, zpos)
        # if 1800 >= xpos >= 1400:
        #     # xmin = xpos-200
        #     # xmax = xpos+200
        #     xlim(xpos-200, xpos+200)
        # else:
        #     # xmin = 1400
        #     # xmax = 1800
        #     xlim(1400, 1800)
        #
        # if 950 >= zpos >= 650:
        #     # zmin = zpos-150
        #     # zmax = zpos+200
        #     ylim(zpos-150, zpos+150)
        # else:
        #     # zmin = 650
        #     # zmax = 950
        #     ylim(650, 950)

        plot_data = plot_data[(zpos - 150):(zpos + 150), (xpos - 200):(xpos + 200)]
        # print(plot_data.shape)
        # print(np.min(plot_data))
        # print(np.max(plot_data))

        fig = imshow(plot_data, cmap = "inferno", extent = [(xpos-200),(xpos+200), (zpos-150), (zpos+150)],
                     origin = 'lower')
        title(plot_data_str + folder + '_' + str(time_step))
        colorbar()
        print('/media/sophianowak/My Passport/INSERT LOCATION HERE/' + plot_data_str + folder + '_' + str(time_step))
        # savefig('/media/sophianowak/My Passport/Python Graphs 4/' + plot_data_str + folder + '_' + str(time_step) + '.png')
        # close()
        show()


if __name__ == '__main__':
    start = time.time()
    # Change the file directory variable depending on where the data is currently stored.
    folder_dir = '/media/sophianowak/My Passport/AsymmetricScan400/'
    file_list = ['uix', 'uiy', 'uiz', 'bx', 'by', 'bz', 'ex', 'ey', 'ez', 'jx', 'jy', 'jz', 'ne', 'ni', 'P1', 'P2', 'Pp']
    folder_list = ['d10-gf0', 'd10-gf4', 'd10-gf8', 'd27-gf0', 'd27-gf4', 'd27-gf8','d200-gf0', 'd200-gf4', 'd200-gf8'] #'d10-gf0', 'd10.5-gf0', 'd11-gf0', 'd12-gf0',
    # Dimensions of the  in each file.
    dim1 = 1680
    dim2 = 3360
    # Choose your time step, and folder to plot
    time_step = 60
    folder = folder_list[1]
    S = MakeDataPlots(folder_dir, file_list, folder_list, time_step, dim1, dim2)
    S.get_data()


    end = time.time()
    print(end - start)  # In seconds.
