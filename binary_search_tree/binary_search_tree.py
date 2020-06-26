"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        # got to left
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = new_node
        # go to right
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        found = False
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            found = self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found


    # Return the maximum value found in the tree
    def get_max(self):
        maximum = self.value
        if self.right is None:
            return maximum
        else:
            maximum = self.right.get_max()
        return maximum
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(node)
        
        print(self.value)

        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)
        # print(node, "NODE")

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left is not None:
                stack.append(current_node.left)
            if current_node.right is not None:
                stack.append(current_node.right)
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


