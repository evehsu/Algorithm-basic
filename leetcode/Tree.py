"""
tree problem => recursion
basecase: child is null


Concept
Blanced Tree: the height difference of left subtree and right subtree is no bigger than 1 for every node
Complete Tree: every non-bottom level is completed filled and the last level is filled as left as possible
Binary Search Tree: for every node, the value is larger than the left child's value and smaller than its right child's value
"""
from collections import deque
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
"""
Tree Treversal general

"""
def preOrder(myTree):
    """
    time O(N), n is the number of nodes
    space O(Height), call stack
    """
    if myTree is None:
        return
    print myTree.data
    preOrder(myTree.left)
    preOrder(myTree.right)

def preOrder_iterative(rootNode):
    """

    :param root: root node
    :return: print my preorder
    """
    if rootNode is None:
        return
    stack = deque([rootNode])
    while len(stack) > 0:
        cur = stack.pop()
        print cur.data
        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)
    return

def inOrder(myTree):

    if myTree is None:
        return
    inOrder(myTree.left)
    print myTree.data
    inOrder(myTree.right)


def inOrder_interative(rootNode):
    """

    :param rootNode:
    :return: none, just print
    step1: going down to find the left most leafnode
    step2: if cur.left is null, we need to take it out of stack and print
    step2.1 if the printed node above has right child, we need to going down its right child path
    '''note: that meet with inorder requirement, so if it has left child, we going down to left, when no left child
    or left child has been pri'''
    step2.2: if no right child, we will go back to print its parent and repeat step 2.1
    step3: repeat 2.1 and 2.2 till stack is empty
    """

    if rootNode is None:
        return
    stack = deque([rootNode])
    helper = stack[-1]
    while len(stack) > 0:
        # step 1
        if helper.left is not None:
            stack.append(helper.left)
            helper = helper.left
        # step2
        if helper.left is None: # helper has no left child and cur helper points to the last element of stack
            stack.pop()
            print helper.data
            # 2.1
            if helper.right is not None:
                stack.append(helper.right)
                helper = helper.right
            # 2.1
            while helper.right is None and len(stack) > 0:
                helper = stack.pop()
                print helper.data
            if helper.right is not None:
                stack.append(helper.right)
                helper = helper.right
    return

def postOrder(myTree):

    if myTree is None:
        return
    postOrder(myTree.left)
    postOrder(myTree.right)
    print myTree.data


"""
Tree Traversal special path
leaf-to-leaf
root-to-leaf
any-2-node
"""
def leaf_to_leaf_max(root):
    """
    midterm 2
    :param root:
    :return:
    get from child: left max path , right max path
    current: max(left, right) + curNode.data
    report to parent: max(left, right) + curNode.data
    trick as it requires leaf to leaf: global_max could only be updated when the current node
    has both left or right child
    """
    global_max = [-float("inf")]
    def helper(root, global_max):

        if root is None:
            return 0
        max_left = helper(root.left)
        max_right = helper(root.right)
        if root.left is not None and root.right is not None: # this is the trick
            if max_left + max_right + root.data > global_max:
                global_max[0] = max_left + max_right + root.data
            return max(max_left, max_right) + root.data
        if root.left is None:
            return max_right + root.data
        if root.right is None:
            return max_left + root.data
    helper(root,global_max)
    return global_max[0]


def any_to_any(root):
    """
    find the maximum sum path from any to any (not required to be leaf node)
    difference with leaf to leaf is that we could set sum to 0 for some node if its left sum and right sum < 0
     which is disregard the below nodes (start from the current node)
    :param root:
    :return:
    """
    global_max = [-float("inf")]

    def helper(root, global_max):
        if root is None:
            return 0
        left = max(0,helper(root.left,global_max))
        right = max(0,helper(root.right,global_max))
        global_max[0] = max(left + right + root.data,global_max[0])
        return max(left, right) + root.data
    helper(root, global_max)
    return global_max[0]


