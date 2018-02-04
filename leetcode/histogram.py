"""
find largest rectangle given a histogram
with histogram given by a list, the list index is x axis and list value is y axis=
"""
from collections import deque

def find_max_rectange(mylist):
    """
    find the maximum rectange that could formed by the given histotram
    http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
    :param mylist:
    :return:
    create a stack
    iterate from left to right
    if cur is greater than stack top index value ,then the index push to stack
    if cur is less than stack top index value, then pop stack and calculate area till cur value is greater than stack top
    (add 0 to the given array, so when interate to last dummy element, all element in stack will be popped out)
    Time o(N), Space, o(n)

    """
    stack = deque([])
    result = [0]
    # add dummy
    mylist.append(0)
    # iterate from left to right
    for i in range(len(mylist)):
        # push to stack when stack is empty or cur is larger
        if len(stack) == 0 or mylist[i] > mylist[stack[-1]]:
            stack.append(i)
        # if cur value is smaller than mylist[stack[-1].
        # we need to start pop stack till cur is larger again
        # similar to using deque to solve max in sliding window
        # the similarity is the index in stack following the order that their corresponding value in
        while len(stack) > 0 and mylist[i] <= mylist[stack[-1]]:
            cur_stack_top = stack.pop()
            cur_height = mylist[cur_stack_top]
            left = 0 if len(stack) == 0 else stack[-1] + 1
            result[0] = max(result[0],cur_height * (i - left))
        stack.append(i)
    return result[0]


def water_trap_dp(mylist):
    """
    given a histogram shape, calcuate the max water it could hold
    :param mylist:
    :return:
    using dp
    1. left_max create an array to save the max height from 0 to current index, which is max(array[0,i])
    2. right_max create an array to save the max height from n-1 to current index, which is max(array[i,n-1])
    3. current holding capability is min(left_max, right_max) - array[cur_index]
    time o(n) space o(n)
    """
    if len(mylist) < 1:
        print ("invalid input")
        return
    length = len(mylist)
    m1 = [mylist[0]] * length
    m2 = [mylist[-1]] * length
    result = [0]
    for i in range(1,length):
        m1[i] = max(m1[i-1],mylist[i])
        m2[length - i - 1] = max(m2[length - i],mylist[length - i - 1])
    print m1
    print m2
    for i in range(length):
        result[0] += max(0,min(m1[i],m2[i]) - mylist[i])
    return result[0]