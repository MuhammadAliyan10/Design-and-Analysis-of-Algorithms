class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root= None
    def height(self,node):
        if not node:
            return 0
        return node.height
    def balanceFactor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right))+ 1
        x.height = max(self.height(x.left), self.height(x.right))+ 1
        return x
    
    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right))+ 1
        y.height = max(self.height(y.left), self.height(y.right))+ 1
        return y
    
    def insert(self, root, value):
        if not root:
            return Node(value)
        
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balanceFactor(root)
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def insertValue(self, value):
        self.root = self.insert(self.root, value)
        
    def printTree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left or root.right:
                if root.left:
                    self.printTree(root.left, level + 1, prefix="L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    self.printTree(root.right, level + 1, prefix="R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

# Example usage:
avl_tree = AVLTree()

avl_tree.insertValue(25)
avl_tree.insertValue(29)
avl_tree.insertValue(30)
avl_tree.insertValue(15)
avl_tree.insertValue(12)
avl_tree.insertValue(14)
avl_tree.insertValue(10)
avl_tree.insertValue(9)
avl_tree.insertValue(45)
avl_tree.insertValue(47)

print("AVL Tree structure:")
avl_tree.printTree(avl_tree.root)
        