def leaf_to_root(root):
    """
    find the maxisum of path where is leaf to root (each level pick one node)
    difference with leaf_to_leaf and any_to_any, the global_max would be possibly updated only we found the sum from root-leaf
    instead of every recursion level
    therefore, only from top to bottom one direction(once touch the leaf node, stop recursion) would be fine, while drill down
    keep the record of prefix sum
    it pass value from top - bottom, so no need to take value from child node, when meet leaf node, return
    cur level: add value
    report to parent: none
    :param root:
    :return:
    """
    global_max = [-float("inf")]
    prefix = 0
    def helper(root, global_max,prefix):
        if root is None:
            return
        prefix += root.data
        if root.left is None and root.right is None:
            # now is leaf node , should check global_max
            global_max[0] = max(global_max[0],prefix)
            return
        helper(root.left, global_max, prefix)
        helper(root.right, global_max,prefix)
    helper(root, global_max,prefix)
    return global_max[0]


def leaf_to_root_any_to_any_find_target(root,target):
    """
    determine whether there are a path(any to any) on the root to one of the leaf node that could sum to target
    use a set to save the prefix_sum,which is root to the current node sum. for new prefix_sum, if target - prefix_sum
    exist in the set, then the target path is found, otherwise addin to the set
    :param root:
    :return:
    """
    def helper(root,prefix_sum,prefix_sum_set,target):
        if root is None:
            return False
        prefix_sum += root.data
        if prefix_sum - target in prefix_sum_set:
            return True
        else:
            prefix_sum_set.add(prefix_sum)
            exist_in_left = helper(root.left, prefix_sum,prefix_sum_set,target)
            exist_in_right = helper(root.right, prefix_sum,prefix_sum_set,target)
            return exist_in_left or exist_in_right

    return helper(root,0,set([0]),target)


def leaf_to_root_any_to_any_maxPath(root):

    global_max = [-float("inf")]


    def helper(root, global_max):
        if root is None:
            return 0
        left = helper(root.left, global_max)
        right = helper(root.right,global_max)
        cur = max(max(left, right),0) + root.data # we could start with cur node if its child sum < 0
        global_max[0] = max(cur, global_max[0])
        return cur
    helper(root,global_max)
    return global_max[0]

def getHeight(root):
    """
    get from child: height of left child, height of right child
    cur level: max(height left, height right) + 1
    report to parent: cur level value
    time O(N), n is number of node; space O(Height)
    """
    if root is None:
        return 0
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    return max(left_height,right_height) + 1


def isBalanced(myTree):
    """
    time O(NlogN)
    """
    if myTree is None:
        return True
    leftHeight = getHeight(myTree.left)
    rightHeight = getHeight(myTree.right)
    if abs(leftHeight - rightHeight) > 1:
        return False
    return isBalanced(myTree.left) and isBalanced(myTree.right)

def isBalanced_optimize(root):
    """
    use 3 steps to make the time complexity in o(N)
    get from left child/right child, child tree height
    current: add 1 to the height, if left height - right height  is larget than 1, return -1
    report to parent: height

    :param root:
    :return:
    """
    def getHeight_v2(root):
        if root is None:
            return 0
        left_height = getHeight_v2(root.left)
        right_height = getHeight_v2(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height,right_height) + 1
    if root is None:
        return True
    if getHeight_v2(root) > 0:
        return True
    else:
        return False



def isBST(myTree):

    thisMin = -100
    thisMax = 100

    def helper(myTree, myMin, myMax):

        if myTree is None:
            return True
        if myTree.data < myMin or myTree.data > myMax:
            return False
        return helper(myTree.left, myMin, myTree.data) and helper(myTree.right, myTree.data, myMax)
    return helper(myTree, thisMin, thisMax)


def insert_bst(root,target):
    newNode = Tree()
    newNode.data = target

    if root is None:
        return newNode

    cur = root
    while cur is not None:

        if cur.data == target:
            print ("the node is already exist")

        elif cur.data < target:
            if cur.right is None:
                cur.right = newNode
            else:
                cur = cur.right
        else:
            if cur.left is None:
                cur.left = newNode
            else:
                cur = cur.left
    return root


