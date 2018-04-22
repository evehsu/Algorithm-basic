from collections import deque


def remove_char(mystr,mychar):
    mylist = list(mystr)
    slow = 0
    fast = 0
    while fast < len(mylist):
        if mylist[fast] == mychar:
            fast += 1
        else:
            mylist[slow] = mylist[fast]
            slow += 1
            fast += 1
    return ''.join(mylist[:slow])


def removeNoUseSpace(string):
    # slow pointer i: all the letters not including i were processed letters
    # fast pointer j: is the cur_pointer
    # [i.j] inclusive in nothing important
    stringList = list(string)
    wordCount = 0
    i = 0
    j = 0
    while(j < len(stringList)):
        if wordCount == 0:
            # remove leading spaces
            if stringList[j] == ' ':
                 j += 1
            else:
            # copy first word
                while j < len(stringList) and stringList[j] != ' ':
                    stringList[i],stringList[j] = stringList[j],stringList[i]
                    i += 1
                    j += 1
                wordCount += 1
        else:
            # remove between spaces
            if stringList[j] == ' ':
                 j += 1
            # keep only one space and copy word
            else:
                stringList[i] = ' '
                i += 1
                while j < len(stringList) and stringList[j] != ' ':
                    stringList[i],stringList[j] = stringList[j],stringList[i]
                    i += 1
                    j += 1
                wordCount += 1
    resultList = stringList[:i]
    return ''.join(resultList)


def string_dedup(mystr):
    mylist = list(mystr)
    slow = 0
    fast = 1
    while fast < len(mylist):
        if mylist[slow] == mylist[fast]:
            fast += 1
        else:
            slow += 1
            mylist[slow] = mylist[fast]
            fast += 1
    print fast
    return ''.join(mylist[:slow+1])


def dedupRepeat(string): # has bug
    """
    :param string: original string
    :return: string after dedup repeatedly. "abbbaccz" => "z"
    """
    stringList = list(string)
    i = 0
    j = 1
    resultList = deque([stringList[i]])
    while j < len(stringList):
        dup = False
        # when we have repeated char, move faster pointer to the end of repeat
        if stringList[i] == stringList[j]:
            j += 1
            dup = True
        # when repeat end, we need to remove the repeat char from resultlist before append a different char
        # reset the slow pointer to the new char
        if stringList[i] != stringList[j] and dup == True:
            resultList.pop()
            resultList.append(stringList[j])
            i = j
            j += 1
            dup = False
        # when there is no repeated pattern,we need to check whether there it would cause another dup with resultList
        if stringList[i] != stringList[j] and dup == False:
            if resultList[-1] != stringList[i]:
                resultList.append(stringList[i])
            else:
                resultList.pop()
                resultList.append(stringList[j])
            i = j
            j += 1
    return ''.join(resultList)


def string_finding(string,pattern): # no bug but may need to simplify
    """

    :param string: original string
    :param pattern: pattern needed to be matched
    :return: if match exists, return the index, otherwise return -1
    """
    string_list = list(string)
    pattern_list = list(pattern)
    # i : every possible start
    # j : char index in pattern
    i = 0
    j = 0
    result_list = []
    while i + j < len(string_list):
        print (string_list[i],pattern_list[j])
        if string_list[i] == pattern_list[j]:
            while j < len(pattern_list) and i + j < len(string_list):
                if string_list[i + j] != pattern_list[j]:
                    break
                else:
                    j += 1
            if j == len(pattern_list):
                result_list.append(i)
                i += j
                j = 0
            else:
                i += 1
                j = 0
        else:
            i += 1
    if len(result_list) < 1:
        result_list = -1
    return result_list



def string_replace(string,pattern,replace): # has bug
    """

    :param string: original string
    :param patthen: the string that need to be replaced
    :param replace: string that used to replace
    :return:
    """
    # slow faster pointer
    stringList = list(string)
    patternList = list(pattern)
    replaceList = list(replace)
    p_len = len(patternList)
    r_len = len(replaceList)

    occrIndex = string_finding(string,pattern)
    occrTime = len(occrIndex)
    if p_len < r_len: # if replaced string is longer than searched pattern, we need to paste space to accommodate that
        stringList = stringList + occrTime * [' ']
    print stringList
    print patternList
    print replaceList
    slow = len(stringList) - 1
    fast = len(stringList) - 1 - occrTime
    while fast >= len(patternList) - 1:
        if stringList[(fast - p_len + 1):(fast + 1)] == patternList:
            for i in range(r_len - 1,-1,-1):
                stringList[slow] = replaceList[i]
                slow -= 1
                fast -= 1
        else:
            stringList[slow] = stringList[fast]
            slow -= 1
            fast -= 1
    return ''.join(stringList)



def str_encoding(string): # no bug but need to simplify and optimize
    """

    :param string:
    :return: aaaabccddaa => a4b1c2d2a2
    trick : cannot say a6 therefore cannot simply hashtable
            pay attention to occurance of 1, that will cause enlarge the capacity of the string
    solution: when it may need enlarge the capacity of the string, we need to add additional space to the end of string before iteration
            it is only safe to iterate string when the new string size is equal or smaller than original string with inplace manipulation
            so we need to iterate twice for inplace manipulation
            1st time, aaaabccddaa => a4bc2d2a2 and keep a counter to count single char, which would indicate the addional required spacds
            2nd time, from right - left, if char digit is not coming in pairs, we will insert 1
    space O(1), time O(N)
    """
    stringList = list(string)
    singleCount = 0
    curChar = stringList[0]
    count = 0
    slow = 0
    fast = 0
    while fast < len(stringList):
        if curChar == stringList[fast]:
            count += 1
            if fast == len(stringList) - 1 and count == 1:
                singleCount += 1
                break
            elif fast == len(stringList) - 1 and count > 1:
                break
            else:
                fast += 1
        else:
            stringList[slow] = curChar
            curChar = stringList[fast]
            slow += 1
            if count == 1:
                singleCount += 1
            else:
                stringList[slow] = str(count)
                slow += 1
            count = 0
    stringList[slow],stringList[slow + 1] = stringList[fast],str(count)
    slow += 2
    fast = len(stringList) - 1
    stringList = stringList[:slow] + singleCount * [' ']
    slow = len(stringList) - 1
    while fast >= 1:
        if stringList[fast].isdigit() and stringList[fast - 1].isalpha():
            stringList[slow] = stringList[fast]
            stringList[slow - 1] = stringList[fast - 1]
            fast -= 2
            slow -= 2
        elif stringList[fast].isalpha() and stringList[fast - 1].isalpha():
            stringList[slow] = str(1)
            stringList[slow - 1] = stringList[fast]
            fast -= 1
            slow -= 2
    if fast == 0:
        stringList[slow] = str(1)
        stringList[slow - 1] = stringList[fast]
    return ''.join(stringList)


def str_reversal_iter(string):
    stringList = list(string)
    i = 0
    j = len(stringList) - 1
    while (i < j):
        stringList[i],stringList[j] = stringList[j],stringList[i]
        i += 1
        j -= 1
    return ''.join(stringList)


def str_reversal_recur(string):
    stringList = list(string)
    if len(stringList) == 1:
        return stringList
    else:
        stringList[0],stringList[len(stringList) - 1] = stringList[len(stringList) - 1],stringList[0]
        return str_reversal_recur(stringList[1:len(stringList)-1])


def reverse_word_order(string):
    """
    :param string:I love yahoo
    :return: yahoo love I
    solution: reverse the whole string : I love yahoo => oohay evol I
    and reverse each word
    """
    def my_str_reversal_iter(stringList):
        i = 0
        j = len(stringList) - 1
        while (i < j):
            stringList[i],stringList[j] = stringList[j],stringList[i]
            i += 1
            j -= 1
        return stringList
    stringList = list(string)
    stringList = my_str_reversal_iter(stringList)
    fast = 0
    slow = 0
    while (fast < len(stringList)):
        if stringList[fast] != ' ':
            fast += 1
        else:
            stringList[slow:fast] = my_str_reversal_iter(stringList[slow:fast])
            fast += 1
            slow = fast
    return ''.join(stringList)

#########################    string with sliding window and hash_table
def longest_unique(string):
    """
    :param string:
    :return:substring which contains longest unique chars in the original string
    since it is require char count, we need to use a dict to save char freq
    we have two pointer slow and fast
    fast is the end cur unique string while slow is the start of the cur unique string
    create global_max and final_solution, where global_max is the length of longest unique string and final_solution is
    the slow and fast for longest string. They should be updated together
    """
    stringList = list(string)
    dict = {}
    fast = 0
    slow = 0
    global_max = 0
    final_solution = [0,0]
    while fast < len(stringList):
        if stringList[fast] not in dict:
            dict[stringList[fast]] = 1
            if global_max < fast - slow + 1:
                global_max = fast - slow + 1
                final_solution[0] = slow
                final_solution[1] = fast

        else:
            while stringList[fast] in dict:
                dict.pop(stringList[slow],None)
                slow += 1
        fast += 1
    return final_solution

def find_1st_nonDup_char(myStr):
    """
    given a string, find the first non repeating string
    for example: GeeksForGeeks: F: GeeksForMe: G
    worst solution: 1. scan the string and save the count in a dict
    2. scan the string a again, and look up into the dict , return the char when first time found count ==1
    above is the worst solution because it needs to scan the array 2 twice

    Better solution: 1. scan the string the save the count as well as the first position in a dict
    so dict's key is char:(count,pos)
    2. only scan the dict
    it could save more time when the string has lot of dups, as it only need to scan the string once
    :param myStr:
    :return:
    """
    mylist = list(myStr)
    dict = {}
    for i in range(len(mylist)):
        if mylist[i] in dict:
            dict[mylist[i]][0] += 1
        else:
            dict[mylist[i]] = [1,i]
    for k,v in dict.iteritems():
        if v[0] == 1:
            return k
        else: continue
    return -1


