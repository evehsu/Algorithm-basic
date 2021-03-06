
"""
best buy stocks
"""

def bestBuyStock_infinity(mylist):
    # if allows unlimited number of transection
    # we could just scan/iterate once of the array and aggregate if array[i+1] > array[i]
    # we iterate the array once so the time complexity is O(N)
    if len(mylist) < 2 or mylist is None:
        print ("price list should have at least 2 element,method did not execute")
        return
    profit = 0
    for i in range(len(mylist) - 1):
        if mylist[i+1] > mylist[i]:
            profit += mylist[i+1] - mylist[i]
    return profit

def bestBuyStock_once(mylist):
    # originally we hope we could find the max and min with condition of max is appeared after min
    # if scan once ,we could keep the cur min max for scanned area,
    # if next element is larger than global max we need to update global max,
    # if smaller than global min , update global min the max profit will be affected too
    # therefore, we may use dp
    # d[i] is equal to the max profit we have when we scan element i => [0,i]
    # rule: d[i+1] = max(d[i],array[i+1] - globalmin)
    # have scan the array once, so time complexity is O(N)
    if len(mylist) < 2 or mylist is None:
        raise ValueError("price list should have at least 2 elements")
    d = [0]*len(mylist) # d need to start with 0, meaning at the beginning the profit is zero
    global_min = mylist[0]
    for i in range(1,len(mylist)):
        d[i] = max(d[i-1],mylist[i] - global_min)
        if mylist[i] < global_min:
            global_min = mylist[i]
    return d[-1]

def bestBuyStock_twice(mylist):
    # similarly as we did for stock trade once, we could still use dp
    # d[i] is the max profit with first transection in [0,i] an the second in [i+1,N-1]
    # therefore we need 2 list (1-d dp process twice) to save max[0,i] and max[i+1,N-1]
    # max[0,i] f[i]; max[i+1,N] g[i]
    # f[i+1] = max(f[i],mylist[i+1] - cur_global_min) same as trade once
    # s[i] = max(s[i+1],cur_global_max - mylist[i])
    # have iterate 3 times on length n list, so time complexity is O(3N) ,which is O(N)
    if len(mylist) < 2 or mylist is None:
        raise ValueError("price list should have at least 2 elements")
    first_half_min = mylist[0]
    second_half_max = mylist[-1]
    f = [0] * len(mylist)
    s = [0] * len(mylist)
    final = [0] * len(mylist) # need to create three reference independently

    for i in range(1,len(mylist)):
        f[i] = max(f[i-1],mylist[i] - first_half_min)
        if mylist[i] < first_half_min:
            first_half_min = mylist[i]
    for j in range(len(mylist)-2,-1,-1):
        s[j] = max(s[j+1],second_half_max - mylist[j])
        if mylist[j] > second_half_max:
            second_half_max = mylist[j]
    final[0] = f[0] + s[0]
    print f
    print s
    print final
    for m in range(1,len(mylist)):
        final[m] = max(final[m-1],f[m] + s[m])
    return final[-1]


def bestBuyStock_twice_optimize(mylist):
    # based on bestBuyStock_twice, we compress the time complexity is O(2N), which is still O(N)
    if len(mylist) < 2 or mylist is None:
        raise ValueError("price list should have at least 2 elements")
    first_half_min = mylist[0]
    second_half_max = mylist[-1]
    f = [0] * len(mylist)
    s = [0] * len(mylist)
    final = [0] * len(mylist) # need to create three reference independently

    for i in range(1,len(mylist)):
        f[i] = max(f[i-1],mylist[i] - first_half_min)
        if mylist[i] < first_half_min:
            first_half_min = mylist[i]
        s[len(mylist) - i - 1] = max(s[len(mylist) - i], second_half_max - mylist[len(mylist) - i - 1])
        if mylist[len(mylist) - i - 1] > second_half_max:
            second_half_max = mylist[len(mylist) - i - 1]
    final[0] = f[0] + s[0]
    print f
    print s
    print final
    for m in range(1,len(mylist)):
        final[m] = max(final[m-1],f[m] + s[m])
    return final[-1]