def printKeyInRange(myTree,lower,upper):
    """
    the 2nd - 4th if condition could change order,
    the difference will be output order (preorder,inorder,and postorder)
    we chose inorder because this is a BST, so inorder will give an ascending array
    """
    if myTree is None:
        return

    if myTree.data > lower:
        printKeyInRange(myTree.left,lower,upper)

    if myTree.data >= lower and myTree.data <= upper:
        print(myTree.data)

    if myTree.data < upper:
        printKeyInRange(myTree.right,lower,upper)


def print_tree_by_level(root):
    """
    bfs: expand root, add left, right child
    each layer using a new line
    """
    if root is None:
        return
    queue = deque([])
    queue.append(root)
    while len(queue) > 0:
        cur_size = len(queue)
        for i in range(cur_size):
            curNode = queue.popleft()
            print curNode.data,
            if curNode.left is not None:
                queue.append(curNode.left)
            if curNode.right is not None:
                queue.append(curNode.right)
        print("\n")
    return

def printTreeByLevel_recursive(myTree):
    """
    we only need from top-down and don't need to return value from down-top
    therefore, we need another index(level) helping to mark which level we are in ,
    the base case was defined by this index rather than relying on leaf node
    in order to prevent return value from down-top, we need to manual set level in every recursive call

    we need O(N) to get Height of the tree,
    for every call of pretTreeByGivenLevel, the time complexity is O(N) too

    therefore the overall time is O(N + height*N) as for binary tree is O(N + N*logN), which is O(N*logN)
    """
    treeHeight = getHeight(myTree)
    print treeHeight
    resultList = [0] * treeHeight
    def printTreeByGivenLevel(theTree,level,curList):
        if level == 0:
            curList.append(theTree.data)
        else:
            printTreeByGivenLevel(theTree.left, level - 1,curList)
            printTreeByGivenLevel(theTree.right,level - 1,curList)
        return curList
    for i in range(treeHeight):
        curList = []
        resultList[i] = printTreeByGivenLevel(myTree,i,curList)
    print resultList
    return


def print_tree_zigzag_by_level(root):
    """
    compared with print tree by level, we need to know the level is even or odd
    if odd: from left to right to print, if even from right to lef to print
    :param root:
    :return:
    """
    if root is None:
            return
    mydeque = deque([])
    level_idx = True # True is odd, False is even
    mydeque.append(root)
    while len(mydeque) > 0:
        cur_size = len(mydeque)
        if level_idx:
            for i in range(cur_size):
                curNode = mydeque.popleft()
                print curNode.key,
                if curNode.left is not None:
                    mydeque.append(curNode.left)
                if curNode.right is not None:
                    mydeque.append(curNode.right)
            level_idx = False
        else:
            for i in range(cur_size , 0 , -1):
                curNode = mydeque.pop()
                print curNode.key,
                if curNode.right is not None:
                    mydeque.appendleft(curNode.right)
                if curNode.left is not None:
                    mydeque.appendleft(curNode.left)
            level_idx = True
        print "\n"
    return

def isComplete(myTree):
    """
    complete tree is only the last level allows null value and null is as right as possible
    it looks like we could still apply bfs to traverse the tree
    with that being said, if some mode is null, it must be all null after that in a bfs order

    still using BFS
    """
    if myTree is None:
        return True
    buffList = deque([])
    buffList.append(myTree)
    flag = True
    while flag:
        cur = buffList.popleft()
        if cur.left is None and cur.right is not None: # naturally violate complete tree defination
            return False
        elif cur.left is None and cur.right is None: # this is a leaf node, all node existing in buffList should all be leafNode
            flag = False
        elif cur.left is not None and cur.right is None: # this is not a full node,all the node after in buffList, include its left child should be leafnode
            buffList.append(cur.left)
            flag = False
        else: # this is a full node, we just append its child into buffList
            buffList.append(cur.left)
            buffList.append(cur.right)

    # when there is only root node in this tree,bufflist is empty we could directly return true
    if len(buffList) > 0:
        for treeNode in buffList: # check all remaining node is leafNode
            if treeNode.left is not None or treeNode.right is not None:
                return False
    return True


