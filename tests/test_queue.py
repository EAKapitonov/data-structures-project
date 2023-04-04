from src.queue import Node, Queue


class test_Node(unittest.TestCase):
    """
    тестирует класс Node
    """

    def test_init(self):
        data_test = Node(5, None)
        self.assertEqual(data_test.data, 5)
        self.assertEqual(data_test.next_node, None)


class test_Queve(unittest.TestCase):
    """
    тестирует класс Queve
    """

    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.next, None)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert queue.head.data == 'data1'

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        queue.dequeue()
        assert queue.head.data == 'data2'
        queue.dequeue()
        assert queue.head.data == 'data3'

    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert str(queue) == "data1\ndata2\ndata3"
