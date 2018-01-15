
"""
binary matrix problem : given a matrix of 0,1, find some pattern limit such as largest X, cross, square of 1
usually use longest 1 as helper matrix
"""

def largest_one_matrix(mymatrix):
    """
    find the largest matrix of 1 in 1 binary matrix and return the edge length
    0 0 0 0 0
    1 1 1 1 0
    1 1 1 1 0
    1 1 1 0 0
    1 1 1 0 0
    should return 3
    similarly as edit distance, we could use a matrix to save the tmp result => 2-DP
    m
    0 0 0 0 0
    1 1 1 1 0
    1 2 2 2 0
    1 2 3 0 0
    1 2 3 0 0
    if mymatrix[i][j] == 0:
        m[i][j] = 0
    else:
        m[i][j] = min(m[i-1][j],m[i][j-1],m[i-1][j-1]) + 1
    :param mymatrix:
    :return: edge length of matrix of 1

    time complexity is O(N^2), space complexity is O(N^2)
    """
    # deep copy will copy original object while shallow copy will copy the reference
    # m = copy.deepcopy(mymatrix)
    m = [x[:] for x in mymatrix]
    ncol = len(mymatrix[0])
    nrow = len(mymatrix)
    global_max = 0
    for i in range(1,nrow):
        for j in range(1,ncol):
            if m[i][j] != 0:
                m[i][j] = min(m[i-1][j],m[i][j-1],m[i-1][j-1]) + 1
                if m[i][j] > global_max:
                    global_max = m[i][j]
            else:
                continue
    return global_max


def largest_cross(myMat):
    """
    0 1 0 0
    1 1 1 1
    0 1 0 1
    0 1 0 0
    :param myMat:
    :return: target cross arm size

    solution: we could count the longest1 from bottom-up, up-bottom, left-right, right-left for each position [i,j]
    and for creating the result matrix iterate the above 4 matrix and get the minimum one
    finally return the largest element of the final matrix

    time: O(n^2) space: o(n^2)
    """
    def longest_1_sofar(mylist,direction):
        m = [0] * len(mylist)
        if direction == 'pos':
            m[0] = mylist[0]
            for i in range(1,len(m)):
                if mylist[i] == 1:
                    m[i] = m[i - 1] + 1
                else:
                    m[i] = 0
        else:
            m[len(mylist) - 1] = mylist[-1]
            for i in range(len(mylist) - 2, -1, -1):
                if mylist[i] == 1:
                    m[i] = m[i + 1] + 1
                else:
                    m[i] = 0
        return m

    nrow = len(myMat)
    ncol = len(myMat[0])

    # create left-right and right-left matrix
    left_right = [[[0] for i in range(ncol)] for j in range(nrow)]
    right_left = [[[0] for i in range(ncol)] for j in range(nrow)]
    for i in range(nrow):
        left_right[i] = longest_1_sofar(myMat[i],'pos')
        right_left[i] = longest_1_sofar(myMat[i],'neg')

    # create up-bottom and bottom-up matrix
    up_bottom = [[[0] for i in range(ncol)] for j in range(nrow)]
    bottom_up = [[[0] for i in range(ncol)] for j in range(nrow)]
    for j in range(ncol):
        tmpResult_ub = longest_1_sofar([row[j] for row in myMat],'pos')
        tmpResult_bu = longest_1_sofar([row[j] for row in myMat],'neg')
        for i in range(len(up_bottom)):
            up_bottom[i][j] = tmpResult_ub[i]
            bottom_up[i][j] = tmpResult_bu[i]

    # build final result matrix
    final_result = [[[0] for i in range(ncol)] for j in range(nrow)]
    global_max = 0
    for i in range(len(final_result)):
        for j in range(len(final_result[0])):
            final_result[i][j] = min(left_right[i][j],right_left[i][j],up_bottom[i][j],bottom_up[i][j])
            if final_result[i][j] > global_max:
                global_max = final_result[i][j]
    return global_max


