#-------------------Algebra and Coding First Homework----------------------------#
    #|########Student: Touer Mohamed Elamine.
    #|##########Group: 4.
    #|##Academic Year: 2024/2025.
    #|######Professor: Rezki Chemlal.
#-------------------Algebra and Coding First Homework----------------------------#

def createmat(n): #Creates a square matrix of size n. Not that useful since we can write arrays of size n^2
    a = []  #All this function does is that it forces the user to input n^2 entries.
    for i in range(n*n):
        a.append(input())
    return a


def printmat(a): #Prints a square matrix of size n. It's for testing purposes only
    n = len(a)**(1/2) #All the function does is it writes each row in a separate line
    if n.is_integer:
        n= int(n)
        print("[")
        for j in range(0,n):
            print(a[n*j:n*(j+1)])
        print("]")
    else:
        return "The matrix is not square!"


def decomp(a): #Decomposes a square matrix of size 2k into 4 matrices of size k.
    n = len(a)**(1/2)
    if not n.is_integer:
        return "The matrix is not square!"
    elif n%2 != 0:
        return "The matrix is of odd size!"
    else:
        n = int(n)
        k = int(n/2)
        A = [[], [], [], []]
        for i in range(0,2):
            for j in range(0,k):
                A[i] = A[i] + (a[n*j + i*k : n*j+k + i*k]) #this computes A11 and A12, e.g for A11, we take the elements from a11 to a1k, and
        for i in range(2,4):                               #we add them to A11, then the elements from an1 to ank, and so on.
            for j in range(0,k):
                A[i] = A[i] + (a[n*j + i*k + (k-1)*n: n*j+k + i*k + (k-1)*n])        
    
        return A


def prod(a,b): #product of square matrices of the same size.
    n = len(a)**(1/2)
    m = len(b)**(1/2)
    if not n.is_integer:
        return "One of the matrices is not square!"
    if n != m:
        return "The matrices have different sizes!"
    n = int(n)
    c = []
    c_entry = 0
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                c_entry += a[i*n+k]*b[k*n+j] #the general form of a_rs is a[r*n+s], where 0<=r,s<=n-1, so we multiply accordingly.
            c.append(c_entry)
            c_entry = 0
    return c


def sum(a,b): #sum of matrices of the same size.
    
    if len(a) != len(b):
        return "The matrices have different sizes!"
    c = []
    for i in range(0, len(a)):
      c.append(a[i]+b[i])
    return c


def inv(a): #additional inverse of a matrix
    c = []
    for i in range(0, len(a)):
        c.append(-a[i])
    return c


def strassen(a,b):   #multiplication of matrices of size 2^n (i.e. matrices with 2^2n elements) with strassen's algorithm. 
    if len(a) == 1 and len(b) == 1:  #No size check is included due to the increased time complexity.
        return [a[0]*b[0]]
    else:         #A11 = A[0], A12 = A[1], A21=A[2], A22=A[3]
        A = decomp(a)    
        B = decomp(b)    
        M1 = strassen(sum(A[0],A[3]), sum(B[0],B[3]))
        M2 = strassen(sum(A[2],A[3]), B[0])
        M3 = strassen(A[0], sum(B[1],inv(B[3])))
        M4 = strassen(A[3], sum(B[2], inv(B[0])))
        M5 = strassen(sum(A[0],A[1]), B[3])
        M6 = strassen(sum(A[2], inv(A[0])), sum(B[0], B[1]))
        M7 = strassen(sum(A[1],inv(A[3])), sum(B[2], B[3]))
        
        return sum(sum(M1,M4),sum(inv(M5),M7))+ sum(M3,M5)+ sum(M2,M4)+ sum(sum(M1,inv(M2)),sum(M3,M6))
    

def strassen2(a,b):   #multiplication of matrices of size 2^n (i.e. matrices with 2^2n elements) with strassen's algorithm. 
    if len(a) == 1 and len(b) == 1:  #No size check is included due to the increased time complexity.
        return [a[0]*b[0]]
    else:         #A11 = A[0], A12 = A[1], A21=A[2], A22=A[3]
        A = decomp(a)    
        B = decomp(b)    
        M1 = prod(sum(A[0],A[3]), sum(B[0],B[3]))
        M2 = prod(sum(A[2],A[3]), B[0])
        M3 = prod(A[0], sum(B[1],inv(B[3])))
        M4 = prod(A[3], sum(B[2], inv(B[0])))
        M5 = prod(sum(A[0],A[1]), B[3])
        M6 = prod(sum(A[2], inv(A[0])), sum(B[0], B[1]))
        M7 = prod(sum(A[1],inv(A[3])), sum(B[2], B[3]))
        
        return sum(sum(M1,M4),sum(inv(M5),M7))+ sum(M3,M5)+ sum(M2,M4)+ sum(sum(M1,inv(M2)),sum(M3,M6))









'''
a = list(range(1,65))
b = list(range(1,65))
print(a)
print(b)
print(prod(a,b))
print(sum(a,b))
print(strassen(a,b))
'''