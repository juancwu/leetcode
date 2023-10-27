from typing import Optional
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        use hashmap to record visited knows in the
        map[node] = i where i is the index
        loop til end of linked list, if no early return then no loop
        """
        
        visited = defaultdict(int)
        
        while head:
            if head.next in visited:
                return head.next
            visited[head] = 1
            head = head.next
        
        return None