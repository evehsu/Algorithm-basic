from random import randint


def myShuffle(mylist):
    """
    # given an array, return one possible result of its shuffle
    # the result array appearance possibility is 1/n!
    # random sample 1 element at a time and repeat n times without replacement
    # time is O(N), space is O(N) or O(1)
    """
    permutation = mylist[:]
    n = len(permutation)
    for i in range(len(permutation)):
        randomNum = randint(0, n - i - 1)
        permutation[i], permutation[randomNum] = permutation[randomNum], permutation[i]
    return permutation


def reservoir_1(mylist):
    """
    given unlimited data flow of size n randomly sample 1 element
    so each probability is 1/n
    the solution need space O(N),
    for every iteration i from (0,N),if random picked number of randint(0,i-1) is 0,
     which is to say the probability is 1/i, we take the new coming number, otherwise use the number of last iteration
    """
    result = mylist[0]
    for index,item in enumerate(mylist):
        randomNum = randint(0,index)
        if randomNum == 0:
            result = item
        else:
            continue
    return result

def reservoir_k(mylist,k):
    # assuming n is really large
    result = []
    for index,item in enumerate(mylist):
        if index < k:
            result.append(item)
        else:
            randomNum = randint(0,index)
            if randomNum < k:
                result[randomNum] = item
    return result


def ran5_to_ran7():
    """
    it will be much easier to generate from larger range to smaller range
    such as ran7_to_ran5, if the number falls into [0,1,2,3,4], return result
    so we will try to concat this problem to large_to_small too
    the approach will be expand ran(5) to ran(25), and then ran(25) to ran(7)
    """

    # ran5_to_ran25
    row = randint(0,4)
    col = randint(0,4)
    ran25 = row * 5 + col

    # ran25_to_ran7
    endSampling = False
    result = -1
    while endSampling == False:
        if ran25 < 21:
            endSampling = True
            result = ran25 % 7
    return result





if __name__ == "__main__":

    testlist = [1,2,3,4,5,6]
    print("test myshuffle is ", myShuffle(testlist))
    print("test sample is ",reservoir_k(testlist,2))
    print("test ran5_to_ran7 ", ran5_to_ran7())




