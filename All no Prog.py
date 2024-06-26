def prime(num,count=0):
    for fa in range(1,num+1):
        if num%fa==0:
            count+=1
    return count==2

def composite(num,count=0):
    for fa in range(1,num+1):
        if num%fa==0:
            count+=1
    return count>2

def perfect(num,count=0,dsum=0):
    for fa in range(1,num):
        if num%fa==0:
            dsum+=fa
    return dsum==num

def palindrome(num,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return num==rev

def spy(num,dsum=0,dprod=0):
    while num!=0:
        rem=num%10
        dsum+=rem
        dprod*=rem
        num//=10
    return dsum==dprod

def niven(num,dsum=0):
    while(num!=0):
        rem=num%10
        dsum+=rem
        num//=10
    return num/dsum==0

def neon(num,dsum=0):
    copy=num
    squ=num**2
    while squ!=0:
        rem=squ%10
        dsum+=rem
        squ//=10
    return dsum==copy

def chronic(num,n=0):
    while n*(n+1)<=num:
        if n*(n+1)==num:
            return True
        else:
            n+=1
    else:
        return False
    
def sunny(num,n=0):
    while(n**2<=num+1):
        if n**2==num+1:
            return True
        else:
            n+=1
    else:
        return False
    
def armstrong(num,dsum=0):
    copy=num
    p=len(str(num))
    while num!=0:
        rem=num%10
        dsum+=rem**p
        num//=10
    return copy==dsum

def disarium(num,dsum=0):
    copy=num
    p=len(str(num))
    while num!=0:
        rem=num%10
        dsum+=rem**p
        num//=10
        p-=1
    return copy==dsum

def factorial(num,fact=1):
    for num in range(num,0,-1):
        fact*=num
    return fact

def Strong(num,dsum=0):
    copy=num
    rem=num%10
    dsum+=factorial(rem)
    num//10
    return dsum==copy

def evil(num,dsum=0):
    while num!=0:
        rem=num%2
        dsum+=rem
        num//=2
    return dsum%2==0

def BinToDec(num,dsum=0):
    p=0
    while num!=0:
        rem=num%10
        dsum+=rem*(2**p)
        num//=10
        p+=1
    return dsum

def AutoMorphic(num):
    sq=num**2
    p=len(str(num))
    if sq%(10**p)==num:
        print("Automorphic")
    else:
        print("Not")
    

def Trimorphic(num):
    cub=num**3
    p=len(str(num))
    if cub%(10**p)==num:
        print("Trimorphic")
    else:
        print("not")
print(__name__)



        
    







              

        
    

    





    
