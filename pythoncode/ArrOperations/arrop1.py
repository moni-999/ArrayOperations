import numpy as np
arr= np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
reshaped_arr=arr.reshape(1, 9)
print("Original Array:")
print(arr)
print("Reshaped Array (1, 9):")
print(reshaped_arr)


