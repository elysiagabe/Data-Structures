from singly_linked_list import LinkedList, Node

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   As far as implementation goes, we were able to use the built-in append() and pop() methods available to us for the array; for the Linked List, we used add_to_tail() and remove_tail methods we built out as part of the Linked List class. 

   As far as run time classification goes, LL is much more efficient (it's classified as O(c)) because you basically just have to update the tail reference value and set the old tail's next_node reference to the new tail instead of none instead of having to copy and move the entire list to a new space as you would with an array (appending a dynamic array is classified as O(n)).
"""

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ARRAY STORAGE STRUCTURE IMPLEMENTATION: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    # RETURNS THE # OF ELEMENTS IN THE STACK
    def __len__(self):
        return self.size

    # ADDS ITEM TO TOP OF STACK
    def push(self, value):
        # Array implementation: use append() method to add value to end of self.storage array...will also need to increase the size by 1 
        self.storage.append(value)
        self.size += 1
        

    # REMOVES ITEM AT TOP OF STACK AND RETURNS THAT ITEM
    def pop(self):
        # Array implementation: use pop() method to remove last value of self.storage and return that value...will also need to decrease size by 1
        # Need to account for empty list!
        if self.size is 0: 
            return None
        
        removed = self.storage.pop()
        self.size -= 1
        return removed

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LINKED LIST STORAGE STRUCTURE IMPLEMENTATION: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class Stack: 
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    # RETURNS THE # OF ELEMENTS IN THE STACK
    def __len__(self):
        return self.size

    # ADDS ITEM TO TOP OF STACK
    def push(self, value):
        # LL implementation: value will become tail of LL...use add_to_tail() method from LinkedList class...class accounts for empty list
        self.storage.add_to_tail(value)
        self.size += 1

    # REMOVES ITEM AT TOP OF STACK AND RETURNS THAT ITEM
    def pop(self):
        # LL implementation: value at top of stack is tail...use remove_tail() method from LinkedList class to remove and return that item...
        if self.size is not 0:
            self.size -= 1
        return self.storage.remove_tail()