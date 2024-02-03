import heapq
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        for l in [list1, list2]:
            while l:
                nodes.append(l.val)
                l = l.next
        heapq.heapify(nodes)
        head = ListNode(0) # dummy node
        node = head
        while nodes:
            val = heapq.heappop(nodes)
            node.next = ListNode(val)
            node = node.next
        return head.next


