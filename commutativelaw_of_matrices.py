import numpy as np
A = np.array([[0+1j,0+2j],[1,0-1j]])
B = np.array([[0-1j,1],[0+2j,1]])
C = np.array([[0+2j,1],[0-1j,1]])
AB = np.dot(A,B)
BC = np.dot(B,C)
AB_C = np.dot(AB,C)
A_BC = np.dot(A,BC)
if AB_C[(0,0)] == A_BC[(0,0)] and AB_C[(0,1)] == A_BC[(0,1)] and AB_C[(1,0)] == A_BC[(1,0)] and AB_C[(1,1)] == A_BC[(1,1)]:
    print("L.H.S == R.H.S")
else:
    print("L.H.S != R.H.S")