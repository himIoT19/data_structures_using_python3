# region "Node" Class
class Node:
    def __init__(self, value):
        """
        Example, Node = {
                            "value": 4,
                            "next": None
                        }
        :param value:
        """
        self.value = value
        self.next = None


# endregion

# region "LinkedList" Class
class LinkedList:
    # region Constructor
    def __init__(self, value):
        """
        Create new Node
        :param value:
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # endregion

    # region Append functionality
    def append(self, value):
        """
        Add an item to the end of the LinkedList & becomes 'tail'
        Create new Node
        add Node to end
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    # endregion

    # region Prepend functionality
    def prepend(self, value):
        """
        Add an item to the start of the LinkedList & becomes 'head'
        Create new Node
        add Node to beginning
        :param value:
        :return:
        """
        new_node = Node(value)

        # If empty LinkedList
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True

    # endregion

    # region Get value by index
    def get_value(self, index):
        """

        :param index:
        :return:
        """
        # Check if the 'index' is valid
        if index < 0 or index >= self.length:
            return None

        # will point to 'head'
        temp = self.head

        for _ in range(index):
            temp = temp.next
        return temp

    # endregion

    # region Insert value start/end/between o and max index value
    def insert(self, index, value):
        """
        Create new Node
        insert Node
        :param index:
        :param value:
        :return:
        """
        if index < 0 or index > self.length:
            return False
        # If we want to add element to
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    # endregion

    # region Pop functionality
    def pop(self):
        """

        :return:
        """
        # Check if we have empty LinkedList
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        # Go to the end of the LinkedList
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # If LinkedList has only one element then LinkedList ends with None
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    # endregion

    # region Pop first element
    def pop_first(self):
        """
        Pops the first element of the LinkedList & 'head' moves to the next element
        :return:
        """
        # If empty LinkedList
        if self.length == 0:
            return None

        # Business logic to move head to next element
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # If LinkedList is empty then 'tail' will be None
        if self.length == 0:
            self.tail = None

        return temp

    # endregion

    # region Remove by index
    def remove(self, index):
        """

        :param index:
        :return:
        """
        # Validate the index is valid
        if index < 0 or index >= self.length:
            return None
        # Remove item from the start of LinkedList
        if index == 0:
            return self.pop_first()
        # Remove item from the end of LinkedList
        if index == self.length - 1:
            return self.pop()

        prev = self.get_value(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

    # endregion

    # region Set value by index
    def set_value(self, index, value):
        """

        :param index:
        :param value:
        :return:
        """
        if temp := self.get_value(index):
            temp.value = value
            return True
        return False

    # endregion

    # region Reverse functionality
    def reverse(self):
        """

        :return:
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # endregion

    # region Print LinkedList
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    # endregion


# endregion


if __name__ == "__main__":
    # Create a LinkedList
    my_linked_list = LinkedList(2)

    # append() an item to the LinkedList
    my_linked_list.append(3)
    my_linked_list.append(4)

    # prepend() an item to the LinkedList
    my_linked_list.prepend(1)

    # set_value() at index 2 value=33
    # my_linked_list.set_value(index=2, value=33)

    # print_list() LinkedList elements
    # my_linked_list.print_list()

    # reverse() LinkedList elements
    # my_linked_list.reverse()
    # my_linked_list.print_list()

    # remove() operation LinkedList
    # print(my_linked_list.remove(2), end='\n')
    # my_linked_list.print_list()

    # pop() operation LinkedList
    print(my_linked_list.pop())
    print(my_linked_list.pop())
    print(my_linked_list.pop())

    # pop_first() operation LinkedList
    # print(my_linked_list.pop_first())
    # print(my_linked_list.pop_first())
    # print(my_linked_list.pop_first())
    # print(my_linked_list.pop_first())
    # print(my_linked_list.pop_first())

    # get_value() the value of index 2
    # print(my_linked_list.get_value(2))
