import random

def mod_exp(a,e,m):
     bi=[] #이진수 
     sum=1
     while e!=0:
        bi.append(e%2)
        e=int(e//2)
     t=a
     for i in bi:
         if i==1:
             sum=sum*t%m
         t=t**2%m
     return sum

def gcd(a,b):
    while(1):
        r=a%b
        a=b
        b=r
        if r==0:
            return a

def miller_rabin_test(n,b,s,t):
    res=mod_exp(b,t,n)
    if(res==1 or res==n-1):
         return 1
    for i in range(1,s):
         res=res**2%n
         if (res==n-1):
              return 1
         elif (res==1):
              return 0
    return 0  

def is_prime(n):
     k=n-1
     s=0
     while 1:
          if k%2==0:
               s=s+1
               k=k//2
          else:
               t=k
               break
     
     for i in range(0,20):
          while 1:
               b=random.randint(2,n-1)
               if gcd(n,b)==1:
                    break
          if miller_rabin_test(n,b,s,t)==0:
               return 0
     return 1
