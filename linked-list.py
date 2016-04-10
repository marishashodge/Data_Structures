# Make a node class

class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

# Instantiate a new node
# new_node = Node(5)


# Make a Linked List class (object):

class LinkedList(object):
    """Linked List class with a head and a tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        """Print all the items in the list."""

        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def find_node(self, data):
        """Find the matching data in the linked list"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next

        return False

    def add_node(self, data):
        """Add the node to the end of a linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    # def remove_node(self,value):
    #     """Remove a node from the list."""
    #
    #     if self.head and self.head.data == value:
    #         self.head = self.head.next
    #
    #     current = self.head
    #
    #     while current.next is not None:
    #         if current.next.data == value:
    #             current.next = current.next.next
    #             return
    #         else:
    #             current = current.next


    def remove_node_with_prev(self, value):
        """Remove a node from the list."""

        prev = None
        current = self.head

        while current is not None:
            if current.data == value:
                if prev is None:
                    current.next = self.head
                else:
                    prev.next = current.next
                    current.next = self.head
                return
            else:
                prev = current
                current = current.next

    def remove_by_index(self, index):
        """Remove a node at the index."""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next

        else:
            prev.next = node.next


    def add_by_index(self, index, data):
        """Add a node to a list at a given index."""

        new_node = Node(data)

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            prev = new_node
            prev.next = node
            prev = self.head

        else:
            prev.next = new_node
            new_node.next = node


my_ll = LinkedList()
my_ll.add_node("apple")
my_ll.add_node("berry")
my_ll.add_node("cherry")
my_ll.remove_node_with_prev("berry")
my_ll.print_list()
my_ll.add_node("banana")s
my_ll.add_node("orange")
my_ll.remove_by_index(1)
my_ll.print_list()
my_ll.add_by_index(3, "honey")
my_ll.print_list()
