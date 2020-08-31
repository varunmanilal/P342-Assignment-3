#Code for partial pivot
def Parpivot(A, B):
    if A[k][k] == 0:
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[k][k]) and abs(A[k][k]) == 0:
                A[k], A[i] = A[i], A[k]
                B[k], B[i] = B[i], B[k]
    return A, B

#Code for gauss jordan
def GaussJordan(A, B):
    # the pivot row
    pivot = A[k][k]
    for i in range(k, n):
        A[k][i] /= pivot
    B[k] = B[k] / pivot
    # other rows
    for i in range(n):
        if A[i][k] == 0 or i == k:
            continue
        else:
            term = A[i][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - term * A[k][j]
            B[i] = B[i] - term * B[k]
    return B


def main():
    global n, k

    #1st set of equations
    with open('Q1A.txt') as matA:
        A = []
        for line in matA:
            A.append([float(x) for x in line.split()])

    B = [0, 0, 0]
    matB = open("Q1B.txt", "r")
    b = matB.read()
    b1 = (b.split(' '))
    for i in range(3):
        B[i] = float(b1[i])
    n = len(B)
    for k in range(n):
        Parpivot(A, B)
        GaussJordan(A, B)
        
    print("Solution of 1st set of equations",B)

    #2nd set of equations
    with open('Q2A.txt') as matA:
        A = []
        for line in matA:
            A.append([float(x) for x in line.split()])
    matB = open("Q2B.txt","r")
    b = matB.read()
    b1 = (b.split(' '))
    for i in range(3):
        B[i]=float(b1[i])
    n = len(B)
    for k in range(n):
        Parpivot(A, B)
        GaussJordan(A, B)
    
    print("Solution of 2nd set of equations",B)

main()
#The Soln of 1st set of equations = [3.0 1.0 -2.0]
#The Soln of 2nd set of equations = [-2.0 -2.0 1.0]
