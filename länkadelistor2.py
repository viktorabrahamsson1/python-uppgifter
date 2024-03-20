class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushfirst(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def popfirst(self):
        if self.head is None:
            print("List is empty")
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def pushlast(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def poplast(self):
        if self.tail is None:
            print("List is empty")
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    my_list = DoubleLinkedList()

    my_list.pushfirst(2)
    my_list.pushfirst(1)
    my_list.pushlast(3)
    my_list.pushlast(4)

    my_list.display()

    print("Pop first:", my_list.popfirst())
    print("Pop last:", my_list.poplast())

    my_list.display()

