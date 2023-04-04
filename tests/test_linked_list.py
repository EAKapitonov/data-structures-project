import unittest
from src.linked_list import LinkedList, Node

"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""


class test_Node(unittest.TestCase):
    """
    тестирует класс Node
    """

    def test_init(self):
        data_test = Node({'id': 1}, None)
        self.assertEqual(data_test.data, {'id': 1})
        self.assertEqual(data_test.next_node, None)


class test_LinkedList(unittest.TestCase):
    """
    тестирует класс LinkedList
    """

    def test_init(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        self.assertEqual(ll.tail.next_node, None)
