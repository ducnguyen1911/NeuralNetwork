__author__ = 'duc07'



__author__ = 'duc07'

# from pandas import read_csv
# import matplotlib.pyplot as plt
#
# df = read_csv('data.data', sep=' ')
# x = df.x
# y = df.y
# colors = ['r' if item > 0 else 'b' for item in df.Name]
#
# plt.scatter(x, y, s=35, c=colors, marker='o')
# plt.show()

#====================================================
# problem 5

#====================================================
# problem 7
# import numpy as np
# import matplotlib.pyplot as plt
#
# threshold = 0.001
# eta = 0.01
#
#
# def calc_err(w):
#     return (w - 2) * (w - 2.05) * (w - 4) * (w - 7)
#
#
# def update_w(w):
#     return w - eta * (4 * w ** 3 - 45.15 * w ** 2 + 153.3 * w - 158.5)
#
#
# def gradient_descent(w):
#     x = w
#     pre_E = 99999999
#     cur_E = calc_err(x)
#     iter = 0
#     plt.vlines(w, -50, cur_E, colors='b', linestyles='solid', label='w0')
#     while abs(cur_E - pre_E) >= threshold:
#         plt.plot([x], [cur_E], 'rx')
#         iter += 1
#         x = update_w(x)
#         pre_E = cur_E
#         cur_E = calc_err(x)
#     print 'With w = ', w, ' - Number of iterations needed: ', iter
#
#
# def run(w0):
#     x = np.arange(0.9, 7.1, 0.1)
#     y = [calc_err(item) for item in x]
#     plt.plot(x, y)
#     gradient_descent(w0)
#     plt.show()
#
# run(1)
# run(3)
# run(4)
# run(7)

#====================================================
# problem 8
# import numpy as np
# import matplotlib.pyplot as plt
#
# threshold = 0.001
# eta = 0.01
#
#
# def calc_err(w):
#     return (w - 2) * (w - 2.05) * (w - 4) * (w - 7)
#
#
# def calc_delta(w):
#     return - eta * (4 * w ** 3 - 45.15 * w ** 2 + 153.3 * w - 158.5)
#
#
# def gradient_descent(w, alpha):
#     x = w
#     pre_E = 99999999
#     cur_E = calc_err(x)
#     pre_delta = 0
#     iter = 0
#     plt.vlines(w, -50, cur_E, colors='b', linestyles='solid', label='w0')
#     while abs(cur_E - pre_E) >= threshold:
#         plt.plot([x], [cur_E], 'rx')
#         iter += 1
#         cur_delta = calc_delta(x)
#         x = x + cur_delta + pre_delta * alpha
#         pre_delta = cur_delta
#         pre_E = cur_E
#         cur_E = calc_err(x)
#     print 'With w = ', w, ', alpha = ', alpha, ' - Number of iterations needed: ', iter
#
#
# def run(w0, alpha):
#     x = np.arange(-0.1, 7.1, 0.1)
#     y = [calc_err(item) for item in x]
#     plt.plot(x, y)
#     gradient_descent(w0, alpha)
#     plt.show()
#
# for rate in np.arange(0.9, 1.2, 0.1):
#     run(0, rate)
#
# for rate in np.arange(1, 1.2, 0.1):
#     run(3, rate)
#

#====================================================
# problem 10
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# X = np.arange(-10, 10, 0.25)
# Y = np.arange(-10, 10, 0.25)
# X, Y = np.meshgrid(X, Y)
#
# Z1 = X**2 + Y**2/4
# fig1 = plt.figure()
# ax1 = fig1.gca(projection='3d')
# surf1 = ax1.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap=cm.coolwarm,
#         linewidth=0, antialiased=False)
#
# Z2 = X**2 + Y**2
# fig2 = plt.figure()
# ax2 = fig2.gca(projection='3d')
# surf2 = ax2.plot_surface(X, Y, Z2, rstride=1, cstride=1, cmap=cm.coolwarm,
#         linewidth=0, antialiased=False)
#
# plt.show()


#====================================================
# problem 10.4
def grad_descent(w1, w2, eta, func):
    # delta_w1 = 0
    # delta_w2 = 0
    for i in range(1, 5):
        if func == 1:
            delta_w1 = - eta * (2 * w1)
            delta_w2 = - eta * (w2 / 2)
        else:
            delta_w1 = - eta * (2 * w1)
            delta_w2 = - eta * (2 * w2)
        w1 = w1 + delta_w1
        w2 = w2 + delta_w2
        print 'Loop ', i, ' : w1 = ', w1, ' , w2 = ', w2
    return 0


grad_descent(6, 6, 0.1, 1)
grad_descent(6, 6, 0.1, 2)
