from doubly_linked_list import DoublyLinkedList


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = DoublyLinkedList()

#     def append(self, item):
#         pass

#     def get(self):
#         # Note:  This is the only [] allowed
#         list_buffer_contents = []

#         # TODO: Your code here

#         return list_buffer_contents


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

    
        if self.storage.length < self.capacity:
          self.storage.add_to_tail(item)
          self.current = self.storage.tail
        
        
        elif self.current == self.storage.tail:
            self.storage.head.value = item
            self.current = self.storage.head

        else:
          self.current.next.value = item
          self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head

        if self.storage.length == 0:
          return list_buffer_contents
        else:
          while node:
            # list_buffer_contents = [node.value for node in self.storage]
            list_buffer_contents.append(node.value)
            node = node.next

          return list_buffer_contents






# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass




if __name__ == "__main__":
    b = RingBuffer(5)
    b.append("a")
    b.append("b")
    b.append("c")
    b.append("d")
    # print(b.storage.length)
    print(b.get())
    b.append("e")
    # # # print(b.storage.length)
    print(b.get())
    b.append("f")
    print(b.get())
    b.append("g")
    b.append("h")
    b.append("i")
    print(b.get())

