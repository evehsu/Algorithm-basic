# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def reverse_iter(myNode):
    """
    using iterative to reverse a linked list
    :param myNode:
    :return:
    """
    if myNode is None:
        return
    prev = None
    while myNode is not None:
        myNext = myNode.next
        myNode.next = prev
        prev = myNode
        myNode = myNext
    return prev


def reverse_recur(myNode):
    if myNode is None or myNode.next is None:
        return myNode
    newHead = reverse_recur(myNode.next)
    myNode.next.next = myNode
    myNode.next = None
    return newHead

def reverse_inPairs(head):
    """
    1 -> 2 -> 3 -> 4
    2 -> 1 -> 4 -> 3
    :param head:
    :return: newhead
    """
    if head is None or head.next is None:
        return head
    newhead = head.next
    head.next = reverse_inPairs(head.next.next)
    newhead.next = head
    return newhead


def reverse_binary_tree(root):

    """
    reverse binary tree upside down
    make the root to be the leaf ndoe, and make the left most leaf node to the root
    even though it is tree-based,the logic is almost the same as reverse a linkedlist
    :param root:
    :return: newroot
    """
    if root is None or root.left is None:
        return root
    newRoot = reverse_binary_tree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    return newRoot