def climbing_stairs(n):
    """
    given n stairs, we could take either 1 or 2 steps every time
    how many distinct ways to reach top
    induction rule
    d[n] = d[n-1] + d[n-2]
    d[0] = 0 useless
    d[1] = 1
    d[2] = 2
    """
    if n < 1:
        return
    if n == 1:
        return 1
    if n == 2:
        return 2
    tmp1 = 1
    tmp2 = 2
    for i in range(3,n + 1):
        cur = tmp1 + tmp2
        tmp1,tmp2 = tmp2,cur
    return cur


def longest_ascending_subarray(mystr):
    mylist = list(mystr)
    global_max = 0
    m = [1] * len(mylist)
    for i in range(1,len(mystr)):
        if mylist[i] > mylist[i - 1]:
            m[i] = m[i - 1] + 1
            global_max = max(global_max, m[i])
    return global_max


def longest_ascending_subarray_saveSpace(mystr):
    mylist = list(mystr)
    global_max = 1
    cur = 1
    for i in range(1,len(mystr)):
        if mylist[i] > mylist[i - 1]:
            follow = cur + 1
            global_max = max(global_max, follow)
            cur = follow
        else:
            cur = 1
    return global_max


def longest_ascending_subseq(mylist):
    """
    ascending subsequence is not continuous stored (difference with ascending subarray)
    [10, 9, 2, 5, 3, 7, 101, 18] => [2, 3, 7, 101]
    2 nested for loop result in time complexity of O(n^2)
    :param mylist:
    :return: longest subsequence length
    """
    # m[i] stopping by index i what is the longest sequence length
    m = [1] * len(mylist)
    global_max = 1
    for i in range(1,len(mylist)):
        for j in range(i):
            if mylist[i] > mylist[j]:
                tmp = m[j] + 1
                if tmp > m[i]:
                    m[i] = tmp
        if m[i] > global_max:
            global_max = m[i]
    return global_max


def longest_ascending_subseq_saveTime(mylist):
    """
    still solve longest scending subsequence,but
    for the inner loop, using binary search , so total time is O(nlogn)
    the trick is during scanning, we need to save <val,ascending_seq_len>, for given value,
    what is the max ascending_seq_len so far containing this value
    if there are two val share the same ascending_seq_len, <val1, ascending_seq_len> <val2,ascending_seq_len>
    then we could disregard the larger value (say val2),because for future coming value, as long as it is greater than val1
    it would have ascending_seq_len + 1 as the cur min ascending length
    :param mylist:
    :return:
    """
    def bs_left_closest(mylist,target):
        """
        return the index of the element which is cloest and smaller than target
        :param mylist:
        :param target:
        :return:
        """
        if mylist[0] >= target:
            return -1
        if mylist[-1] < target:
            return len(mylist) - 1
        left = 0
        right = len(mylist) - 1
        while left < right - 1:
            mid = (left + right)/2
            if mylist[mid] >= target:
                right = mid
            if mylist[mid] < target:
                left = mid
        return left

    cur_active = [mylist[0]] # active val in mylist that could decide the future asc seq length
    cur_lgest_asc_seq = [1] # for each element in cur_active, what is the max ascending seq len

    for i in range(1,len(mylist)):
        # fit new coming element in cur_active by applying binary search
        # by finding the cloest smaller element in cur_active
        cur_pos = bs_left_closest(cur_active,mylist[i])
        cur_pssbl_max_len = cur_lgest_asc_seq[cur_pos] + 1
        print cur_active,cur_lgest_asc_seq,mylist[i],cur_pos,cur_pssbl_max_len

        if cur_pos < len(cur_lgest_asc_seq) - 1:
            cur_active[cur_pos + 1] = min(mylist[i],cur_active[cur_pos + 1])
        else:
            cur_active.append(mylist[i])
            cur_lgest_asc_seq.append(cur_pssbl_max_len)
    return cur_lgest_asc_seq[-1]

def largest_sum(mylist):
    # create global_Max and max_ending_here
    max_ending_here = 0
    global_max = 0
    for i in range(len(mylist)):
        max_ending_here = max_ending_here + mylist[i]
        if max_ending_here > global_max:
            global_max = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return global_max


