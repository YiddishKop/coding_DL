import itertools

import matplotlib.pyplot as plt
import numpy as np

# dataset
x_data = [338., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]

# contour prepare
w_arr = np.arange(-200, -100, 1)
b_arr = np.arange(-200, -100, 1)
err_grid_value = np.zeros((len(w_arr), len(b_arr)))
contour_W, contour_B = np.meshgrid(w_arr, b_arr)

# err_grid_value compute
for (index_w, index_b) in itertools.product(
        range(len(w_arr)), range(len(b_arr))):
    for i in range(len(x_data)):
        err_grid_value[index_w][index_b] += (
            x_data[i] * w_arr[index_w] + b_arr[index_b] - y_data[i])**2

print(err_grid_value.shape)
print(contour_B.shape)
print(contour_W.shape)

# contour plotting
# plt.contourf(
#     contour_W, contour_B, err_grid_value, 50, cmap=plt.get_cmap('jet'))
# plt.xlim(-10, -20)
# plt.ylim(-100, -200)
