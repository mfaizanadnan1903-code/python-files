import numpy as np
arr = np.array([7,8,9,5,6,7,2,3,4]).reshape(3,3)
art = arr.copy().transpose()
arting = art[1].copy()
art[0] = art[1] - art[0]
art[1] = art[2] - art[1]
art[2] = art[2] - arting
print(art)
for i in range(3):
    for j in range(3):
        print("hello",arr[i][j])