"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {} #original, copy
        dummy = copy = Node(0)
        while head:
            copy.next = Node(head.val)
            hashMap[head] = copy.next
            copy = copy.next
            head = head.next
        
        for node, c in hashMap.items():
            rand = node.random #key/original
            c.random = hashMap.get(rand)
        
        return dummy.next