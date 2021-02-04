********************** FIND THE FIRST SET BIT FROM THE RIGHT ******************************

INT_SIZE = 32

pos = Right_most_setbit(num)

def Right_most_setbit(num):
    
    for i in range(INT_SIZE):
        if not (num & (1 << i)):
            pos+=1
            
        else:
            break
            
    return pos 
    
    
******************** POSITION OF THE RIGHTMOST DIFFERENT BIT BETWEEN 2 NUMBERS *************************
import math

def posofRightMostDiffBit(m,n):
    return getRightMostSetBit(m^n)
    
def getRightMostSetBit(n):
    return math.log2(n & -n)+1

m = 52, n = 4

print("position="int(posofRightMostDiffBit(m,n)))



********************* CHECK IF THE KTH BIT IS SET OR NOT ******************************

def isKthBitSet(n,k):
    
    if n & (1 << (k-1)):
        print ("SET")
        
    else:
        print ("NOT SET")
        

******************** HOW TO SET THE KTH BIT IN A NUMBER ***********************************

def setKthBit(n,k):

    return ((1 << k) | n)


******************** TOGGLE BITS IN A GIVEN RANGE *************************************

# 1 <=l <=r <= No. of bits of n

def toggleBitsfromLtoR(n,l,r):

    num = (((1 << r) - 1) ^ ((1 << (l -1)) - 1))
    
    return (n ^ num)


******************** COUNT NUMBER OF BITS TO BE FLIPPED TO CONVERT A TO B*****************************

def FlippedCount(a,b):
    return countSetBits(a ^ b)
    

def countSetBits(n):
    count = 0
    while n:
        count+=1
        n&=(n-1)
    
    return count
    
******************** LENGTH OF CONSECUTIVE 1'S IN A BINARY REPRESENTATION **************************

def maxConsecutive(x):
    count = 0
    
    while x!=0:
        x = (x & (x << 1))
        count = count +1
        
    return count
    
    
******************** SWAP ALL ODD AND EVEN BITS **********************************

def swapBits(x):
    
    #Get all even bits of x
    even_bits = x & 0xAAAAAAAA
    
    #Get all odd bits of x 
    odd_bits = x & 0x55555555
    
    #Right shift even bits
    even_bits >>=1 
    
    #Left shift odd bits
    odd_bits <<=1
    
    return (even_bits | odd_bits)

x = 23
print(swapBits(x))
    

******************* ROTATE BITS OF A NUMBER (d is the number of bits by which it will be rotated) ***************************************
INT_BITS = 32

def leftRotate(n,d):
    
    return (n << d) | (n >> (INT_BITS - d))
    
def rightRotate(n,d):

    return (n >> d) | (n << (INT_BITS - d))


n = 16
d = 2
print(leftRotate(n,d))

print(rightRotate(n,d))

******************* COUNT SET BITS IN A NUMBER *******************************************

def countSetBits(n):

    count = 0
    
    while n:
        count+= n & 1
        n >>=1

    return count 
    
i = 9
print(countSetBits(i))


****************** REVERSE BITS OF A NUMBER ************************************************

def reverseBits(num,bitsize):

    binary = bin(num)[2:]
    
    reverse = binary[-1:1:-1]
    
    reverse = reverse + (bitsize - len(reverse)) * '0'

    #Convert reverse binary string into integer
    print int(reverse,2)

num = 1
bitsize = 32
reverseBits(num,bitsize)

****************** HAMMING DISTANCE BETWEEN TWO NUMBERS *********************************

# Hamming Distance is the number of bits which are different at the same position in the two numbers

def hammingDist(n1,n2):

    x = n1 & n2
    setBits = 0
    
    while (x>0):
        setBits+= x & 1
        x >>=1
        
    return setBits

if __name__ == '__main__':
    
    n1 = 9
    n2 = 14
    
    print(hammingDist(9,14))  

****************** GIVEN A NUMBER, COUNT NUMBER OF ONES AND RETURN THEM AS AN ARRAY ***************

def countOnes(num):
    
    count = 0
    
    while num:
        count+=1
        num&=(n-1)
        return count
    
ans = []
    
for i in range(num + 1):
    ans.append(countOnes(i))
        
return ans
    
    
***************** COUNT SET BITS IN A GIVEN RANGE *************************

def countSetBits(n):

    count = 0
    
    while n:
        n&=(n-1)
        count+=1
        
    return count


def countSetBitsinRange(n,l,r):
    
    num = (((1<<r) - 1) ^ ((1<<(l-1)) -1))
    
    return countSetBits(n & num)


n = 42
l = 2
r = 5
ans = countSetBitsinRange(n,l,r)
print ans 


***************** BITWISE AND OF A RANGE (0 < X < Y) *************************

def msbPos(n):

    msb_p = -1
    
    while (n>0):
        
        n = n>>=1
        msb_p+=1
        
    return msb_p

def andOperator(x,y):
    
    #Initialize result
    res = 0
    
    while (x>0 and y>0):
        
        msb_p1 = msbPos(x)
        msb_p2 = msbPos(y)
               
        #If positions are not same, then return
        
        if (msb_p1!=msb_p2):            
            break
        
        #Add 2^msb_p1 to the result         
        msb_val = (1 << msb_p1)
        res = res + msb_val
        
        #Subtract 2^msb_p1 from x and y 
        x = x - msb_val
        y = y - msb_val
        
    return res 
        
        
x,y = 10,15
print(andOperator(x,y))


****************** TOTAL BITS OF A NUMBER **********************************

def countBits(n):
    
    count = 0
    
    while n:        
        count +=1
        n >>=1
        
    return count 


i = 65
print(countBits(i))


**************** CHECK IF A GIVEN NUMBER HAS ALTERNATING BITS ******************

def hasAlternatingBits(n):
    bits = bin(n)
    
    return all(bits[i]!=bits[i+1] for i in range(len(bits)-1))


**************** PROGRAM TO CHECK IF A BINARY REPRESENTATION OF A NUMBER IS A PALINDROME ***********

def isKthBitSet(x,k):
    
    if ((x & (1 << (1-k)))!=0):
    
        return True
        
    else:
        return False 


def isPalindrome(x):
    
    l = 1
    
    r = 2*8
    
    while(l<r):
        
        if(isKthBitSet(x,l)!=isKthBitSet(x,r)):
            return False
            
        l+=1
        r-=1
        
    return True

if __name__ == '__main__':

    x = 1 << 15+1 << 16
    
    print(int(isPalindrome(x)))
    
    x = 1 << 31+1 << 32
    
    print(int(isPalindrome(x)))
    
      
#Alternate method 
def binarypalindrome(num):

    binary = bin(num)[2:]
    
    return binary == binary[::-1]
    
    
if __name__=="__main__":
    num = 9
    print binarypalindrome(num)

   
*********************** SET, CLEAR AND TOGGLE BITS ********************
def setBit(n,k):

    return (n | 1 << (k-1))

def clearBit(n,k):
    
    return (n & ~(1 << (k-1)))

def toggleBit(n,k):
    
    return (n ^ (1 << (k-1)))


if __name__=="__main__":
    
    n = 5
    k = 1
    
    print("%d with %d-th bit set:%d\n",n,k,setBit(n,k))

    print("%d with %d-th bit cleared:%d\n",n,k,clearBit(n,k))
    
    print("%d with %d-th bit toggled:%d\n",n,k,toggleBit(n,k))













    
















































