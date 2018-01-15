# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

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
    if myNode is None:
        return
    newHead = reverse_recur(myNode.next)
    myNode.next.next = myNode
    myNode.next = None
    return newHead

