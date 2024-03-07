from typing import Optional

from node.ListNode import ListNode


class MiddleOfTheLinkedList:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        result = head
        counter = 0
        while cursor.next != None:
            cursor = cursor.next
            counter += 1
            if counter % 2 == 1:
                result = result.next
        return result