def longest_sum_returnIndex(mylist):
    start = 0
    # end = 0
    final_start = 0
    final_end = 0
    max_ending_here = 0
    global_max = 0
    for i in range(0,len(mylist)):
        max_ending_here = mylist[i] + max_ending_here
        end = i
        if max_ending_here > global_max:
            global_max = max_ending_here
            final_start = start
            final_end = end
        if max_ending_here < 0:
            max_ending_here = 0
            start = i + 1
            # end = i + 1
    return [final_start,final_end]


def longest_1(mylist):
    """
    time: O(N)
    """
    global_max = mylist[0]
    cur_max = mylist[0]
    for i in range(1,len(mylist)):
        if mylist[i] == 1:
            cur_max += 1
            if cur_max > global_max:
                global_max = cur_max
        else:
            cur_max = 0
    return global_max


"""
cutting ropes problem
description: given a rope with length n, and at least gave one cut, finding the maximum value of the multiplication
of the length after cutting
# when length =  1 __
we cannot cut and the multiplication is 1
# when length = 2 __ __
we could only cut into 1 and 1, so the multiplication is still 1 __ | __
# when length is 3 we will have __ __ __
we could have __ __ | __ and __ | __ __, the multiplication is 2, we could see the problem was cut into two pieces
one length 1 and one length 2, for the piece of length 2, it was actually reusing the situation when given a length 2 rope
the only difference is now we allow no cut on the length 2 part (cause there is already one cut)

therefore, the problem could be cut into subproblem => recursion
cut(n) = max(max(n-i,cut(n-i)) * max(i,cut(i)) for i in range(1,n))
the recursion tree will be
           n
/        |      |
1,n-1   2,n - 2 n-1, 1

so we have n level, the node in  first level has n-1 split, and the second level have n-2 split...so time complexity is O(n!)
as in recursion tree, there are a lot of dup node between each level, we meant we had a lot of repeat calculation.
so dp could help to solve this issue

"""
def cut_recur(n):
    if n == 1:
        return 0
    max_product = 1
    for i in range(1,n):
        cur_cut_best = max(n - i, cut_recur(n - i))
        if cur_cut_best * i > max_product:
            max_product = i * cur_cut_best
    return max_product

def cur_dp_1(n):
    # we would use a vector m to save the result
    # m[i] is the max multiplication with length i
    m = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            cur_cut_best = max(j, m[j])
            cur_best = max(m[i],cur_cut_best * (i - j))
        m[i] = cur_best
    return m[n]


def jumping_game(mylist):	# m[i] save whether the ith element could jump to the end
    # as long as the ith element could jump to any place that could jump to the end, it could jump to the end
    m = [False] * len(mylist)
    length = len(mylist)
    m[len(m) - 1] = True
    for i in range(length - 2, -1,-1):
        # could start from i directly jump to the end
        if mylist[i] >= length - i - 1:
            m[i] = True
        # could jump to some place that could jump to the end
        else:
            for j in range(i,i + mylist[i] + 1):
                if m[j] == True:
                    m[i] == True
    return m[0]


def jumping_game_step(mylist):
    """
    return the minimum step of jumping to end
    scan from right to left
    m[i] is starting at the ith position , the minimum number of steps of jumping to end
    :param mylist:
    :return:
    """
    m = [9999] * len(mylist)
    length = len(mylist)
    for i in range(length - 2, -1, -1):
        if mylist[i] >= length - 1 - i:
            m[i] = 1
        else:
            tmp = min(m[i:(i+mylist[i] + 1)])
            m[i] = tmp + 1
    return m[0]


def dict_find_word(mystr,mydict):
    """
    return True if the given string could be cut into words in dictionary
    :param mystr: given string
    :param mydict: given dictionary
    :return: True or False

    generally go through string from left to right, check [0:1],[0:2]...[0:n]
    record the result in a list m, return m[n-1]
    for each [0:i], check [0: i-1] & [i-1:i], [0:i-2] & [i-2:i]... ,[0:1] & [1:i]
    if one of the above combination is okay, then m[i] is true

    time complexity O(N^2) for 2 for loop and O(N) for join char, total O(N^3)
    """
    mystrlist = list(mystr)
    m = [False] * len(mystrlist)
    for i in range(0,len(m)):
        if ''.join(mystrlist[0:(i+1)]) in mydict:
            m[i] = True
        else:
            for j in range(i,0,-1):
                if m[j-1] and ''.join(mystrlist[j:i+1]) in mydict:
                    m[i] = True
                    break
    return m[-1]


