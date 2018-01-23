from collections import deque
import heapq

class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] \
                                for row in range(V)]


class GraphNode():
    def __init__(self):
        self.val = None
        self.neighbors = None

# BFS1 : BiPartie using queue
# def bipartie(myGraph):

# BFS 2: using priority queue => we need breadth first search and meanwhile, everytime we need to pop the min value
# def dijkstra_adjMat_iterative(targetNode,adjMat):
#     """
#
#     :param targetNode: the start node
#     :param adjMat: adjMat that uses to represent the graph
#     :return: list with length of number of node in the graph, in which element is the (shortestPath_to_targetNode,nodeName)
#     actually, we could treat for each of the node in graph, iterative other nodes to find the shortest possibility
#     so the time complexity is O(N^2) by iteration
#     """
#     costList = {}
#     costList[targetNode] = 0
#     traversed = set()
#     for node1 in range(len(adjMat)):
#         for node2 in range(node1 + 1,len(adjMat[targetNode])):
#             if node2 == targetNode or adjMat[targetNode][node2] == 0:
#                 continue
#             if node2 not in traversed:
#                 traversed.append(node2)
#                 costList[node2] = adjMat[targetNode][node2]
#             else:
#                 if costList[node] >

def dijkstra_adjMat_minheap(targetNode,adjMat): # has bug
    """

    :param targetNode: the start node
    :param adjMat: adjMat that uses to represent the graph
    :return: list with length of number of node in the graph, in which element is the (shortestPath_to_targetNode,nodeName)
    actually, we could use min heap ,as Laioffer lecture described.
    assuming V is number of Node, E is number of Edges
    we would have O(VN)*log(V) as time complexity
    """
    pq = [(0,targetNode)]
    costList = {}
    traversed = set()
    while len(pq) > 0:
        cur_pop = heapq.heappop(pq)
        costList[cur_pop[1]] = cur_pop(0)
        traversed.add(cur_pop[1])
        for node in range(len(adjMat[cur_pop[1]])):
            if node in traversed or adjMat[cur_pop[1]][node] == 0:
                continue
            shortest_possible = cur_pop[1] + adjMat[cur_pop[1]][node]
            if node in zip(*pq)[1]:
                if shortest_possible < [item for item in pq if item[1] == node][0]:
                    pq = [item if item[1] != node else (shortest_possible,node) for item in pq]
                    heapq.heapify(pq)
            else:
                heapq.heappush(pq,(shortest_possible,node))
    return costList


def kth_smallest_sort_matrix(myMat,k):
    """
    :param myMat: a sorted matrix (row and col is sorted, the whole matrix does not need to be sorted)
    :return:the kth smallest element

    using bfs2 (priority queue), everytime pop one from heap, and push the 2 neighbors in to the heap
    the element that was popped at the kth time was the answer

    to avoid dup neighbor problem, we use an other matrix to save the element that has been visited
    assuming the matrix has at least k elements
    """
    if len(myMat) < 1 or len(myMat[0]) < 1:
        return None
    if k >= len(myMat)*len(myMat[0]):
        return myMat[len(myMat) - 1][len(myMat[0]) - 1]
    scanMat = [[True for i in range(len(myMat[0]))] for j in range(len(myMat))]
    myheap = [(myMat[0][0],(0,0))]
    heapq.heapify(myheap)
    scanMat[0][0] = False
    i = 1
    result = None
    while i <= k:
        result = heapq.heappop(myheap)
        cur_idx = result[1]
        if scanMat[cur_idx[0]][cur_idx[1] + 1]:
            heapq.heappush(myheap,(myMat[cur_idx[0]][cur_idx[1] + 1],(cur_idx[0],cur_idx[1] + 1)))
            scanMat[cur_idx[0]][cur_idx[1] + 1] = False
        if scanMat[cur_idx[0] + 1][cur_idx[1]]:
            heapq.heappush(myheap,(myMat[cur_idx[0] + 1][cur_idx[1]],(cur_idx[0] + 1,cur_idx[1])))
            scanMat[cur_idx[0] + 1][cur_idx[1]] = False
        i += 1
    return result[0]


