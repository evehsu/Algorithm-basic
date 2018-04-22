
from random import randint

def swap(mylist, a, b):
    tmp = mylist[a]
    mylist[a] = mylist[b]
    mylist[b] = tmp
    return mylist


def selection_sort(mylist):
    if len(mylist) < 2 :
        return
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[i]:
                mylist[i],mylist[j] = mylist[j],mylist[i]
    return mylist


def merge_sort(mylist):
    if len(mylist) < 2:
        return mylist
    mid = len(mylist)/2
    mylist[:mid] = merge_sort(mylist[:mid])
    mylist[mid:] = merge_sort(mylist[mid:])

    def merge_sorted_list(list1,list2):
        result = [0] * (len(list1) + len(list2))
        i = 0
        j = 0
        k = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result[k] = list1[i]
                i += 1
            else:
                result[k] = list2[j]
                j += 1
            k += 1
        while i < len(list1):
            result[k] = list1[i]
            k += 1
            i += 1
        while j < len(list2):
            result[k] = list2[j]
            k += 1
            j += 1
        return result
    mylist = merge_sorted_list(mylist[:mid],mylist[mid:])

    return mylist

def quick_sort(mylist):
    left = 0
    right = len(mylist) - 1
    if (left < right):
        splitPoint = quick_sort_split(mylist)
        mylist[:splitPoint] = quick_sort(mylist[:splitPoint])
        mylist[splitPoint:] = quick_sort(mylist[(splitPoint):])
    return mylist

def quick_sort_split(mylist):
    # bucket i define : position is left than i exclude i will be smaller or equal than pivot_pos
    # bucket j define: position is right than j exclude j will be larger or equal than pivot_pos
    # note: [i,j]inclusive is unknown area
    # when i == j,if list[i] <= pivot,i = i+1,right now left than i will all <= pivot, safe to move pivot to position i
    #             if list[i] > pivot,swap(i,j),j = j-1,actually nothing has been swapped,safe to move pivot to position i

    print("now my list is ", mylist)
    pivot_pos = randint(0,len(mylist) - 1)
    pivot_val = mylist[pivot_pos]
    print("now the pivot pos is ", pivot_pos," and value is ",pivot_val)
    mylist[pivot_pos],mylist[len(mylist) - 1] = mylist[len(mylist) - 1],mylist[pivot_pos]
    print("after swap to right the list is ",mylist)
    i = 0
    j = len(mylist) - 2
    while i <= j:
        if mylist[i] > pivot_val:
            mylist[i],mylist[j] = mylist[j],mylist[i]
            j -= 1
        else:
            i += 1
        print("after this loop i is ", i ," and j is ",j)
    mylist[i], mylist[len(mylist) - 1] = mylist[len(mylist) - 1], mylist[i]
    print("now the pivot pos is ", i," on value of ",pivot_val)
    print("the cur list is ",mylist)
    return i


def rainbow_abc(mylist):
    i = 0
    j = 0
    k = len(mylist) - 1
    while (j <= k):
        if mylist[j] == "a":
            swap(mylist,i,j)
            j += 1
            i += 1
        elif mylist[j] == "b":
            swap(mylist,i,j)
            j += 1
        else:
            swap(mylist,j,k)
            k -= 1
    return mylist



    # bucket : left than not include i is a
    #          between i (inclusive) and j not include j is b
    #          right than k include k is c
    #          between j(inclusive) and k (inclusive) is unknown


# test
# print ("test selection sort " , selection_sort([4,67,3,3,2,6]))
# print ("test merge sorted list ", merge_sorted_list([67],[3]))
if __name__ == "__main__":
    curlist = [4,67,3,3,2,6]
    curStrList = ["a","b","c","c","b","a"]
    # print ("test merge sort", merge_sort(curlist))
    # print ("test quick sort", quick_sort(curlist))
    print ("test rainbow sort", rainbow_abc(curStrList))

