"""
This is used for solving find common element in two array
the method is different in different assumption
if the given two arrays are sorted equal sized,then just iterate (m + n)
if given array are sorted one is much bigger than the other m>>n, then run binary search, time O(m*logn) at most run n times

if given array is unsorted, using hash table to save the smaller string
"""

def find_comment_element1(list1, list2):
    """
    assuming two list are equal sized and sorted in ascending order
    :param list1:
    :param list2:
    :return:
    """
    if len(list1) < 1 or len(list2) < 1:
        return
    i = 0
    j = 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result


def find_comment_element2(list1, list2):
    """
    assuming array is unsorted and unique
    :param list1:
    :param list2:
    :return:
    """
    result = []
    def put_to_dict(mylist):
        mydict = {}
        for item in mylist:
            if item in mydict:
                mydict[item] += 1
            else:
                mydict[item] = 1
        return mydict


    if len(list1) < len(list2):
        lookup = put_to_dict(list1)
        for item in list2:
            if item in lookup:
                result.append(item)
            else:
                continue
    else:
        lookup = put_to_dict(list2)
        for item in list1:
            if item in lookup:
                result.append(item)
            else:
                continue
    return result

def common_element_in_K_sorted_array(listOflist):
    """
    a1
    a2
    .
    .
    .
    ak
    s1 we could iteratively find the common element a1 + a2, a1 + a2 + a3 ..., O(kn)
    s2: binary reduction: a1 + a2, a3 + a4...time = O(kn + n * k/2 + n*k/4...) , still O(kn)
    different with k-way merge, doing the k array simultaneously is not applicable here, because if we followed the similar
    way to save k element in a heap, the heap won't tell whether this element is shared by all arrays, it could only
    pop the min element.(others unknown)
    :param listOflist:
    :return:
    """
    if len(listOflist) < 1 or len(listOflist[0]) < 1:
        # invalid input
        return
    if len(listOflist) < 2:
        # only one list
        return listOflist[0]
    result = listOflist[0]
    for i in range(1,len(listOflist)):
        list1 = result
        list2 = listOflist[i]
        result = find_comment_element1(list1,list2)
    return result
