import numpy as np
import matplotlib.pyplot as plt


def getting_data_to_tuple(name_of_file):
    X = []
    Y = []
    with open(name_of_file, 'r') as fin:
        for line in fin.readlines():
            lin = line.replace(',', '.')
            lin = lin.replace('\n', '')
            _, x, y = lin.split(';')
            X.append(float(x))
            Y.append(float(y))
    return X, Y


def getting_polynomial_regression_coefficients(X, Y):
    return np.polyfit(X, Y, 17)


def creating_linspace_over_X(X):
    return np.linspace(min(X), max(X), 10000)


def plotter(XY, nameoffig):
    X = XY[:][0]
    Y = XY[:][1]
    c = getting_polynomial_regression_coefficients(X, Y) #coefficient tuple
    x = creating_linspace_over_X(X)
    plt.plot(x, np.polyval(c, x))
    c_bandwith = c
    c_bandwith[-1] = c_bandwith[-1] - max(Y) / np.sqrt(2)
    roots = np.roots(c_bandwith)
    rootsreal = [root for root in roots if np.iscomplex(root) == False and root < max(X) and root > min(X)]
    bandwith = abs(rootsreal[1] - rootsreal[0])
    print("Bandswidth is {0} kHz".format(bandwith.round(2)))
    plt.xlabel("Frequency [$kHz$]")
    plt.ylabel("Current [$mA$]")
    plt.tight_layout()
    plt.savefig(nameoffig)
    plt.clf()
    resonancefrequency = X[Y.index(max(Y))]
    print("The resonance frequency is {0} kHz".format(resonancefrequency))
    qobtainedwith5thequation = resonancefrequency / bandwith
    print("Q factor obtained with equation 5 is {0}".format(qobtainedwith5thequation.round(2)))


plotter(getting_data_to_tuple("E-06,1.csv"), "plot1")
plotter(getting_data_to_tuple("E-06,2.csv"), "plot2")
plotter(getting_data_to_tuple("E-06,3.csv"), "plot3")
plotter(getting_data_to_tuple("E-06,4.csv"), "plot4")