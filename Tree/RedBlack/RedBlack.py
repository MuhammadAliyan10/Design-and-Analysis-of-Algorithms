class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED" 
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  
        self.TNULL.color = "BLACK"  
        self.root = self.TNULL

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _fix_insert(self, k):
        while k.parent.color == "RED": 
            if k.parent == k.parent.parent.right: 
                uncle = k.parent.parent.left
                if uncle.color == "RED": 
                    uncle.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  
                        k = k.parent
                        self._rotate_right(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._rotate_left(k.parent.parent)
            else: 
                uncle = k.parent.parent.right
                if uncle.color == "RED":  
                    uncle.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right: 
                        k = k.parent
                        self._rotate_left(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._rotate_right(k.parent.parent)
        self.root.color = "BLACK" 

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "RED" 


        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self._fix_insert(node)

    def _pre_order_helper(self, node):
        if node != self.TNULL:
            print(node.data, end=' ')
            self._pre_order_helper(node.left)
            self._pre_order_helper(node.right)

    def pre_order(self):
        self._pre_order_helper(self.root)

    def _in_order_helper(self, node):
        if node != self.TNULL:
            self._in_order_helper(node.left)
            print(node.data, end=' ')
            self._in_order_helper(node.right)

    def in_order(self):
        self._in_order_helper(self.root)

    def _post_order_helper(self, node):
        if node != self.TNULL:
            self._post_order_helper(node.left)
            self._post_order_helper(node.right)
            print(node.data, end=' ')

    def post_order(self):
        self._post_order_helper(self.root)
