"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)
            self.head.prev = None
            self.head.next = None
            self.length += 1
        elif self.length == 1:
            self.head = ListNode(value)
            self.head.next = self.tail
            self.head.prev = None
            self.tail.prev = self.head
            self.tail.next = None
            self.length += 1
        else:
            print(self.length, "BEFORE")
            head = self.head
            self.head = ListNode(value)
            self.head.next = head.prev
            self.head.prev = None
            head.prev = self.head
            self.length += 1
            print(self.length, "AFTER")


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            old_node = self.head
            self.head = old_node.next
            self.head.prev = None
            self.length -= 1
            return old_node.value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.length == 0:
            new = ListNode(value)
            self.tail = new
            self.tail.prev = None
            self.tail.next = None
            self.head = self.tail
            self.length += 1
        elif self.length == 1:
            new = ListNode(value)
            old = self.tail
            self.tail = new
            self.tail.prev = old
            self.tail.next = None
            old.next = new
            self.length += 1
        else:
            old = self.tail
            new = ListNode(value)
            self.tail = new
            self.tail.prev = old
            self.tail.next = None
            old.next = self.tail
            self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return tail.value
        else:
            old = self.tail
            self.tail = old.prev
            self.tail.next = None
            self.length -= 1

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.length == 0:
            return None
        elif node.next is None:
            tail = self.tail
            head = self.head
            self.tail = tail.prev
            self.tail.next = None
            self.head = tail
            self.head.prev = None
            self.head.next = head
            head.prev = self.head
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            old = self.head
            self.head = node
            old.prev = head
            head.next = old
            node.next = None

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.length == 0:
            return None
        elif node.prev is None:
            old = self.head
            self.head = old.next
            self.head.prev = None
            tail = self.tail
            self.tail = old
            self.tail.next = None
            self.tail.prev = tail.next
        else:
            print(node.prev, node.next, "PREV, NEXT")
            prev = node.prev
            next = node.next
            prev.next = node.next
            next.prev = node.prev
            old = self.tail
            self.tail = node
            old.prev = self.tail
            self.tail.next = old
            self.tail.prev = None
            node.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.length == 0:
            return None
        elif node == self.head:
            self.remove_from_head()
        elif  node == self.tail:
            self.remove_from_tail()
        else:
            prev = node.prev
            next = node.next
            prev.next = node.next
            next.prev = node.prev
            self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        maximum = 0
        didgit = self.head
        while didgit.next != None:
            if didgit < didgit.next:
                maximum = didgit
                return maximum
            else:
                maximum = didgit.next
                return maximum


