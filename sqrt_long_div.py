
import math

n = 351.86
fr = 4 #No of fraction points
print()
print("n =",n)
m = n

if n<100:

    for j in range (10):
        if j*j<=n and (j+1)*(j+1)>n :
            res = j
            rem = n-j*j
            break

else:

    for i in range(100):
        m = m/10
        if m < 1:
            dgt = i+1
            break

    # print (dgt)
    # print()
    m = n
    l = math.ceil(dgt/2)
    A = [0]*l
    # print(len(A))
    # print()
    for i in range(l-1 ,-1, -1):
        
        A[i] = m % 100
        m = int(m / 100)
        print(A[i])

    # print()
    for i in range(l-1):
        # print(A[i])
        for j in range (10):
            if j*j<=A[i] and (j+1)*(j+1)>A[i] and i==0 :
                res = j
                rem = A[i]-res*res
                # print(res)
                print()
                break
        for j in range(0,10):
            if (rem*100)+A[i+1] >= (res*2*10+j)*j and (rem*100)+A[i+1] < (res*2*10+(j+1))*(j+1) :
                # print((rem*100)+A[i+1],(res*2*10+j)*j,j)
                rem = (rem*100)+A[i+1] - (res*2*10+j)*j
                res = res*10+j
                break

# print()
# print("rem=" , rem)            
# print("res=" , res)
# print()
if rem > 0:
    mul=res

    for i in range(1,fr+1):
        for j in range(0,10):
            if (rem*100) >= (mul*2*10+j)*j and (rem*100) < (mul*2*10+(j+1))*(j+1) :
                # print((rem*100),(mul*2*10+j)*j,j)
                rem = (rem*100) - (mul*2*10+j)*j
                res = res+(j/(10**i))
                mul = mul*10+j
                break

print("squre root =" , res)