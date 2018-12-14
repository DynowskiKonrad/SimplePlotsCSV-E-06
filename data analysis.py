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
    return np.polyfit(X, Y, 10)


def creating_linspace_over_X(X):
    return np.linspace(min(X), max(X), 10000)


def plotter(XY, nameoffig):
    X = XY[:][0]
    Y = XY[:][1]
    c = getting_polynomial_regression_coefficients(X, Y) #coefficient tuple
    x = creating_linspace_over_X(X)
    plt.plot(x, c[0]*x**10 + c[1]*x**9 + c[2] * x**8 + c[3] * x**7 + c[4] * x ** 6 + c[5] * x ** 5 +
             c[6] * x ** 4 + c[7] * x ** 3 + c[8] * x ** 2 + c[9] * x + c[10])
    plt.xlabel("Frequency [$kHz$]")
    plt.ylabel("Current [$mA$]")
    plt.tight_layout()
    plt.savefig(nameoffig)
    plt.clf()



plotter(getting_data_to_tuple("E-06,1.csv"), "plot1")
plotter(getting_data_to_tuple("E-06,2.csv"), "plot2")
plotter(getting_data_to_tuple("E-06,3.csv"), "plot3")
plotter(getting_data_to_tuple("E-06,4.csv"), "plot4")