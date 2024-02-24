import unittest

from node.ListNode import ListNode
from solutions.easy.RemoveDuplicatesFromSortedList import RemoveDuplicatesFromSortedList


class TestRemoveDuplicatesFromSortedList(unittest.TestCase):

    def setUp(self):
        self.solution = RemoveDuplicatesFromSortedList()

    def test_empty_list(self):
        self.assertEqual(self.solution.deleteDuplicates(None), None)

    def test_single_node_list(self):
        node = ListNode(1)
        self.assertEqual(self.solution.deleteDuplicates(node), node)

    def test_two_identical_nodes(self):
        node1 = ListNode(1)
        node2 = ListNode(1)
        node1.next = node2
        self.assertEqual(self.solution.deleteDuplicates(node1), node1)

    def test_two_different_nodes(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        self.assertEqual(self.solution.deleteDuplicates(node1), node1)

    def test_list_with_no_duplicates(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3
        self.assertEqual(self.solution.deleteDuplicates(node1), node1)

    def test_list_with_duplicates(self):
        node1 = ListNode(1)
        node2 = ListNode(1)
        node3 = ListNode(2)
        node4 = ListNode(3)
        node5 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = self.solution.deleteDuplicates(node1)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next, None)


if __name__ == "__main__":
    unittest.main()
