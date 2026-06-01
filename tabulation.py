import pandas as pd
import numpy as np
n = int(input("Enter the no. of observations:"))
lower = np.array([float(input(f"Enter {i+1} lower class limit:")) for i in range(n)])
upper = np.array([float(input(f"Enter {i+1} upper class limit:")) for i in range(n)])
x = np.array([float(input(f"Enter {i+1} observation:")) for i in range(n)])
freq = np.array([int(input(f"Enter {i+1} frequency:")) for i in range(n)])
b = ["---" for i in range(n)]
data = {
    "lower class limit" : lower,
    " ": b,
    "upper class limit" : upper,
    "X" : x,
    "Frequency" : freq
}

df = pd.DataFrame(data)
df.to_csv("Tabulation.csv",index=False)