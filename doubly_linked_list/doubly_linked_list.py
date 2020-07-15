"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.

    Replaces the head of the list with a new value that's passed in.
    """
    def add_to_head(self, value):
        # if current head is None (means nothing in list yet), add the new node to the list (prev & next will both be none, which is default value)
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # if current head is not None, the new node will have the old head as the next value and none as the previous value...current head next will remain the same and prev will be the new node
        else: 
            current_head = self.head
            new_node = ListNode(value, None, current_head)
            self.head = new_node
            current_head.prev = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if current head is None / length is 0, means empty list. Return None...nothing to remove
        if not self.head: 
            return None
        # if current length is 1 / next value on current head is none / just one node in list, remove & return that node. Head & tail will both become None
        current_head = self.head
        if not current_head.next: 
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        # if list is longer than 1, remove & return the current head. New head will be the next value of current head. Also need to set prev value of new head to None?
        self.head = current_head.next
        self.head.prev = None
        self.length -= 1
        return current_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.

    Replaces tail of list w/new value that's passed in. 
    """
    def add_to_tail(self, value):
        # if empty list (length 0, current head or tail is None), new node is assigned to head and tail. prev & next values of new node will both be none (which is default)
        if self.tail is None: 
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1

        # if list of one or more, new node becomes tail (prev points to current tail, next is none) and current tail's next value becomes the new tail
        else: 
            current_tail = self.tail
            new_node = ListNode(value, current_tail, None)
            current_tail.next = new_node
            self.tail = new_node
            self.length += 1
        # CLASS NOTES: 
        # create instance of List Node w/ value
        # incrememnt DLL length attr
        # if DLL is empty
            # set head & tail to new node instance
        # if DLL is not empty
            # set new node's prev to current tail
            # set tail's next to new node
            # set tail to new node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # If empty list, nothing to remove. Return None. 
        if not self.tail: 
            return None
        # If list has only one element, return & remove that node. Then reassign head & tail to None. Decrement length
        current_tail = self.tail
        self.length -= 1
        if self.tail == self.head: # if not current_tail.prev:
            self.head = None
            self.tail = None
        # If list has more than 1, Remove & return current tail. New tail becomes the previous value of the current tail. Decrement length
        self.tail = current_tail.prev
        return current_tail.value

        # CLASS NOTES: 
        # store value of tail
        # decrement length of DLL
        # delete the tail
            # if tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
            # else (if tail.prev is None)
                # set head to None
                # set tail to None
        # return the value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if only one item in list, nowhere to move...
        if self.head is not self.tail: 
            # if list is not empty, delete the node first...
            if self.head is not None: 
                self.delete(node)
            # add to tail 
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if only one item in list, nowhere to move...
        if self.head is not self.tail: 
            # if list is not empty, delete the node first...
            if self.head is not None: 
                self.delete(node)
            # add to tail 
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # empty list? dont do anything...nothing to delete
        if self.length > 0: 
            # decrement length
            self.length -= 1
            # if one item in list: head & tail are same...set both to None
            if self.tail is self.head: 
                self.tail = None
                self.head = None
            # if node is head, the previous value on node's next value needs to be None...reassign head to node's next value
            elif node is self.head: 
                next_node = node.next
                next_node.prev = None
                self.head = next_node
            # if node is tail, the next value on node's previous needs to be set to None...reassign tail to node's previous
            elif node is self.tail:
                prev_node = node.prev
                prev_node.next = None
                self.tail = prev_node
            # otherwise, set next value for node's previous to node's next and vice versa
            else:
                prev_node, next_node = node.prev, node.next
                prev_node.next, next_node.prev = next_node.value, prev_node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass