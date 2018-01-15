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




if __name__ == "__main__":
    mystr1 = "   love   Is   Blind   "
    mystr2 = "stuudent"
    myChar = "u"
    print(removeChar(mystr2,myChar))
    print(removeNoUseSpace(mystr1))