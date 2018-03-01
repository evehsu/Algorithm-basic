"""
other leetcode practice but not fall into a special category
"""


def merge_sort_interval(mylist,index):
    """
    merge sort for interval
    index: 0:sort by start of interval
    index  1 sort by end of interval
    :param mylist:
    :param index:
    :return:
    """
    if len(mylist) < 2:
        return mylist
    mid = len(mylist)/2
    mylist[:mid] = merge_sort_interval(mylist[:mid],index)
    mylist[mid:] = merge_sort_interval(mylist[mid:],index)

    def merge_sorted_list(list1,list2,index):
        result = [0] * (len(list1) + len(list2))
        i = 0
        j = 0
        k = 0
        while i < len(list1) and j < len(list2):
            if list1[i][index] <= list2[j][index]:
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
    mylist = merge_sorted_list(mylist[:mid],mylist[mid:],index)

    return mylist


def merge_interval(mylist):
    """
    given a list of interval, merge the interval
    [1,3],[2,6],[8,10],[15,18] => [1,6],[8,10],[15,18]
    :param mylist:
    :return:
    solution: sort the list by interval left boundaryand then iterate once
    """
    mylist_sort = merge_sort_interval(mylist,0)
    result = [mylist_sort[0]]
    for item in mylist_sort[1:]:
        cur_tail = result[-1][1]
        next_head = item[0]
        next_tail = item[1]
        if cur_tail >= next_head:
            result[-1][1] = next_tail
        else:
            result.append(item)
    return result


def find_meeting_room(mylist):
    """
    similar as merge_interval, still given a list of intervals representing meeting start and end time
    find the minimum meeting room required

    same as merge_interval: if interval overlap with each other, then we need 2 meeting room
    otherwise one is good

    solution
    step1: sort the interval by start, save sorting result
    step2: sort the interval by end, save sorting result
    step3: set end pointer to 0 ,iterate the sorted start list, if cur_start < cur_end, meeting room  + 1,
    else end_pointer + 1
    :param mylist:
    :return:
    time complexity : 2*nlogn + n = O(nlogn)
    """

    start_list = merge_sort_interval(mylist,0)
    end_list = merge_sort_interval(mylist,1)

    cur_end = 0
    result = 0
    for i in range(len(start_list)):
        if start_list[i][0] < end_list[cur_end][1]:
            result += 1
        else:
            cur_end += 1
    return result


def major_element(mylist):
    if len(mylist) < 2:
        return

    candidate = [mylist[0],1]
    for i in range(1, len(mylist)):
        if candidate[1] == 0:
            candidate = [mylist[i],1]
            continue
        if mylist[i] == candidate[0]:
            candidate[1] += 1
        else:
            candidate[1] -= 1
    return candidate[0]

