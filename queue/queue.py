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

# ARRAY
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.storage:
            item = self.storage.pop(-1)
            self.size -= 1
            return item
        else:
            return None


# LINKED LIST
class Node:
  def __init__(self, value=None, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
  

class Queue:
    def __init__(self):
        self.head = None # Stores a node, that corresponds to our first node in the list 
        self.tail = None # stores a node that is the end of the list
        self.len = 0

    def __len__(self):
        return self.len

    def enqueue(self, value):
        # create a node to add
        new_node = Node(value)
        
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.len += 1
        else:
            # new_node should point to current head
            old_node = self.head
            new_node.next_node = old_node
            old_node.prev_node = new_node
            self.len += 1
            # move head to new node
            self.head = new_node

    # remove the head and return its value
    def dequeue(self):
        # if list is empty, do nothing
        if not self.tail:
            return None
        # if list only has one element, set head and tail to None
        elif self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.len -= 1
            return head_value
        # otherwise we have more elements in the list
        else:
            tail_value = self.tail.value
            self.tail = self.tail.prev_node
            self.len -= 1
            return tail_value 

    def contains(self, value):
        if self.head is None:
            return False
        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
        # check if this is the node we are looking for
            if current_node.value == value:
                return True
            # otherwise, go to the next node
            current_node = current_node.next_node
            return False 


