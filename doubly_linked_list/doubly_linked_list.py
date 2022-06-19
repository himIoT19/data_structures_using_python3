class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        """
        Constructor
        :param value:
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()

    def append(self, value) -> bool | None:
        """

        :param value:
        :return:
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node | None:
        if self.length == 0:
            return None
        # If we have 1 or more elements
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node | None:
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp


if __name__ == '__main__':
    my_doubly_linked_list = DoublyLinkedList(7)

    # region Print DoublyLinkedList
    # my_doubly_linked_list.print_list()
    # endregion

    # region Append an item
    # my_doubly_linked_list.append(13)
    # my_doubly_linked_list.print_list()
    # endregion

    # region POP
    # my_doubly_linked_list.append(12)
    # my_doubly_linked_list.append(14)
    # my_doubly_linked_list.append(16)
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.print_list()
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.print_list()
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.print_list()
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.print_list()
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.print_list()

    # endregion

    # region Prepend
    # my_doubly_linked_list.append(8)
    # my_doubly_linked_list.prepend(6)
    # my_doubly_linked_list.print_list()

    # endregion

    # region POP first element

    # endregion
