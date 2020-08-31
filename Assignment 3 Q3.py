#code for Partial pivot
def Parpivot(A,B):
    if A[k][k] == 0:
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[k][k]) and abs(A[k][k]) == 0:
                A[k], A[i] = A[i], A[k]
                B[k], B[i] = B[i], B[k]
    return A, B
#code for gauss jordan
def GaussJordan(A,B):
    # the pivot row
    pivot = A[k][k]
    for i in range(k, n):
        A[k][i] /= pivot
    B[k] /= pivot
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

#code for matrix multiplication
def MatrixMultiply(M,A):
    B=[[0,0,0],[0,0,0],[0,0,0]]
    for x in range(len(M)):
        for y in range(len(A[0])):
            for z in range(len(M[0])):
                B[x][y] += M[x][z] * A[z][y]

    inv = print("The matrix A*Ainv is", B)
    return B

def main():
    #A*A-1=I->I*A-1=A-1
    #B=I initially can be taken as three column vectors [1 0 0],[0,1,0],[0,0,1]
    I = [[1,0,0],[0,1,0],[0,0,1]]
    C = [[0,0,0],[0,0,0],[0,0,0]]
    global n,k
    for l in range(3):
        with open('MatrixA1.txt') as matA:
            A = []
            for line in matA:
                A.append([float(x) for x in line.split()])
        n = len(I[l])
        for k in range(n):
            Parpivot(A,I[l])
            GaussJordan(A,I[l])

        C[l]=I[l]

    # Taking transpose gives the inverse matrix
    Ainv = [[C[j][i] for j in range(3)] for i in range(3)]

    #The inverse
    print("The inverse is:",Ainv)
    with open('MatrixA1.txt') as matA:
        A = []
        for line in matA:
            A.append([float(x) for x in line.split()])
   
    MatrixMultiply("The matrix A*Ainv",A,Ainv)

main()
#The inverse is [[-3.0, 3.0, -7.0],[1.0, 1.0, 0.0][1.0, 0.0, 1.0]]
#The matrix A*Ainv = [[1.0, 0.0, 0.0][0.0, 1.0, 0.0][0.0, 0.0, 1.0]]
