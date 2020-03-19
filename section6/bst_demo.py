class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # create Node
        if not isinstance(key, Node):
            key = Node(key)
        # if empty, no root    
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    # _{method_name} provate method
    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        # left, root, right
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def pre_order(self):
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)  
            print(curr.data, end=" ")

tree = BSTDemo()             
# tree.insert("F")
# print(tree.root.data)
# tree.insert("C")
# print(tree.root.left_child.data)
# tree.insert("G")
# print(tree.root.right_child.data)
# tree.insert("A")
# print(tree.root.left_child.left_child.data)
# tree.insert("B")
# print(tree.root.left_child.left_child.right_child.data)
# tree.insert("K")
# print(tree.root.right_child.right_child.data)
# tree.insert("H")
# print(tree.root.right_child.right_child.left_child.data)
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")
tree.in_order()
tree.pre_order()
tree.post_order()