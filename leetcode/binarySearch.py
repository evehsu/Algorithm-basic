def find_target(mylist,target):
    # given a sorted list in ascending order, return the target index or -1 if no target has been found
    # assuming mylist is not null
    left = 0
    right = len(mylist) - 1
    while left <= right: # this is where decides whether we could enter the while loop
        mid = left + (right - left)/2
        if mylist[mid] == target:
            return mid
        elif mylist[mid] < target: # this is where decides whether we will miss the true answer
                                   # and whether we will never getting out of the while loop
            left = mid + 1
        else:
            right = mid - 1

    return -1

def find_target_2D(myMat, target):
    nrow = len(myMat)
    ncol = len(myMat[0])
    left = 0
    right = nrow * ncol - 1
    while left <= right:
        mid = left + (right-left)/2
        midrow = mid/ncol
        midcol = mid%ncol
        if myMat[midrow][midcol] == target:
            return [midrow,midcol]
        elif myMat[midrow][midcol] > target:
            right = mid - 1
        else:
            left = mid + 1
    return [-1,-1]


def find_target_or_closest(mylist,target):
    # return target index , if not exist return the index of the closest of the number to target
    left = 0
    right = len(mylist) - 1
    while left < right-1:
        mid = left + (right - left)/2
        if (mylist[mid] >= target):
            right = mid # current mid could still be the true answer
            print("now right is updated to ", right)
        else:
            left = mid
            print("now left is updated to ", left)
    print ("end of while loop left is ", left, " right is ",right)
    # add post processing to see left or right which is more close to target
    if abs(mylist[left] - target) < abs(mylist[right] - target):
        print ("closest number to target ", target," is at position ", left)
    else:
        print ("closest number to target ", target," is at position ", right)
    return

def find_first_occur(mylist,target):
    # return the index of first occurance of target and otherwise return -1
    left = 0
    right = len(mylist) - 1
    # now if mid is target , we could not stop searching
    while left < right - 1:
        mid = left + (right - left)/2
        if (mylist[mid] >= target):
            right = mid
        else:
            left = mid
    if mylist[left] == target:
        return left
    elif mylist[right] == target:
        return right
    else:
        return -1



if __name__ == "__main__":
    tmplist = [1,1,2,3,4,5,6,9]
    k = 1
    myMat = [[1,2,3],[4,5,6],[7,8,9]]
    # print ("test find_target ", find_target(tmplist,k))
    # find_target_or_closest(tmplist,k)
    # print ("test find_first_occur ", find_first_occur(tmplist,k))
    print ("test find_target_2D ", find_target_2D(myMat,4))