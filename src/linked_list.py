class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.tail = None
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data, self.tail)
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.tail is None:
            if self.head is None:
                self.head = Node(data, self.tail)
            else:
                self.tail = Node(data, None)
                self.head.next_node = self.tail
        else:
            new_node = Node(data, None)
            self.tail.next_node = new_node
            self.tail = self.tail.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
