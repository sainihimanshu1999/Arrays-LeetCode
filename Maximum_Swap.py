'''
In this question a number is given and we an swap at most two digit as once, and if we find max number
than original we swap them
'''

#Basic or Brute Force Method

def swap1(self,num):
    A = list(str(num))
    ret = A[:]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            A[i],A[j] = A[j],A[i]
            if A>ans: ans = A[:]
            A[i],A[j] = A[j],A[i]

    return int(''.join(ret))


#Dictionary Method

def swap2(self,num):
    a = list(map(int,str(num)))
    dic = {x:i for i,x in enumerate(a)}

    for i,x in enumerate(a):
        for d in range(9,x,-1):
            if d in dic:
                if dic[d]>i:
                    a[i],a[dic[d]] = a[dic[d]],a[i]
                    return int(''.join(map(str,a)))


    return num