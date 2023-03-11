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
        self.data = [None]
        self.i = 0

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        obj_node = Node(data, self.data[self.i])
        self.data.append(obj_node)
        self.i += 1

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        return_data = self.data[self.i]
        self.data.pop()
        self.i -= 1
        return return_data

    def top(self):
        """
        Метод для это ссылки на верхний элемент

        :return: данные верхнего элемента
        """
        return self.data[self.i]

    top = property(top)
