from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert(self,index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        
        if index == 0:
            new_node.set_next(cur_node)
            self.head = new_node
            return
            
        while cur_node != None:
            if count + 1 == index:
                the_node_after_cur = cur_node.get_next() 
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()

        print("The index out of range")

    def display(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.get_data(), end = " -> ")
            cur_node = cur_node.get_next()
        print()
    
   
    def delete(self,data):
        cur_node = self.head
        prev = None

        while cur_node != None and cur_node.get_data() != data:
            prev = cur_node
            cur_node = cur_node.get_next()

        if cur_node != None and cur_node.get_data() == data:    
            the_after_cur_node = cur_node.get_next()

            if prev != None:
                prev.set_next(the_after_cur_node)
            else:
                self.head = the_after_cur_node

    def append(self, data):
	    new_node = Node(data)
	    cur_node = self.head
	    if cur_node == None:
		    self.head = new_node
		    return
	    while cur_node.get_next() != None:
		    cur_node = cur_node.get_next()
	    cur_node.set_next(new_node)


    def __iter__(self):
        cur_node = self.head

        while cur_node != None:
            yield cur_node.get_data()
            cur_node = cur_node.get_next()

    def __next__(self):
       return self.head.get_next()