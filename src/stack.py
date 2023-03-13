class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self._data = [None]
        self.i = 0
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        obj_node = Node(data, self._data[self.i])
        self._data.append(obj_node)
        self.i += 1
        self.top = self._data[self.i]

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и возвращение его данных

        :return: данные удаленного элемента
        """
        return_data = self._data[self.i]
        self._data.pop()
        self.i -= 1
        return return_data

