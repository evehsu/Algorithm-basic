# sliding window max

import heapq
from collections import deque

def sliding_window_max_forloop(mylist, window):
    """
    :param mylist:
    :return: list of max for given window
    using 2 for loop as time complexity of O(n*window), no good
    space O(n)
    """
    if len(mylist) < window:
        return
    mymax = [0] * (len(mylist) - window + 1)
    for i in range(len(mylist) - window + 1):
        tmpMax = mylist[i]
        for j in range(window):
            if tmpMax < mylist[i + j]:
                tmpMax = mylist[i + j]
        mymax[i] = tmpMax
    return mymax


def sliding_window_max_heap(mylist,window):
    """
    using heap so time complexity would be O(n*log(window))
    time:  O(2n) + O(2nlog(window) = O(nlog(window))
    space o(n)
    THIS SOLUTION IS WRONG
    AS HEAP IN PYTHON COULDN'T LOCATE ELEMENT BY VALUE  , SO ELEMENT OUT OF WINDOW MAY STILL EXIST IN THE HEAP
    """
    if len(mylist) < window:
        print("length of given list is shorter than window")
        return
    newlist = [-x for x in mylist]
    myheap = newlist[:window]
    mymin = [0] * (len(newlist) - window + 1)
    heapq.heapify(myheap)
    print myheap
    for i in range(window,len(newlist)):
        mymin[i - window] = heapq.heappop(myheap)
        heapq.heappush(myheap,newlist[i])
    mymin[-1] = heapq.heappop(myheap)
    return [-x for x in mymin]


def slide_window_max_deque(mylist,window):
    """
    using a deque to save the max element in the cur window
    deque is saving the element 1. max of cur window 2. potential max in later window
    for achieving this
    within each window
    1. if deque is null insert element
    2. if new element is larger than deque's tail, pop tail(cur tail is impossible to be cur max or later max) and insert new element to tail
    3. if new element is smaller than deques tail, insert to tail (cur tail and added element could be max)

    first: iterate the first window, implement 1 2 3
    for each item after:
        the head of deque is max in cur window
        if element in deque is only belong to previous window, pop out
        do similar:  implement 1 2 3
    time complexity is O(n), space O(n + k)
    """
    if len(mylist) < window:
        return

    mydeque = deque([])
    for i in range(window):
        while mydeque and mylist[i] >= mylist[mydeque[-1]]:
            mydeque.pop()
        mydeque.append(i)
    mymax = [0] * (len(mylist) - window + 1)

    for i in range(window,len(mylist)):
        mymax[i - window] = mylist[mydeque[0]]
        while mydeque and mydeque[0] <= i - window:
            mydeque.popleft()
        while mydeque and mylist[i] >= mylist[mydeque[-1]]:
            mydeque.pop()
        mydeque.append(i)
    mymax[-1] = mylist[mydeque[0]]
    return mymax
