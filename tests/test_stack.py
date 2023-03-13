from src.stack import Node, Stack
import unittest
"""Здесь надо написать тесты с использованием unittest для модуля stack."""
class test_Node(unittest.TestCase):
    """
    тестирует класс Node
    """
    def test_init(self):
        data_test = Node(5, None)
        self.assertEqual(data_test.data, 5)
        self.assertEqual(data_test.next_node, None)
class test_Stack(unittest.TestCase):
    """
    тестирует класс Stack
    """
    def test_top(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')

