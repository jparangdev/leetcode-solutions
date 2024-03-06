import unittest
from solutions.easy.LinkedListCycle import LinkedListCycle
from typing import Optional, List


class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.instance = LinkedListCycle()

    def create_cycle_linked_list(self, arr: List[int], pos: int) -> Optional[ListNode]:
        if not arr:
            return None
        head = ListNode(arr[0])
        nodes = [head]
        for num in arr[1:]:
            node = ListNode(num)
            nodes.append(node)
        for i in range(1, len(nodes)):
            nodes[i - 1].next = nodes[i]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return head

    def test_empty_linked_list(self):
        head = self.create_cycle_linked_list([], -1)
        self.assertEqual(self.instance.hasCycle(head), False)

    def test_linked_list_with_one_node(self):
        head = self.create_cycle_linked_list([1], -1)
        self.assertEqual(self.instance.hasCycle(head), False)

    def test_linked_list_with_one_node_cycle(self):
        head = self.create_cycle_linked_list([1], 0)
        self.assertEqual(self.instance.hasCycle(head), True)

    def test_linked_list_with_multiple_nodes_no_cycle(self):
        head = self.create_cycle_linked_list([1, 2, 3, 4, 5], -1)
        self.assertEqual(self.instance.hasCycle(head), False)

    def test_linked_list_with_multiple_nodes_cycle(self):
        head = self.create_cycle_linked_list([1, 2, 3, 4, 5], 2)
        self.assertEqual(self.instance.hasCycle(head), True)


if __name__ == '__main__':
    unittest.main()


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