def subset_of_unique_dfs(mylist):
    """
    :param list: a list of char first assuming the element in the list is unique
    :return: list of subset of the input list
    we could treated as tree, with ith level represent the ith element is selected or not (binary tree)
    when we reach the leafnode of the tree, append the result
    so we need to track the level of the tree where we currently at
    """
    def helper(thelist, level, curResult,result):
        print("at level ",level, "curResult is ",curResult)
        if level == len(thelist):
            result.append(list(curResult))
            return

        helper(thelist,level + 1,curResult,result)
        curResult.append(thelist[level])
        helper(thelist,level + 1,curResult,result)
        curResult.pop()
    result_list = []
    helper(mylist, 0,[],result_list)
    return result_list



def subset_of_dup_dfs(mylist):
    """
    :param list: a list of char first assuming the element in the list may not be unique
    :return: list of subset of the input list
    we could build a dictionary to save the frequency
    and append 0, 1,2,...freq of each item
    """
    # build dict to save the freq
    mydict = {}
    for item in mylist:
        if item in mydict:
            mydict[item] += 1
        else:
            mydict[item] = 1
    keys = mydict.keys()

    def helper(thedict,level, curResult,result):
        if level == len(mydict):
            result.append(list(curResult))
            return
        for i in range(mydict[keys[level]] + 1):
            curResult += [keys[level]]*i
            helper(thedict,level + 1,curResult,result)
            curResult[len(curResult) - i:len(curResult)] = []
    result_list = []
    helper(mydict, 0,[],result_list)
    return result_list

    

def permutation_unique_dfs(mylist):
    """

    :param list: a list of unique char
    :return: list of list where each sublist is a permutation of the given list
    think it as at every level, we could swap(list[level],list[level+ i]) for i in 1:len(list) - level - 1
    time n*(n-1)*(n-2)...*1 , as the split decrease for 1 for every level increase by 1
    """
    if len(mylist) < 1:
        return

    final_result = []

    def helper(mylist,level,result):
        if level == len(mylist) - 1:
            result.append(list(mylist))
            return
        helper(mylist,level+1,result)
        for i in range(level+1,len(mylist)):
            mylist[level],mylist[i] = mylist[i],mylist[level]
            helper(mylist,level+1,result)
            mylist[level],mylist[i] = mylist[i],mylist[level]

    helper(mylist,0,final_result)
    return final_result


def permutation_dup_dfs(mylist):
    """

    :param list: a list of unique char
    :return: list of list where each sublist is a permutation of the given list
    different with no duplication is
    1. if the swapped elements are the same, then don't swap
     => at each iteration before swap, check mylist[level+i] != mylist[level]
    2. if any of the element's duplication has been swapped, then don't swap
    => use a set to document which element has been swapped at cur level

    """
    if len(mylist) < 1:
        return
    final_result = []

    def helper(mylist,level,result):
        if level == len(mylist) - 1:
            result.append(list(mylist))
            return
        helper(mylist,level+1,result)
        myset = set()
        for i in range(level+1,len(mylist)):
            if mylist[i] not in myset and mylist[i] != mylist[level]:
                myset.add(mylist[i])
                mylist[level],mylist[i] = mylist[i],mylist[level]
                helper(mylist,level+1,result)
                mylist[level],mylist[i] = mylist[i],mylist[level]
            else:
                continue
    helper(mylist,0,final_result)
    return final_result


def valid_parenthesis(n):
    """
    output the possible combination
    :return: list of possible combination
    there are 2*n levels in the recursion tree. Each level determines one position
    with restriction applied here that ) need to come after (, so when we put ) the result, we need to make sure
    the number of ( is larger than the number of )
    time complexity: O(4^n) space: O(n)

    """
    final_result = []

    def helper(n,n_left,n_right,level,curResult,result):
        if level == 2*n:
            result.append(list(curResult))
            return
        if n_left > 0:
            curResult[level] = '('
            helper(n,n_left - 1,n_right,level + 1,curResult,result)
        if n_right > n_left:
            curResult[level] = ')'
            helper(n,n_left,n_right - 1, level + 1,curResult,result)


    helper(n,n,n,0,[0]*2*n,final_result)
    return final_result


