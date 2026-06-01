print("Palindromic numbers")
for i in range(1,1000):
    i = str(i)
    g = i[::-1]
    if(i==g):
        print(i,end=" ")
print()        
print("Prime numbers")        
for i in range(2,1001):
    flag=1
    for j in range(2,i):
        if(i%j==0):
            flag=0
    if(flag==1):
        print(i,end=" ")