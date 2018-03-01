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


def find_closest_k_to_target(mylist,target,k):
    """
    given a list and a target, print out the closest k element that are closest to the target
    1.apply binary search to find target or cloest :time o(logn)
    2. compare left and right, moves the one whose gap is smaller : time o(k)
    total time o(logn + k)
    3 optional: the step2 could be optimized to logk, by the approach in the below find_kth_smallest_2_sorted_list

    :param mylist:
    :param target:
    :return:
    """
    # find closest target
    if len(mylist) < 1:
        return
    left = 0
    right = len(mylist) - 1
    while left < right - 1:
        mid = (left + right)/2
        if target <= mylist[mid]:
            right = mid
        else:
            left = mid
    while k > 0:
        if abs(mylist[left] - target) < abs(mylist[right] - target):
            print mylist[left]
            left -= 1
        else:
            print mylist[right]
            right += 1
        k -= 1
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


def find_sqrt(x, accur):
    """
    find the sqrt root of x (positive integer), which abs(sqrt ^ 2 - x) is less than accur
    :param x:
    :return:
    """
    if x < 0:
        return
    left = 0
    right = x
    while abs(pow((left + right)/2.0,2) - x) > accur:
        mid = (left + right)/2.0
        if pow(mid,2) - x < 0:
            left = mid
        else:
            right = mid
    return (left + right)/2.0


def find_kth_smallest_2_sorted_list(list1,list2,k):
    """
    given 2 sorted list, find kth smallest using logk time (rather than k,shui xiao yi shui)
    compared list1[k/2] and list2[k/2], if list1[k/2] < list2[k/2], it's safe to delete k/2 elements from list1
    in the next iteration, check k/4, until k/XX == 1, now it only takes logk time
    """
    # assuming k < len(list1) + len(list2) - 1
    def helper(list1, list2, idx1,idx2, k):
        # base case
        if idx1 >= len(list1):
            return list2[idx2 + k -1]
        if idx2 >= len(list2):
            return list1[idx1 + k - 1]
        if k == 1:
            return min(list1[idx1],list2[idx2])
        # recursion rule
        # k < len(list1[idx1:] + len(list2[idx2:] - 1
        if idx1 + k/2 - 1 > len(list1):
            helper(list1,list2,idx1,idx2 + k/2 - 1,k - k/2)
        elif idx2 + k/2 - 1 > len(list2):
            helper(list1,list2,idx1 + k/2 - 1,k - k/2)
        else:
            if list1[idx1 + k/2 - 1] < list2[idx2 +k/2 - 1]:
                helper(list1,list2,idx1 + k/2 -1, idx2, k/2 - 1)
            else:
                helper(list1,list2,idx1, idx2 + k/2 -1, k/2 - 1)
    return helper(list1,list2,0,0,k)

"""

if __name__ == "__main__":
    tmplist = [1,1,2,3,4,5,6,9]
    k = 1
    myMat = [[1,2,3],[4,5,6],[7,8,9]]
    # print ("test find_target ", find_target(tmplist,k))
    # find_target_or_closest(tmplist,k)
    # print ("test find_first_occur ", find_first_occur(tmplist,k))
    print ("test find_target_2D ", find_target_2D(myMat,4))