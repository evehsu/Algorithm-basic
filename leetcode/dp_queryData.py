"""
how to use dp (addional memory) to make frequent query faster
"""
# 1-D query
def query_list(mylist,i,j):
    """
    given a list, we need to frequently query the sum between mylist[i] and mylist[j]
    usually it takes o(n) with query the list directly, how to reduece to o(1)?

    solution: build another list m, m[i] = sum(mylist[0:i + 1] for i in range(len(mylist))
    so sum (mylist[i:j]) inclusive  =  m[j] - m[i] + mylist[i]
    time O(N)
    space O(n)
    """
    m = [0] * len(mylist)
    m[0] = mylist[0]
    for p in range(1,len(mylist)):
        m[p] = m[p - 1] + mylist[p]
    return m[j] - m[i] + mylist[i]


# 2-d query
# given a matrix of integers(pos and neg), how to find/query the submatrix with largest sum
def query_mat_largest_sum(myMat):
    """

    :param myMat:
    :return:
    """