def delete_bst(root, target):
    """

    :param root: where tree start
    :param target: the node we want to delete
    :return:
    1.if target node has no child, we could just deleted it,by return null to the last recursion call
    2.if target is the node that miss left/right child,we could use its right/left node to replace it
    3. if target node has both left/right child, we could use the biggest from its left subtree and smallest from the
    right subtree to replace it
    so how to find the smallest from the right sub tree
    1).if targetNode.right.left is null, then targetnode.right is the smallest node in right subtree
    2).if targetNode.right.left is not null,trace down on left path and get the smallest node,
        set smallest.left = targetNode.left and smallest.right = targetNode.right
    """
    if root is None:
        return None
    targetNode = Tree()
    targetNode.data = target

    def find_smallest(cur): # find the most left node given cur treenode, delete it and return cur after the deletion
        prev = cur
        cur = cur.left
        while cur.left is not None:
            prev = cur
            cur = cur.left
        # not cur.left is null we can use case 2
        prev.left = prev.left.right
        return cur

    # first we need to search for the target node
    if root.data < target:
        root.right = delete_bst(root.right, target)
        return root
    if root.data > target:
        root.left = delete_bst(root.left, target)
        return root

    # now root.val == target, this function will choose using smallest node in right subtree to replace targetNode
    if root.right is None: # use root.left to replace the target Node
        return root.left
    elif root.left is None: # use root.right to replace the target Node
        return root.right
    elif root.right.left is None:
        root.right.left = root.left # make root.left to be the left of the new node (which is used to replace the old one)
        return root.right
    else:
        smallest = find_smallest(root.right)
        smallest.left = root.left
        smallest.right = root.right
        return smallest


def find_max_diff_size(root):
    """
    get from child: size of left subtree and size of right subtree
    cur level: size_left - size_right
    report to parent: size left + size right + 1
    """
    global_max_diff = [0]
    soluNode = [root]

    def get_size(root,diff,solution):
        if root is None:
            return 0

        left_size = get_size(root.left)
        right_size = get_size(root.right)

        if abs(left_size - right_size) > diff[0]:
            diff[0] = abs(left_size - right_size)
            solution[0] = root

        return left_size + right_size + 1
    get_size(root,global_max_diff,soluNode)
    return soluNode[0]


def find_a_closest_node(root,target):
    """
    given a bst, decide whether the target is exist in the node
    :param root:
    :param target:
    :return:
    """
    if root is None:
        return root
    result = root.data

    while root is not None:
        if root.data == target:
            return root.data
        else:
            if abs(root.data - target) < abs(result - target):
                result = root.data

            if root.data > target:
                root = root.left
            else:
                root = root.right
    return result


def find_largest_smaller_than_target(root,target):

    """
    give a bst and a target, among the smaller ones , find the closest to target
    :param root:
    :return:
    """
    if root is None:
        return root

    result = 0
    while root is not None:
        if root.data >= target:
            root = root.left
        else: # if cur node < target, then the right most leaf node has the largest value
            result = root.data
            root = root.right
    return result



if __name__ == "__main__":

    root = Tree()
    root.data = 10
    root.left = Tree()
    root.left.data = 8
    root.right = Tree()
    root.right.data = 12
    root.left.left = Tree()
    root.left.left.data = 6
    root.left.right = Tree()
    root.left.right.data = 9
    root.right.left = Tree()
    root.right.left.data = 11
    root.right.right = Tree()
    root.right.right.data = 13
    # print("test preOrder ", preOrder(root))
    # print("test inOrder ", inOrder(root))
    # print("test postOrder ", postOrder(root))
    # print("test getHeight", getHeight(root))
    # print("test isBST ",isBST(root))
    # print("test isBalanced ", isBalanced(root))
    # print("test printKeyByRange ", printKeyInRange(root,8,10))
    # print("test printTreeByLevel_iterative ", printTreeByLevel_iterative(root))
    # print("test printTreeByLevel_recursive ", printTreeByLevel_recursive(root))
    print("test printTreeByLevel_recursive ", isComplete(root))