from functools import reduce
max = lambda a,b : a if(a>b) else b
arr = [10,6,7,8,54,56,3,5,7,8,6,98,32,42]
print("Maximum no. in array:",reduce(max,arr))
min = lambda a,b : a if(a<b) else b
print("Minimum no. in array:",reduce(min,arr))