def longest_common_prefix(listofstr):
    """
    givena list of str, get the longest common prefix for those strs
    :param
    :return: the commom prefix str
    solution: 1. find the shortest length of given strings, say the length is min_Len
    2. for i in range(min_len): i iterate the chars in the min length string
            for j in range(len(listOfStr0)): j index is the jth string we have

            if come across something different, stop and return
    """
    minlen = float("inf")
    for i in range(len(listofstr)):
        minlen = min(minlen,len(listofstr[i]))
    result = []
    for j in range(minlen):
        cur_char = listofstr[0][j]
        for k in range(1,len(listofstr)):
            if listofstr[k][j] != cur_char:
                break
        result.append(cur_char)
    return ''.join(result)





def longest_common_substr(str1, str2):
    """
    different from longest common prefix, this requires the common substr not only from beginning(prefix)
    but also from middle/end part
    this requires 1. scan 2 array from beginning to end 2. save intermediate result
    so dp : m[i][j] = common_substr between string1 cutting of by the ith string1[0:i] and string2 cutting of by jth string2[0:j],
    base case m[0][0] = 1 if string1[0] ==  string2[0], otherwise 0
    induction m[i][j] = m[i-1][j-1] + 1 if string1[i] = string2[j],otherwise 0 (because it is substring not subsequence),
    which requires the common char need to be continuous, so once not continous, we need to restart (reset to 0)

    finally scan over m and find the max

    :param listOfstr:
    :return:
    """
    list1 = list(str1)
    list2 = list(str2)

    # build basecase
    m = [[0 for i in range(len(list1))] for j in range(len(list2))]
    for i in range(len(m[0])):
        if list1[i] == list2[0]:
            m[0][i] = 1
    for j in range(len(m)):
        if list2[j] == list1[0]:
            m[j][0] == 1
    print m
    # build induction rule
    for i in range(1,len(m[0])):
        for j in range(1,len(m)):
            if list1[i] == list2[j]:
                m[j][i] = m[j-1][i-1] + 1
    print m
    # find global_max
    global_max = 0
    for i in range(len(m[0])):
        for j in range(len(m)):
            global_max = max(global_max,m[j][i])

    return global_max


def longest_common_seq(str1,str2):
    """
    different from substr, now the common part is not required to be continuous, even though still require
    to be in the same order. So we could modify the induction rule as
    m[i][j] = m[i-1][j-1] + 1 if s1[i] = s2[j], otherwise max(m[i-1][j],m[i-1][j-1],m[i][j-1]), which is max(m[i-1][j],m[i][j-1])
    :param str1:
    :param str2:
    :return:
    """
    list1 = list(str1)
    list2 = list(str2)

    m = [[0 for i in range(len(list1))] for j in range(len(list2))]
    # base case
    if list1[0] == list2[0]:
        m[0][0] = 1
    for i in range(1,len(m[0])):
        if list1[i] == list2[0]:
            m[0][i] = 1
        else:
            m[0][i] = m[0][i-1]
    for j in range(1,len(m)):
        if list2[j] == list1[0]:
            m[j][0] = 1
        else:
            m[j][0] = m[j-1][0]

    print m
    # induction rule
    for i in range(1,len(m[0])):
        for j in range(1,len(m)):
            if list1[i] == list2[j]:
                m[j][i] = m[j-1][i-1] + 1
            else:
                m[j][i] = max(m[j-1][i],m[j][i-1])
    print m
    global_max = 0
    for i in range(len(m[0])):
        for j in range(len(m)):
            global_max = max(global_max,m[j][i])

    return global_max


def first_nonrepeat_char(myStream):
    """
    given an unlimited stream of chars, report the first non repeat char at anytime using O(1)
    use a dict and a queue
    dict is used for saving the char and count
    queue save the char as iteration from myStream ,queue[0] will be the answer
    if we found queue[0] has freq > 1, then pop queue until queue[0] is freq == 1 again
    :param myStream:
    :return:
    """
    mydict = {}
    myque = deque([])
    for item in myStream:
        if item in mydict:
            mydict[item] += 1
        else:
            mydict[item] = 1
        myque.append(item)
        while myque and mydict[myque[0]] > 1:
            myque.popleft()
    return myque[0]

def find_char_dup_overhalf(mylist):
    """
    given a list with duplicates, we know some unknown char is taking over a half of the list,
    how to identify the unknown char?

    maintain a pair of (candidate, counter), and iterate the list
    when counter > 0
    if new item != candidate, counter --, otherwise counter ++
    when counter == 0, reset (candidate, counter)
    :param mylist:
    :return:
    """
    if len(mylist) < 2:
        return
    candidate = [mylist[0],1]
    for i in range(1,len(mylist)):
        if candidate[1] == 0:
            candidate = [mylist[i],1]
        elif candidate[0] != mylist[i]:
            candidate[1] -= 1
        else:
            candidate[1] += 1
    return candidate[0]


if __name__ == "__main__":
    mystr1 = "   love   Is   Blind   "
    mystr2 = "stuudent"
    myChar = "u"
    print(remove_char(mystr2,myChar))
    print(removeNoUseSpace(mystr1))