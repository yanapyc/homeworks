class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        return self._head is None

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def insert_after(self, target, data):
        new_node = Node(data)
        cur_node = self._head

        while cur_node != None and cur_node.data != target:
            cur_node = cur_node.next
        
        new_node.prev = cur_node
        new_node.next = cur_node.next

        if cur_node.next != None:
            cur_node.next.prev = new_node

        cur_node.next = new_node

    def insert_before(self, target, data):
        new_node = Node(data)
        cur_node = self._head
        while cur_node != None and cur_node.data != target:
            cur_node = cur_node.next

        if cur_node is None:
            raise ValueError("The target doesn't exist")

        new_node.next = cur_node
        new_node.prev = cur_node.prev

        if cur_node.prev != None:
            cur_node.prev.next = new_node
        else:
            self._head = new_node

        cur_node.prev = new_node

    def delete(self, data):
        cur_node = self._head
        while cur_node != None and cur_node.data != data:
            cur_node = cur_node.next

        if cur_node is None:
            raise ValueError("The data doesn't exist")

        if cur_node.prev != None:
            cur_node.prev.next = cur_node.next
        else:
            self._head = cur_node.next

        if cur_node.next != None:
            cur_node.next.prev = cur_node.prev
        else:
            self._tail = cur_node.prev

    def display(self):
        cur_node = self._head
        while cur_node:
            print(cur_node.data, end=" <-> ")
            cur_node = cur_node.next
        print()

linked_list = LinkedList()
linked_list.append(3)
linked_list.display()
linked_list.prepend(1)
linked_list.display()
linked_list.append(5)
linked_list.display()

linked_list.insert_after(3, 4)
linked_list.display()
linked_list.insert_before(4, 2)
linked_list.display()

linked_list.delete(3)
linked_list.display()