def coin_change(coins,amount):
    """
    given a list of coins, find the min # of coins that need to reach the given amount
    using dp
    dp[i] is min # of coins to reach amount i
    basecase dp[i] = 1 if i in coins
    induction rule dp[i] = min(dp[i-j]) + 1 for j in coins
    """
    d = [float("inf")] * (amount + 1)
    for j in coins:
        d[j] = 1
        for i in range(j,amount + 1):
            d[i] = min(d[i],d[i-j] + 1)
    if d[-1] == float("inf"):
        d[-1] = -1
    return d[-1]


"""
2-D DP problem
"""

def edit_distance_recur(str1, str2):
    """

    :param str1:
    :param str2:
    :return: levenshtein distance
    if written in recursive way, the time complexity will be O(3 ^ (m + n))
    """
    # using recur to solve
    list1 = list(str1)
    list2 = list(str2)

    # base case
    if len(list1) == 0:
        return len(list2)
    if len(list2) == 0:
        return len(list1)

    # recursion
    if list1[0] == list2[0]:
        return edit_distance_recur(list1[1:],list2[1:])
    else:
        delete = edit_distance_recur(list1[1:],list2)
        replace = edit_distance_recur(list1[1:],list2[1:])
        insert = edit_distance_recur(list1,list2[1:])
        best = min(delete, replace, insert)
        return best + 1


def edit_distance_dp(str1,str2):
    """
    we could use 2-d matrix to save string match steps from left to right
    m[i][j] is the minimum step change from str1[:i] to str2[:j]
    if we start from empty, (the first match of each string is empty)
    then we can use a (len(str1) + 1) * (len(str2) + 1) matrix to save
      0 a b c d
    0 0 1 2 3 4
    d 1
    f 2
    g 3
    a 4
    above is the base case (where dp start from)
    if replace m[i][j] = m[i - 1][j - 1] + 1
    if insert  m[i][j] = m[i][j - 1] + 1
    if delete  m[i][j] = m[i-1][j] + 1
    now m[i][j] = min(replace, insert, delete)

    :param str1:
    :param str2:
    :return:
    now time complexity is O(m*n)
    """
    list1 = list(str1)
    list2 = list(str2)
    # set up base case
    m = [[0] * (len(list1) + 1) for _ in range(len(list2) + 1)]
    m[0] = range(len(list1) + 1)
    for i in range(len(list2) + 1):
        m[i][0] = i
    for i in range(1,len(list2) + 1):
        for j in range(1,len(list1) + 1):
            m[i][j] = min(m[i-1][j-1], m[i - 1][j], m[i][j-1]) + 1
    return m[len(list2)][len(list1)]


def min_cut_palindome(myStr):
    """
    palindrome: aba|bbabb|aba
    :param myStr:
    :return:
    m[i] min cut for palindome stopping by index i
    similar to find_word_in_dict
    """
    mylist = list(myStr)
    m = range(len(mylist))

    def is_palindome(mylist):
        length = len(mylist)
        init = True
        for i in range(0,length/2):
            if mylist[i] != mylist[len(mylist) -1 -i]:
                init = False
                break
        return init
    m[0] = 0
    m[1] = 0 if mylist[0] == mylist[1] else 1
    for i in range(2,len(m)):
        if is_palindome(mylist[:i+1]):
            m[i] = 0
            continue
        tmp = [m[i]]
        for j in range(1,i+1):
            if is_palindome(mylist[j:i+1]):
                tmp.append(m[j-1])
        print tmp
        m[i] = min(tmp)+1
        print m
    return m[-1]


