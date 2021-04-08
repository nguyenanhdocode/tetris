def rotateMatrix(matrix):
    M = len(matrix)
    N = len(matrix[0])

    destination =[[0 for i in range(M)] for j in range(N)]

    for i in range(N):
        for j in range(M):
            destination[i][j] = matrix[M - j - 1][i]
    return destination

matrix = [
    [0,1,0],
    [1,1,1]
]

for i in range(4):
    matrix = rotateMatrix(matrix)
    print(matrix)