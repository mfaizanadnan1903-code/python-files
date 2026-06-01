a =["Harry","Larry","Jerry","Carry","Marry"]
f = ":".join(a)
print(f)

#Use of map function
#map(function,list)
l = [1,2,3,4,5,6,7,8,9,10]
sq = lambda x:x*x
sl = map(sq,l)
sl = list(sl)
print(l)
print(sl)

#Use of filter function
def even(n):
    if(n%2==0):
        return True
    return False    
eve = filter(even,l)    
eve = list(eve)    
print(eve)


#Reduce example
from functools import reduce
def sum(a,b):
    return a+b
    
print(reduce(sum,l))   

#map function is used to return the exact value by function
#filter function is used to return the list value by function
#reduce function is used when to deal more than one arguments 

    