def min_cut_wood(cutpoint):
    """
    given a piece of wood (length is known) and a series cutting point
    and the cutting cost is decided by the length
    find the cutting order of minimum cost
    the cutpoint would be given as [0,x,x,...len(cutpoint)]

    because cost for each position is not identical, so using dp on the original given array (if wood length is 10,
    the original given array is [0:10] is not working, so linear scan is not working

    we need to think a framework that save the result of minimum cost of each cutting point
    so if given a cutting point is 2,4,7, and length 10
    we could have an array of [0,2,4,7,10]
    we need to find the min cost of [0,2],[0,4]...[2,4],[2,7],[2,10]...[7,10
    as when we looking for cutting [2,10], we could use [2,7] + [7,10] , or [2,4] + [4,10], it is meaningful to save the
    intermediate result

    therefore, we design m[i][j] referring to the mincost of cutting array from ith to jth position of the given current
    array

    :param cutpoint:
    :param woodLength:
    :return: the min cost
    """
    m = [[0 for p in range(0,len(cutpoint))] for q in range(0,len(cutpoint))]
    gapdict = {}
    for i in range(len(m)):
        for j in range(i + 1,len(m[0])):
            # gap between i.j is [0:len(m)], which is 0,1,2,...len(m) - 1
            if j - i in gapdict:
                gapdict[j-i].append((i,j))
            else:
                gapdict[j-i] = [(i,j)]
    for key in gapdict.keys(): # iterate through gap(keys in gapdict) will guarantee that we fill the m in a diagonal way
        for pair in gapdict[key]:
            i = pair[0]
            j = pair[1]
            if j - i == 1:
                continue
            else:
                inter = float("inf")
                for t in range(i+1,j):
                    inter = min(inter,m[i][t] + m[t][j])
                m[i][j] = cutpoint[j] - cutpoint[i] + inter
    return m[0][len(m) - 1]


def mergeStone(stoneList):
    """
    given a stone list(each number means the size of stone) , we want to merge stone with its neighbor till there is
    only one stone, the cost of the merging is the size of the merged stones
    say if we merge stones of size 5 and size 8, merging these 2 stones will have a cost of
    :param stoneList:
    :return:min cost of merge those stones
    this problem is similar with cutting wood for
    1. minimum element(un splittable) cost is different (wood is lenght, while stone is size), which is to say the weight
    is different. Therefore linear scan is not working because the result is different for different approaches
    2. but we could also build a cost matrix to save the result
    in cutting wood, m[i][j] is min cost in cutting the wood from ith cutting point to the jth cutting point position
    (when cost is cuttingpoint[j] - cuttingpoint[i])
    in merging stone, the stonelist is the cuttingpoint, m[i][j] means min cost of merging the ith stone to the jth stone
    """
    m = [[0 for p in range(0,len(stoneList))] for q in range(0,len(stoneList))]
    gapdict = {}
    for i in range(len(m)):
        for j in range(i + 1,len(m[0])):
            # gap between i.j is [0:len(m)], which is 0,1,2,...len(m) - 1
            if j - i in gapdict:
                gapdict[j-i].append((i,j))
            else:
                gapdict[j-i] = [(i,j)]
    for key in gapdict.keys(): # iterate through gap(keys in gapdict) will guarantee that we fill the m in a diagonal way
        for pair in gapdict[key]:
            i = pair[0]
            j = pair[1]
            if j - i == 1:
                m[i][j] = stoneList[i] + stoneList[j]
            else:
                inter = float("inf")
                for t in range(i,j):
                    inter = min(inter,m[i][t] + m[t+1][j])
                m[i][j] = sum(stoneList[i:j+1]) + inter
    return m[0][len(m)-1]


def isPartition(myArr):
    """
    given the array return true if the array could be divided into 2 parts where these 2 parts have equal sum
    :param
    :return:
    so dp[i] is number i could find through some subset, and finally return dp[target] where target = sum(arr)/2
    dp[j] = dp[j - num] for num in array

    time complexity: n * sum (2 level for loops)
    """
    mysum = sum(myArr)
    if mysum & 1: return False # if sum is odd return false
    target = mysum/2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in myArr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]


