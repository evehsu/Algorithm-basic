def fb_recur(n):
    # function has been called 2 times so the recursion tree as 2 split at each level each node
    # the time complexity will be O(2^n) (# of node in the bottom level)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fb_recur(n-1) + fb_recur(n-2)

## by comparison, use dp to solve the same problem could save time by reducing O(2^n) to O(n)
def fb_dp(n):

    # using n space to create another list to save tmp result to avoid repeated work
    fb_list = [0] * (n+1)
    fb_list[0] = 0
    fb_list[1] = 1
    for i in range(2,n + 1):
        fb_list[i] = fb_list[i-1] + fb_list[i-2]
    return fb_list[n]


def power_recur(a,b):
    # return a^b assuming a > 0, b >= 0
    if b == 0 :
        return 1
    elif b % 2 == 0:
        half = power_recur(a,b/2)
        return half * half
    else:
        half = power_recur(a,b/2)
        return half * half * a

def n_queen_find1(n):
    answer = [-1] * n
    def dfs(depth,answer):
        if depth == n:
            print ("cur valid answer is ",answer)
            return answer
        else:
            for colNum in range(n): # check every col at cur depth
                if is_safe(depth,colNum,answer):
                    answer[depth] = colNum
                    # print ("now the answer is ", answer)
                    # print ("now depth move to ", depth + 1)
                    if dfs(depth + 1,answer): #false i.e None for failed dfs
                        return answer

    def is_safe(i,j,answer_cur):
        # given current queen placement , could we place the ith queen (at row i) at the col j
        for prerow in range(i):
            if answer_cur[prerow] == j or abs(prerow - i) == abs(answer_cur[prerow] - j):
                return False
        return True

    return dfs(0,answer)

def n_queen_findall(n):
    answer = [-1] * n
    finalAnswer = []
    def dfs(depth,answer):
        if depth == n:
            print ("cur valid answer is ",answer)
            finalAnswer.append([i for i in answer])
            print ("after appending final answer is ", finalAnswer)
            return
        else:
            for colNum in range(n): # check every col at cur depth
                if is_safe(depth,colNum,answer):
                    answer[depth] = colNum
                    # print ("now the answer is ", answer)
                    # print ("now depth move to ", depth + 1)
                    dfs(depth + 1,answer)

    def is_safe(i,j,answer_cur):
        # given current queen placement , could we place the ith queen (at row i) at the col j
        for prerow in range(i):
            if answer_cur[prerow] == j or abs(prerow - i) == abs(answer_cur[prerow] - j):
                return False
        return True
    dfs(0,answer)
    return finalAnswer


if __name__ == "__main__":

    # print ("test fb_recur that fb 4 is ", fb_recur(4))
    # print ("test fb_dp that fb 4 is ", fb_dp(4))
    # print ("test pow_recur that fb 4 is ", power_recur(2,3))
    myMatrix = [range(1,17)[i:i+4] for i in range(0,16,4)]
    #print ("test nqueen 1 solution of n == 4 ", n_queen_find1(4))
    #print ("test nqueen all solution of n == 4 ", n_queen_findall(4))




