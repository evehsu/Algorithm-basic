#missing number
## common number of two sorted array
## top k freq word
# 2 sum 3 sum 4 sum
import heapq
def word_freq(mylist):
    # input is a list of string
    # output is a dictionary of word as key and freq as value

    dict = {}
    for i in range(len(mylist)):
        if mylist[i] in dict:
            dict[mylist[i]] += 1
        else:
            dict[mylist[i]] = 1
    return dict


def get_k_largest_minheap(mylist,k):
    klist = mylist[:k]
    heapq.heapify(klist)
    for i in range(k,len(mylist)):
        if (mylist[i] > klist[0]):
            heapq.heappushpop(klist,mylist[i])
    return klist


def largest_k_freq(mylist,k):
    my_word_freq = word_freq(mylist)
    my_word_freq_list = [(p,q) for q,p in my_word_freq.iteritems()] # because heapify will happen on the the first element of the tuple
    return get_k_largest_minheap(my_word_freq_list,k)


def find_min_missing(mylist,n):

    # given an array, start with 1 and end with n, no dup and but not continuous
    # find the minimum of the missing number
    # note that if there is only one missing number, we could just use XOR, which is time O(N) and space O (1),
    # but xor is invalid for multiple missing
    # we need to build a hash map for it with time O(N) and space O(N)

    dict = {}
    for i in range(len(mylist)):
        if mylist[i] in dict:
            dict[mylist[i]] += 1
        else:
            dict[mylist[i]] = 1
    min_miss = 0
    for j in range(1,n+1):
        if j in dict:
            continue
        else:
            min_miss = j
            break
    return min_miss


def common_element(list1, list2):
    # assuming list1, list2 have at least 1 element
    mydict = {}
    for item in list1:
        if item not in mydict:
            mydict[item] = [1,0]
        else:
            mydict[item][0] += 1
    for item in list2:
        if item not in mydict:
            mydict[item] = [0,1]
        else:
            mydict[item][1] += 1
    print mydict
    common = []
    for item in mydict:
        if mydict[item][0] > 0 and mydict[item][1] > 0:
            common.append(item)
    return common

def union_intersection(mylist1,mylist2):
    """
    # if the array is sorted, when len(mylist1) is almost equal to len(mylist2), we could iterate the two array and use a list to save the result
    # the above approach is time O(m+n)
    # if n << m, when the two array lenght is significantly different, we could to a binary search of every element from the smaller array in the larger array
    # the 2nd approach is time O(nlogm)
    # if the arrays are unsorted, we could only use hashmap to solve this, with time O(m + n)
    # if no dup in each array, we could use the element as key and elements count as value for dictionary
    # union set is all keys in dictionary; intersection is the keys with freq (value) > 1
    # if there are dup in each array, we need to use element as key and tuple(x,y) as key freq count, x is the freq of first array, y is freq count of 2nd array
    # union set is all keys, intersect is keys with tuple (x,y) where x,y are all above 0
    """
    dict = {}
    for i in range(len(mylist1)):
        if mylist1[i] in dict:
            dict[mylist1[i]] += 1
        else:
            dict[mylist1[i]] = 1
    for j in range(len(mylist2)):
        if mylist2[j] in dict:
            dict[mylist2[j]] += 1
        else:
            dict[mylist2[j]] = 1

    union = dict.keys()
    intersection = [key for key,val in dict.iteritems() if val > 1]
    resultDict = {"union": union, "intersection": intersection}
    return resultDict


def two_sum(mylist,target):
    """
    assuming list length > 2
    could have duplicatoin
    :param mylist:
    :param target:
    :return:  would return all possible combination
    time: o(n) <for building dict> + O(n ^3) <for loop> so O (N^3)
    """
    if len(mylist) < 2:
        return
    mydict = {}
    for idx, val in enumerate(mylist):
        if val in mydict:
            mydict[val].append(idx)
        else:
            mydict[val] = [idx]
    result = []
    for val in mydict.keys():
        search_target = target - val
        if search_target in mydict:
            list1 = mydict[val]
            list2 = mydict[search_target]
            for i in list1:
                for j in list2:
                    if i != j:
                        result.append([i,j])
            mydict.pop(val,None)
            mydict.pop(search_target,None)
        else:
            continue
    return result





if __name__ == "__main__":
    testlist = ["one","one","one","two","two","three","three","three",
                "four","four","four","four","five","five","five","five"]
    testlist2 = [1,2,3,4,5,6]
    print("test word_freq is",largest_k_freq(testlist,3))
    print("test two_sum is", two_sum(testlist2,7))