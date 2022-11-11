from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two pointers approach
        slow and fast pointer
        
        1 -> 2 -> 3 -> 4 -> 5
        ^
        sf
        1 -> 2 -> 3 -> 4 -> 5
             ^    ^
             s    f
        1 -> 2 -> 3 -> 4 -> 5
                  ^         ^
                  s         f
                  
        s is middle of linked list
        """
        
        s, f = head, head
        
        while f and f.next:
            s = s.next
            f = f.next.next
        
        return s