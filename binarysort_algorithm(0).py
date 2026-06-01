l = [i for i in range(10,0,-1)]
def binarysort1(l):
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            c = l[i]
            l[i] = l[i+1]
            l[i+1] = c
    return l
    
def loop1(l):
    for i in range(len(l)-1):
        binarysort1(l)
    return l
    
print(loop1(l))

l = [i for i in range(1,11)]
def binarysort2(l):
    for i in range(len(l)-1):
        if(l[i]<l[i+1]):
            c = l[i]
            l[i] = l[i+1]
            l[i+1] = c
    return l

def loop2(l):
    for i in range(len(l)-1):
        binarysort2(l)
    return l
    
print(loop2(l))