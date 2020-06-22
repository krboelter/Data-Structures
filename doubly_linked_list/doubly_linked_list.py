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
            self.head.prev = None
            self.head.next = None
            self.tail = self.head
            self.legnth += 1
        if self.length == 1:
            head = self.head
            new = ListNode(value)
            self.tail = head
            self.tail.prev = new
            self.tail.insert_before(new)
            self.length += 1
        new = ListNode(value)
        self.head.insert_before(new)
        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head.delete()
            self.length -= 1
        old_node = self.head
        self.head = old_node.next
        self.length -= 1

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.length == 0:
            self.tail = ListNode(value)
            self.tail.prev = None
            self.tail.next = None
            self.head = self.tail
            self.length += 1
        old = self.tail
        self.tail.insert_after(value)
        self.tail.prev = self.tail
        self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None
            self.head = None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.head.insert_before(node)
        node.prev = None

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.tail.insert_after(node)
        node.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node == self.head:
            print(self.head.prev, "HEAD PREV", self.head.next, "HEAD NEXT")
            if self.head.prev:
                self.head = self.head.prev
                self.head.delete()
            self.head.delete()
            self.length -= 1
            print("DELETED AS HEAD")
        if  node == self.tail:
            tail = self.tail
            self.tail = tail.prev
            tail.delete()
            self.length -= 1
            print("DELETED AS TAIL")
        current_node = node
        prev = current_node.prev
        next = current_node.next
        current_node.next = prev
        current_node.prev = next
        current_node.delete()
        self.length -= 1
        print("DELETED AS OTHER")
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        maximum = 0
        didgit = self.head
        while didgit.next != None:
            if didgit < didgit.next:
                maximum = didgit
            else:
                maximum = didgit.next
