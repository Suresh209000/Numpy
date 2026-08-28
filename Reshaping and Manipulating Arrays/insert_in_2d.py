import numpy as np
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)

new_2d = np.insert(arr_2d,1,[4,5],axis=0)
print(new_2d)  