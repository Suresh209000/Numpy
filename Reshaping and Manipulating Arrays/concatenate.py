import numpy as np
arr1 = np.array([14,15])
arr2 = np.array([13,12])
con_arr = np.concatenate((arr1,arr2),axis=0)
print(con_arr)