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
        copies = {}
        current = head
        if not head:
            return head
        while current:
            copy = Node(current.val)
            copies[current] = copy
            current = current.next

        current = head
        while current:
            copy = copies[current]
            if current.next:
                copy.next = copies[current.next]
            if current.random:
                copy.random = copies[current.random]
            current = current.next

        return copies[head]


