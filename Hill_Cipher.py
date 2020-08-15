import numpy as np
import random
import math

def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) :
        q = a // m
        t = m
        m = a % m 
        a = t 
        t = y
        y = x - q * y 
        x = t
    if (x < 0) : 
        x = x + m0
    return x

def det(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])

def Adj(A,n):
    B=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            row=list(range(n))
            col=list(range(n))
            del row[i]
            del col[j]
            print(math.ceil(np.linalg.det(A[:,col][row,:])))
            B[i,j]=((-1)**(i+j))*int(det(A[:,col][row,:]))
    C=np.transpose(B)
    return C

Msg=input("Enter message: ")
X=np.array([(ord(x)-65) for x in Msg])
H=[x for x in Msg]
print("Plain text:",X)
N=len(Msg)
Key=np.array([[random.randint(0,26) for y in range(N)] for x in range(N)])
Key=np.array([[6,24,1],[13,16,10],[20,17,15]])
print()
print("Key:",Key)
Temp=np.matmul(Key,X)
C=Temp%26
print()
print("Cipher Text:",C)

Akey=Adj(Key,N)
det=int(np.linalg.det(Key))
Ikey=(Akey*modInverse(det,26))%26
print(Akey)
print(Ikey)