def find_missing(mylist):
    n = len(mylist)
    x1 = mylist[0]
    x2 = 1
    for i in range(1,n):
        x1 ^= mylist[i]
    for j in range(2,n + 2):
        x2 ^= j
    return x1^x2

def find_the_single(mylist):
    # given an array with numbers ,only one number appear once and others are all twice
    # find the single one
    x = mylist[0]
    for i in range(1,len(mylist)):
        x ^= mylist[i]
    return x

if __name__ == "__main__":

    testlist1 = [1,2,3,5,6,7]
    testlist2 = [1,1,2,2,3,3,5]

    print("test find_miss_number is ", find_miss_number(testlist1))
    print("test find_the_single is ", find_the_single(testlist2))