def valid_if_block(n):
    comb = []

    def helper(n,n_left,n_right,level,curResult,result):
        if level == 2*n:
            result.append(list(curResult))
            return
        if n_left > 0:
            curResult[level] = '{'
            helper(n,n_left - 1,n_right,level + 1,curResult,result)
        if n_right > n_left:
            curResult[level] = '}'
            helper(n,n_left,n_right - 1, level + 1,curResult,result)

    helper(n,n,n,0,[0]*2*n,comb)

    def print_comb(myComb):
        indent = 0
        for item in myComb:
            if item == '{':
                if indent == 0:
                    print 'if {'
                    indent += 2
                else:
                    print '\n' + ' '*indent + 'if {'
                    indent += 2
            if item == '}':
                print '\n' + ' '*indent + '}'
                if indent > 0:
                    indent -= 2
        return

    for mycomb in comb:
        print_comb(mycomb)
    return




def coin_combination(target,coins):
    """

    :param target: total amount of coin
    :param coins: available coins type 1 cent, 5 cent, 10 cent 25 cent....
    :return: list of list with each sublist is a combination

    using a dfs, where each level represents each type of coin, the number of split would be how many coins it could be filled
    time complexity: there are 4 level in the recursion tree,each level at most has 99 target split (when all filled with 1 cents)
    so the time complexity is O (target^level), with space complexity of the call stack is O(level)
    """
    final_result = []
    def helper(target,coins,level,curResult,result):
        if level == len(coins) - 1: # last level all filled with 1 cents
            curResult[level] = target
            result.append(list(curResult))
            return
        possible = target/coins[level]
        for i in range(possible + 1):
            remain = target - coins[level] * i
            curResult[level] = i
            helper(remain,coins,level + 1,curResult,result)
    helper(target,coins,0,[0,0,0,0],final_result)

    return final_result


def copy_graph_bfs(node):
    """
    given a fully connected graph
    using bfs to copy the node
    expand node, generate its neighbors
    fit for the graph that is deep not wide (so dfs is more likely to overflow than bfs)
    for each generated node, if not exist in visited queue/hashmap, add to queue and add to hashmap

    """
    if node is None:
        return
    mydict = {}
    myqueue = deque([])
    myqueue.append(node)
    while len(myqueue) > 0:
        cur_node = myqueue.popleft()
        if cur_node not in mydict: # cur node hasn't been copied yet
            cur_node_copy = GraphNode()
            cur_node_copy.val = cur_node.val
            cur_node_copy.neighbors = cur_node.neighbors
            mydict[cur_node] = cur_node_copy
            for neighbor_node in cur_node.neighbors:
                myqueue.append(neighbor_node)
        else:
            continue
    return mydict.values()[0]


def copy_graph_dfs(node,lookup):
    """
    given a fully connected graph
    using dfs to copy the node
    using recursion
    fit for the graph that is wide not deep (so bfs is more likely to overflow than dfs)
    :return:
    """
    if node is None:
        return
    if node in lookup:
        return lookup[node]
    copy_node = GraphNode()
    copy_node.val = node.val
    lookup[node] = copy_node
    for neighbor in node.neighbors:
        copy_node.neighbor.append(copy_graph_dfs(neighbor,lookup))
    return copy_node


if __name__ == "__main__":
    myCostMat = [[0,1,0,0,1,0],[1,0,1,0,1,0],[0,1,0,1,0,0],[0,0,1,0,10,1],[0,0,0,1,0,0]]
    root = GraphNode()
    node1 = GraphNode()
    node2 = GraphNode()

    root.val = 0
    node1.val = 1
    node2.val = 2
    root.neighbors = [node1]
    node1.neighbors = [node2]
    node2.neighbors = [root]
    print("test copy_graph_bfs", copy_graph_bfs(root))
