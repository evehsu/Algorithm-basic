from SortAlgorithm import *

import heapq

def get_k_smallest_minheap(mylist,k):
    heapq.heapify(mylist)
    ksmallest = []
    for i in range(k):
        ksmallest.append(heapq.heappop(mylist))
    return ksmallest

# def get_k_smallest_maxheap(mylist,k):
#     myheap = heapq._heapify_max(mylist[:k])
#     for i in range(k,len(mylist)):
#         if mylist[i] < myheap[0]:
#             myheap._heappushpop_max(myheap,mylist[i])
#
#     return myheap

def get_k_largest_minheap(mylist,k):
    klist = mylist[:k]
    heapq.heapify(klist)
    for i in range(k,len(mylist)):
        if (mylist[i] > klist[0]):
            heapq.heappushpop(klist,mylist[i])
    return klist

def merge_k_sorted_list(listOflist):
    # use minheap, so assuming we have k list with each size is n
    # the time complexity could reduced from O(nk^2) to O(nk*logk)
    # to track the index of element in list, we use tuple(val,(d1,d2)) and build a heap on tuple
    # when build a heap on tuple, it will heap sort only by tuple[0], which is our value. tuple[1] is the value idx in 2d array
    listOfTupleList = [[(val,(sublistIdx,sublist.index(val))) for val in sublist]
                       for (sublistIdx, sublist) in enumerate(listOflist)]
    listOflistLen = [len(x) for x in listOflist]
    initial = [x for sublist in listOfTupleList for x in sublist if x[1][1] == 0 ]
    heapq.heapify(initial)
    i = 0
    result = []
    while (i < sum(listOflistLen)):
        cur = heapq.heappop(initial)
        print("initial now pop ",cur)
        result.append(cur[0])
        i += 1
        print ("now after adding ",cur[0]," to result"," i is ", i)
        if (cur[1][1] < listOflistLen[cur[1][0]]-1):
            heapq.heappush(initial,listOfTupleList[cur[1][0]][cur[1][1] + 1])
            print("initial now add ",listOfTupleList[cur[1][0]][cur[1][1] + 1])
        else:
            # if one/some of the k list has been all added to result, we could reduce the min heap size
            # the min heap size is always equal to the number of list that need to be merged
            continue

    return result


def merge_k_sorted_list_equalSize(kList):
    """
    input: list of list, there are k sorted sublist with each one has n element
    output: one big list of sorted n*k element
    """
    # construct the original minheap
    k = len(kList)
    n = len(kList[0])
    minheap = []
    for i in range(k):
        minheap.append((kList[i][0],(i,0)))
    heapq.heapify(minheap)
    print minheap
    final = [0 for i in range(k*n)]
    # start iteration
    for idx in range(k*n):
        cur = heapq.heappop(minheap)
        print cur
        final[idx] = cur[0]
        cur_list_idx = cur[1][0] # which list we take
        cur_val_idx = cur[1][1] # which val we take
        if cur_val_idx < n - 1:
            heapq.heappush(minheap,(kList[cur_list_idx][cur_val_idx + 1],(cur_list_idx,cur_val_idx + 1)))
        else:
            continue
    return final


if __name__ == "__main__":
    curList = [3,1,1,2,2,3,3,4,5]
    nestedList = [[1,2,3],[4,5,6],[7,8,9]]
    nestedList2 = [[1,4,5],[4,5,6,7],[7,8,9]]

    print ("test get k largest",get_k_largest_minheap(curList,3))
    print ("test get k smallest",get_k_smallest_minheap(curList,3))
    print ("test k-way merge",merge_k_sorted_list(nestedList2))