def min_cut_of_array(mylist,limit):
    """
    given an array, try to find the min # of cut that each piece's sum of cut is smaller than limit
    we could still use zuo da duan you xiao duan
    as for every right part, we could directly check whether the sum of right part < 10
    m[0] = 0 if mylist[0] < limit otherwise m[i] = None
    m[i] = min (m[i-1] + 1, if mylist[i] < limit,None is mylist[i] > limit,
                m[i-2] + 1, if mylist[i-1:i+1] < limit,None is sum(mylist[i-1:i+1]) > limit,
                .
                .
                .)
    return m[-1]
    :param mylist:
    :return:
    """
    if len(mylist) < 1:
        return None
    m = [0] * len(mylist)
    m[0] = 0 if mylist[0] < limit else None
    for i in range(1,len(mylist)):
        if sum(mylist[:i + 1]) < limit:
            m[i] = 0
            continue
        tmp = []
        for j in range(i-1,-1,-1):
            cur = m[j] + 1 if m[j] is not None and sum(mylist[j+1:i + 1]) < limit else None
            if cur is not None:
                tmp.append(cur)
        if len(tmp) == 0:
            m[i] = None
        else:
            m[i] = min(tmp)
    return m[-1]


def pizza_picking_strategy(mylist):
    """
    given a list of integer represensts the size of the pieces of pizza
    and you and your friend take turns to pick pizza from either the head or the tail
    suppose your friend strategy is always taking the bigger one
    what's your best strategy to take pizza in order to have larger size in total
    assuming you start first

    so example 1 5 100 10
    in this case you should take 1 as the begining, then your friend will take 10,and you then take 100 and win
    but if you take 10 first, your friend will take 100 and win

    solution
    using dp that m[i][j] is the largest total you could get from mylist[i:j+1], which is (i,j) inclusively
    base case m[i][i]  = mylist[i]; m[i][i+1] = max(mylist[i],mylist[i + 1])
    induction rule: m[i][j] = case 1: take left, if mylist[i+1] > mylist [j], m[i][j] = mylist[i] + m[i+2][j], else m[i][j] = mylist[i] + m[i+1][j-1]
    case2: take right, if mylist[i] > mylist[j-1], m[i][j] = mylist[j] + m[i+1][j-1], else m[i][j] = mylist[j] + m[i][j-2]
    m[i][j] = max(case1,case2)
    fill m in an diagonal direction
    m matrix is symmetric diagonally, so only need to fill right_top or left_bottom

    :param mylist:
    :return:
    """
    n = len(mylist)
    m = [[0 for i in range(n)] for j in range(n)]
    # build base case
    for idx in range(n): # diff = 0
        m[idx][idx] == mylist[idx]
    for idx in range(1,n): # diff = 1
        m[idx-1][idx] = max(mylist[idx - 1],mylist[idx])
    # induction
    for diff in range(2,n):
        for i in range(0,n-diff):
            # calculate m[i][j] where j = i + diff,  which m[i][i+diff]
            # take left
            j = i + diff
            next_step_left = [0]
            if mylist[i + 1] < mylist[j]:# friend will take mylist[j]
                next_step_left[0] = m[i+1][j-1]
            else:
                next_step_left[0] = m[i+2][j]
            # take right
            next_step_right = [0]
            if mylist[i] > mylist[j-1]:
                next_step_right[0] = m[i+1][j-1]
            else:
                next_step_right[0] = m[i][j-2]
            m[i][j] = max(mylist[i] + next_step_left[0],mylist[j] + next_step_right[0])

    return m[0][n-1]

if __name__ == "__main__":
    testList = [2,4,3,6,9,10,4]
    testList2 = [2]
    testList3 = [5,4,3,2,1]
    testList4 = [-2,-3,4,-1,-2,1,5]
    print("test bestBuyStock_infinity ", bestBuyStock_infinity(testList2))
    print("test bestBuyStock_once ", bestBuyStock_once(testList3))
    print("test bestBuyStock_twice ", bestBuyStock_twice(testList))
    print("test bestBuyStock_twice_optimize ", bestBuyStock_twice(testList))
    print("test longest_ascending ", longest_ascending_array(testList))
    print("test largest_sum) ", largest_sum(testList4))
    print("test longest_ascending_sequence", longest_ascending_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))


