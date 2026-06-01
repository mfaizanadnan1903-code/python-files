fact1 = lambda n: 1 if(n==0) else n*fact1(n-1)
fact = lambda n: 1 if(n<=0) else n*fact(n-2)
print("You can only enter 1 to",1558)
n = int(input("Enter a number:"))
if(n<=994):
    print(fact1(n))
elif(n<=1558):
    a = fact(n)
    b = fact(n-1)
    print(a*b) 