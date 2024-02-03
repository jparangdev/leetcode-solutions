import unittest

from solutions.easy.MergeTwoLists import MergeTwoLists, ListNode


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.instance = MergeTwoLists()

    def test(self):
        # Initialize lists here
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))

        result = self.instance.mergeTwoLists(l1, l2)

        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 1)
        self.assertEqual(result.next.next.val, 2)


