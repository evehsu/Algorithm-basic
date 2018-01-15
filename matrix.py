
def matrix_transpose(matrix): # requirement space complexity
    # matrix is a n*m matrix represented in a 2-d array
    # length n list and each element has len m
    # n is num of rows
    n = len(matrix)
    # m is num of cols
    m = len(matrix[0])
    # N is the matrix size
    N = n*m
    flatList = [item for sublist in matrix for item in sublist]
    cycle  = set()
    for start in range(1,N - 1): # the first and the last does not need to change
        if (start in cycle):
            continue;
        buff1 = flatList[start]

        #ol/nl is the old/new location before/after tranpose
        ol = start
        while (ol not in cycle):
            nl = (ol*n)%(N-1) # transpose formula
            cycle.add(ol)
            buff2 = flatList[nl]
            flatList[nl] = buff1
            buff1 = buff2
            ol = nl
    return([flatList[i:i + n] for i in range(0, len(flatList), n)])


def matrix_transpose_comment(matrix): # requirement space complexity

    n = len(matrix)
    # m is num of cols
    m = len(matrix[0])
    # N is the matrix size
    N = n*m
    flatList = [item for sublist in matrix for item in sublist]
    cycle = set()

    for start in range(1,N - 1):
        if (start in cycle):
            print("current start ", start, "is in current cycle ",cycle)
            continue;
        buff1 = flatList[start]

        #ol/nl is the old/new location before/after tranpose
        ol = start
        while (ol not in cycle):
            nl = (ol*n)%(N-1)
            print("now we are at pos ol ",ol," and want to move it to pos nl ",nl)
            cycle.add(ol)
            buff2 = flatList[nl]
            flatList[nl] = buff1
            buff1 = buff2
            ol = nl
            print flatList
        print("ol " ,ol, " is in cur cycle ",cycle," and now we complete the current cycle")

    return([flatList[i:i + n] for i in range(0, len(flatList), n)])

def spiral_print_2D(array_2d):
    # T: top initial as 0
    # B: bottom initial as number of rows
    # R: right initial as numeber of cols
    # L: left initial as 0
    # direction == 0: left => right on top
    # direction == 1: top => down on right
    # direction == 2: right => left on down
    # direction == 3: down => top on left
    T = 0
    B = len(array_2d) - 1
    L = 0
    R = len(array_2d[0]) - 1
    direction = 0
    while B >= T and L <= R:
        if direction == 0:
            for i in range(L, R + 1):
                print array_2d[T][i]
            T += 1;
            direction += 1
        if direction == 1:
            for j in range(T,B + 1):
                print array_2d[j][R]
            R -= 1;
            direction += 1
        if direction == 2:
            for i in range(R,L - 1,-1):
                print array_2d[B][i]
            B -= 1;
            direction += 1
        if direction == 3:
            for j in range(B,T - 1,-1):
                print array_2d[j][L]
            L += 1
            direction = (direction + 1)%4
    return


def rotate_matrix_clockwise(myMat):
    """
    rotate the matrix in clock wise deriction of 90 degrees
    :param myMat: m row and n col
    :return:
    [0][0] => [0][n-1] => [n-1][n-1] => [0][0]
    use another object to save tmp result
    1 2 3 4 5
    6 7 8 9 0
    2 3 4 5 6
    1 2 3 4 5
    4 5 6 7 7
    so if n is odd, there are n/2 round + 1 center(center does not need to move)
    if n is even, there are n/2 round
    """
    n = len(myMat)
    for level in range(0,n/2):
        for i in range(level,n - level - 1):
            tmp = [myMat[level][i],
                   myMat[i][n-level-1],
                   myMat[n-level-1][n-i-1],
                   myMat[n-i-1][level]]
            myMat[level][i] = tmp[3]
            myMat[i][n-level-1] = tmp[0]
            myMat[n-level-1][n-i-1] = tmp[1]
            myMat[n-i-1][level] = tmp[2]
    return myMat


# test
if __name__ == "__main__":

    #myMatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #print(matrix_transpose(myMatrix))
    myMatrix1 = [["A",1],["B",2],["C",3],["D",4]]
    myMatrix2 = [[1,2,3,],[4,5,6],[7,8,9],[10,11,12]]
    print(matrix_transpose(myMatrix1))
    print ("test spiral_print 2d ", spiral_print_2D(myMatrix))