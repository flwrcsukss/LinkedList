class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"




class liLinkedList(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def len_ll(self):
        current_node = self.head
        k = 0
        while current_node is not None:
            current_node = current_node.next_node
            k += 1
        return k

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return 'Список выведен с конца'

    def insert_node_index(self, index, data):
        if index == 0:
            self.insert_at_head(data)
            return 'Добавление в начало завершено'
        elif index >= self.len_ll():
            self.insert_at_tail(data)
            return 'Добавление в конец завершено'
        current_node = self.head
        new_node = Node(data)
        for i in range(index + 1):
            if i == index - 1:
                current_node.next_node.prev_node = new_node
                new_node.next_node = current_node.next_node
                new_node.prev_node = current_node
                current_node.next_node = new_node
                break
            current_node = current_node.next_node

    def remove_node_index(self, index):
        current_node = self.head
        if index == 0:
            self.remove_from_head()
        elif index + 1 == self.len_ll():
            self.remove_from_tail()
        else:
            for i in range(index + 1):
                if i == index:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node.prev_node

                current_node = current_node.next_node

    def remove_node_data(self, data):
        current_node = self.head
        for i in range(self.len_ll()):
            if current_node.data == data and i == 0:
                self.remove_from_head()
                break
            elif current_node.data == data and i == self.len_ll() - 1:
                self.remove_from_tail()
                break
            elif current_node.data == data and i != 0 and i != self.len_ll() + 1:
                current_node.prev_node.next_node = current_node.next_node
                current_node.next_node.prev_node = current_node.prev_node.prev_node
                break
            current_node = current_node.next_node

    def contains_from_head(self, data):
        current_node = self.head
        for i in range(self.len_ll()):
            if current_node.data == data:
                return f'{data} существует в Linked List'
            current_node = current_node.next_node
        return f'{data} в Linked List нет!'

    def contains_from_tail(self, data):
        current_node = self.tail
        for i in range(self.len_ll(), 0, -1):
            if current_node.data == data:
                return f'{data} существует в Linked List'
            current_node = current_node.prev_node
        return f'{data} в Linked List нет!'

    def contains_from(self, side, data):
        if side == 'head':
            return self.contains_from_head(data)
        elif side == 'tail':
            return self.contains_from_tail(data)
        else:
            return 'Не знаю откуда начинать проверять'





llist = liLinkedList()
llist.insert_at_head('robert')
llist.insert_at_head('tom')
llist.insert_at_tail('vovan')
llist.insert_at_tail('unabomber')

# llist.insert_node_index(3, 'qwe')
# llist.remove_node_index(4)
# llist.remove_node_data('vovan')
llist.print_ll_from_head()
# print(llist.contains_from_head('vovan'))
# print(llist.contains_from_tail('wsdv'))
print(llist.contains_from('tail', 'robert'))
print(llist.len_ll())