def largest_X(myMat):
    """
    0 1 0 1
    1 0 1 1
    0 1 0 1
    0 1 0 0
    :param myMat:
    :return: target cross arm size

    solution: we could count the longest1 from left top - right bottom, right top - left bottom, left bottom - right top
    right bottom - left top, for  each position [i,j]
    and for creating the result matrix iterate the above 4 matrix and get the minimum one

    if iterate by diagonal, we could use the fact that on the i - j or i+j is constant for element on same diagonal
    """

    def longest_1_sofar(mylist,direction):
        m = [0] * len(mylist)
        if direction == 'pos':
            m[0] = mylist[0]
            for i in range(1,len(m)):
                if mylist[i] == 1:
                    m[i] = m[i - 1] + 1
                else:
                    m[i] = 0
        else:
            m[len(mylist) - 1] = mylist[-1]
            for i in range(len(mylist) - 2, -1, -1):
                if mylist[i] == 1:
                    m[i] = m[i + 1] + 1
                else:
                    m[i] = 0
        return m

    nrow = len(myMat)
    ncol = len(myMat[0])

    # create lefttop_rightbottom and rightbottom_lefttop matrix
    lt_rb = [[[0] for i in range(ncol)] for j in range(nrow)]
    rb_lt = [[[0] for i in range(ncol)] for j in range(nrow)]

    for mySum in range(0,nrow + ncol - 1):
        i_range = range(0,min(nrow ,mySum + 1))
        j_range = [x1 - x2 for (x1,x2) in zip([mySum]*len(i_range),i_range)]
        comb = zip(i_range,j_range)
        comb = [x for x in comb if x[0] <= 3 and x[1] <= 3]
        lt_rb_tmp = longest_1_sofar([myMat[x[0]][x[1]] for x in comb],'pos')
        rb_lt_tmp = longest_1_sofar([myMat[x[0]][x[1]] for x in comb],'neg')
        for idx in range(len(comb)):
            lt_rb[comb[idx][0]][comb[idx][1]] = lt_rb_tmp[idx]
            rb_lt[comb[idx][0]][comb[idx][1]] = rb_lt_tmp[idx]

    # create righttop_leftbottom  and leftbottom_righttop matrix
    rt_lb = [[[0] for i in range(ncol)] for j in range(nrow)]
    lb_rt = [[[0] for i in range(ncol)] for j in range(nrow)]

    # myGap is j-i
    for myGap in range(ncol - 1,-nrow,-1):
        i_range = range(0,nrow)
        j_range = [x1 + x2 for (x1,x2) in zip(i_range,[myGap]*len(i_range))]
        comb = zip(i_range,j_range)
        comb = [x for x in comb if x[0] <= 3 and x[0] >= 0 and x[1] <= 3 and x[1] >= 0]
        rt_lp_tmp = longest_1_sofar([myMat[x[0]][x[1]] for x in comb],'pos')
        lb_rt_tmp = longest_1_sofar([myMat[x[0]][x[1]] for x in comb],'neg')
        for idx in range(len(comb)):
            rt_lb[comb[idx][0]][comb[idx][1]] = rt_lp_tmp[idx]
            lb_rt[comb[idx][0]][comb[idx][1]] = lb_rt_tmp[idx]

        # build final result matrix
    final_result = [[[0] for i in range(ncol)] for j in range(nrow)]
    global_max = 0
    for i in range(len(final_result)):
        for j in range(len(final_result[0])):
            final_result[i][j] = min(lt_rb[i][j],rb_lt[i][j],rt_lb[i][j],rb_lt[i][j])
            if final_result[i][j] > global_max:
                global_max = final_result[i][j]
    return global_max


def largest_surrounded1(myMat):
    """
    1 1 1 1 1
    1 0 0 0 1
    1 0 0 0 1
    1 0 0 0 1
    1 1 1 1 1

    return 5
    :param myMat:
    :return: edge length
    step 1: build M1 matrix for right-left and M2 matrix bottom-up (one horizontal one vertical)
    step 2: for every position i,j (possible left top corner), check min(M1[i][j], M2[i][j]) as possible edge length
                for length in range(0,possible edge length + 1), check M1[i + possible edge length][j] <left bottom corner> and
                M2[i][j + possible edge length]<right top corner>
                in order to see whether the square is valid
    time: step1 N^2, step2 N^2 *N

    """
    nrow = len(myMat)
    ncol = len(myMat[0])

    def longest_1_sofar(mylist,direction):
        m = [0]*len(mylist)
        if direction == "pos":
            m[0] = mylist[0]
            for i in range(1,len(mylist)):
                m[i] = m[i - 1] + 1 if mylist[i] == 1 else 0
        else:
            m[-1] = mylist[-1]
            for i in range(len(mylist) - 2, -1, -1):
                m[i] = m[i + 1] + 1 if mylist[i] == 1 else 0
        return m

    # step1 : create M1 and M2
    M1 = [[[0] for i in range(ncol)] for j in range(nrow)]
    for i in range(len(M1)):
        M1[i] = longest_1_sofar(myMat[i],"neg")

    M2 = [[[0] for i in range(ncol)] for j in range(nrow)]
    for j in range(len(M2[0])):
        tmpResult = longest_1_sofar(myMat[:][j], "neg")
        for i in range(len(tmpResult)):
            M2[i][j] = tmpResult[i]
    # step2:
    global_max = 0
    cur_max = 0
    for i in range(nrow):
        for j in range(ncol):
            if(myMat[i][j] == 1):
                potential = min(M1[i][j],M2[i][j])
                for p in range(potential-1,0,-1):
                    if M1[i + p][j] >= p and M2[i][j + p] >= p:
                        cur_max = p
                        break

            else:
                continue
            if cur_max + 1 > global_max:
                global_max = cur_max + 1 # potential + 1 (start point itself)
    return global_max