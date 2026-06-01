def fact(n=1):
    if(n<=0):
        return 1
    return n*fact(n-1)
def fact2(n=1):
    if(n<=0):
        return 1
    return n*fact2(n-2)
print("You can only enter 1 to",1558)
n = int(input("Enter a number:"))
if(n<=994):
    print(fact(n))
elif(n<=(994*2)):
    a =     fact2(n)
    b =     fact2(n-1)
    print(a*b) 