from singly_linked_list import LinkedList, Node

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ARRAY STORAGE STRUCTURE IMPLEMENTATION: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    # RETURNS THE # OF ELEMENTS IN QUEUE
    def __len__(self):
        return self.size

    # ADDS AN ELEMENT TO THE BACK OF THE QUEUE
    def enqueue(self, value):
        # Array implementation: can use append() method to add item to end of queue...also need to increase size by 1
        self.storage.append(value)
        self.size += 1

    # REMOVES ELEMENT AT THE FRONT OF THE QUEUE & RETURNS THAT ELEMENT
    def dequeue(self):
        # Array implementation: can use pop() method with index 0 to remove & return that element...will also need to decrease size by 1 and account for length 0
        if self.size is 0: 
            return None

        removed = self.storage.pop(0)
        self.size -= 1
        return removed 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LINKED LIST STORAGE STRUCTURE IMPLEMENTATION: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    # RETURNS THE # OF ELEMENTS IN QUEUE
    def __len__(self):
        return self.size

    # ADDS AN ELEMENT TO THE BACK OF THE QUEUE
    def enqueue(self, value):
        # LL implementation: back of queue means the tail of the queue...can use the add_to_tail() method from the LL Class
        self.storage.add_to_tail(value)
        self.size += 1

    # REMOVES ELEMENT AT THE FRONT OF THE QUEUE & RETURNS THAT ELEMENT
    def dequeue(self):
        #LL implementation: front of queue means the head...can use the remove_head() method from the LL class
        if self.size is not 0:
            self.size -= 1
        return self.storage.remove_head()
