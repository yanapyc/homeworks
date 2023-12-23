from linked_list import LinkedList

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.display()   
    linked_list.append(2)
    linked_list.display()
    linked_list.append(3)
    linked_list.display()
    print("\nLinked List:")
    linked_list.display()

    linked_list.insert(1, 4)
    print("\nIn Linked List insert 4 in index 1:")
    linked_list.display()

    linked_list.delete(2)
    print("\nAfter deleting 2:")
    linked_list.display()

    print("\nIs empty Linked list? ", linked_list.is_empty())