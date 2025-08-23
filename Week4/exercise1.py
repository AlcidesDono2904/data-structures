from typing import Any

class DoubleNode:
    
    def __init__(self,  value):
        self.value = value 
        self.next = None  # Points to next node
        self.prev = None  # Points to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:  # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            last = current
            current = current.next
        print("None")

    def display_backward(self):
        # Go to the last node
        current = self.head
        if current is None:
            print("None")
            return
        while current.next:
            current = current.next
        # Traverse backwards
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")
        
    def delete(self, value):
        if self.head == None:
            print ("None")
            return 

        current = self.head
        while current:
            if current.value == value:
                if current.next != None:
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
                if current.prev != None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                return
            current = current.next

        print ("Error: value", value, "is not in the list")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(6)
    dll.append(5)
    dll.append(9)
    dll.append(4)
    dll.append(2)
    dll.append(7)
    dll.display_forward()
    print ("deleting 3...")
    dll.delete(3)
    dll.display_forward()
    print ("deleting 1...")
    dll.delete(1)
    dll.display_forward()
    print ("deleting 5...")
    dll.delete(5)
    dll.display_forward()
    print ("deleting 7...")
    dll.delete(7)
    dll.display_forward()
    print ("deleting 69...")
    dll.delete(69)
    dll.display_forward()