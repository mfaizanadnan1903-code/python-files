n = len([1,2,3,4,5])
if(n>3):
    print("List is too long")
    
#Is equal to this (Walrus operator)   
if(n:=len([1,2,3,4,5])>3):
    print("list is too long")  
    
#To clarify variable type and (Type definitions)
#make sure the methods should be shown    
a : int = 56
n : str = "Hello"
def fun(a:int,b:str):
    return f"{a}+{b}"
print(fun(a,n))    

#Advanced typing hints
from typing import List,Dict,Tuple,Union
l : List[int] = [1,2*3,4,5]
print(l)
b : Dict[str,int] ={
    "Hello":1
}
print(b)
d : Tuple[str] = ("Hello",1)
print(d)
#Union means any can be it is either int or str
ident : Union[str,int] = "Hell123"
print(ident)


"""
Exception handling:
finally block always executes even if
it is in the function.
else block executes if try block runs
successfully
We can also raise custom exceptions:
if(n==0):
    raise ZeroDivisionError("Hey")
else:
    print()    
"""
'''
def myfun(n):
    return n
print(__name__)    #output:__main__
if __name__ == "__main__":
    ------
'''  
#global keyword work 
s  = 89
def fun():
    global s
    s = 5
    print(s)
fun()
print(s)


#enumerate keyword work
l = [1,2,3,4,5]
j = 0
for i in l:
    print(f"The item{i} is at index{j}")
    j+=1
#above code is equal to
for j,i in enumerate(l):
        print(f"The item{i} is at index{j}")
 
#list comprehension
l = [1,2,3,4,5,6,7,8,9,10]    
sl = []    
for i in l:
    sl.append(i*i)
print(sl)    
#Is equal to
s2 = [i*i for i in l]
print(s2)
        
        
        