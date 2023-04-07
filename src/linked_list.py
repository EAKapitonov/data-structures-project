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

    def to_list(self):
        """
        возвращает список с данными, содержащимися в односвязном списке `LinkedList`
        """
        return_list = []
        first_node: Node = self.head
        while first_node:
            return_list.append(first_node.data)
            first_node = first_node.next_node
        return return_list

    def get_data_by_id(self, dat: int):
        """
        возвращает первый найденный в `LinkedList` словарь с ключом 'id', значение которого равно переданному в метод значению
        """
        first_node: Node = self.head
        while first_node:
            try:
                if not isinstance(first_node.data, dict):
                    raise TypeError
                elif first_node.data["id"] == dat:
                    return first_node.data
                else:
                    first_node = first_node.next_node
            except TypeError:
                print("неподходящий формат данных")
                first_node = first_node.next_node


