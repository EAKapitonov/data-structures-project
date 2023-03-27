class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.next = None
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.next = Node(data, None)
        self.tail.next_node = self.next
        self.tail = self.next
        while self.head.data == None:
            self.head = self.head.next_node


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        return_data = self.head.data
        self.head = self.head.next_node
        return return_data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        x = None
        text = ""
        head = self.head
        while x == None:
            if head.data == None:
                x = 1
                return text.rstrip("\n")
            else:
                text = text + f"{head.data}\n"
                if head.next_node == None:
                    x = 1
                    return text.rstrip("\n")
                else:
                    head = head.next_node
