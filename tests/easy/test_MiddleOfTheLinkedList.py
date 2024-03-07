import unittest
from solutions.easy.MiddleOfTheLinkedList import MiddleOfTheLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TestMiddleOfLinkedList(unittest.TestCase):
    def setUp(self):
        self.MiddleOfTheLinkedList = MiddleOfTheLinkedList()

    def create_linked_list(self, array):
        if not array:
            return None
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            current.next = ListNode(array[i])
            current = current.next
        return head

    def test_middle_node_even(self):
        head = self.create_linked_list([1, 2, 3, 4])
        result = self.MiddleOfTheLinkedList.middleNode(head)
        self.assertEqual(result.val, 3)

    def test_middle_node_odd(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.MiddleOfTheLinkedList.middleNode(head)
        self.assertEqual(result.val, 3)

    def test_single_node(self):
        head = self.create_linked_list([1])
        result = self.MiddleOfTheLinkedList.middleNode(head)
        self.assertEqual(result.val, 1)


if __name__ == "__main__":
    unittest.main()
