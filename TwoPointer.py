"""
This scripts collected problem that could be solved using two pointers
general rules:

if two pointer moving on the same direction
1. we have slow index and fast inddex
2. left of slow(may or may not include slow) is element for return, right than fast is unknown, between slow and fast is unimportant
3. the relative position of element won't be changed

if two pointer moving on the opposite position
1. one starts from left and the other starts from right
2. left than left pointer and right than right pointer is element ready for return
3. in the result, the relative position of elements may be changed
"""

"""
slow fast on the same direction
"""

def rm_dup_sorted_array(mylist):
    """

    :param mylist: an sorted array with dup
    :return: sorted array without dup
    when slow is not equal to fast, we move slow to 1 position and copy fast, otherwise move fast to next position
    time : O(n)
    """
    slow = 0
    fast = 1

    while fast < len(mylist):
        if mylist[slow] != mylist[fast]:
            slow += 1
            mylist[slow] = mylist[fast]
            fast += 1
        else:
            fast += 1
    return mylist[:slow + 1]


def rm_dup_keep2(mylist):
    """
    compared with rm_dup_sorted_array, we could start with slow = 1, fast = 2, and compare mylist[slow - 1] & mylist[fast]
    :param mylist:
    :return:
    """
    if len(mylist) <= 2:
        return mylist
    slow = 1
    fast = 2
    while fast < len(mylist):
        if mylist[slow - 1] != mylist[fast]:
            slow += 1
            mylist[slow] = mylist[fast]
            fast += 1
        else:
            fast += 1
    return mylist[:slow + 1]


def rm_dup_keepK(mylist,k):
    """
    similarly, we could just check mylist[slow - (k - 1)] and mylist[fast]
    note that we could do this because we know the array is sorted (otherwise this method will not work)
    when mylist[fast] == mylist[slow - (k -1)], we could know mylist[slow -k + 1:slow + 1] which is [slow -k + 1 :slow]
    inclusive k element are all equal.
    :param mylist:
    :return:
    """
    if len(mylist) <= k:
        return mylist
    slow = k - 1
    fast = k
    while fast < len(mylist):
        if mylist[slow - k + 1] != mylist[fast]:
            slow += 1
            mylist[slow] = mylist[fast]
            fast += 1
        else:
            fast += 1

    return mylist[:slow + 1]


def rm_dup_nokeep(mylist):
    """
    now we need to return mylist[:slow] instead of mylist[:slow + 1] (not including slow), because slow index may point
    to dup element
    when requires keep no dup element, which means we cannot copy always copy fast when mylist[fast] != mylist[slow]
    we could only copy when some counter is 1. so we need to introduce either a third pointer or a counter

    """
    if len(mylist) < 1:
        return
    slow = 0
    fast = 0
    while fast < len(mylist):
        begin = fast
        print begin,fast,1
        while fast < len(mylist) and mylist[begin] == mylist[fast]:
            fast += 1
        if fast - begin == 1:
            mylist[slow] = mylist[begin]
            slow += 1
    return mylist[:slow]


def rm_dup_nokeep_counter(mylist):
    if len(mylist) < 1:
        return
    slow = 0
    fast = 0
    while fast < len(mylist):
        counter = 0
        while fast + counter < len(mylist) and mylist[fast] == mylist[fast + counter] :
            counter += 1
        print counter
        if counter == 1:
            mylist[slow] = mylist[fast]
            slow += 1
        fast += counter

    return mylist[:slow]


def move_0_to_end(mylist):
    """
    move the 0 element to end of list without changing the relative position
    :param mylist:
    :return:
    """
    if len(mylist) <= 1:
        return mylist
    slow = 0
    fast = 0
    while fast < len(mylist):
        if mylist[fast] == 0:
            fast += 1
        else:
            mylist[slow] = mylist[fast]
            fast += 1
            slow += 1
    mylist[slow:] = 0
    return mylist




if __name__ == '__main__':

    list1 = [1,1,1,2,2,2,3,4,5]
    print("test rm_dup_sorted_array", rm_dup_sorted_array(list1))
    list2 = [1,1,1,2,2,2,2,3,4,5]
    print("test rm_dup_keep2", rm_dup_keep2(list2))
    list3 = [1,1,1,1,2,2,2,3,4,4,4,4,5]
    print("test rm_dup_keepK",rm_dup_keepK(list3,3))