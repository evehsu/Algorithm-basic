from collections import deque
import heapq
import math


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


def place_chair(mat):
    """
    mat has O means obstacle
    E means equipment
    X means empty
    find an X that could be empty
    :param mat:
    :return:
    """