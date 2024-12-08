class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)
    
    def preOrderTraversal(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def inOrderTraversal(self, node):
        if node is not None:
            self.inOrderTraversal(node.left)
            print(node.value, end=' ')
            self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node is not None:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.value, end=' ')

# Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    data_to_insert = [50, 30, 20, 40, 70, 60, 80]
    
    for data in data_to_insert:
        bt.insert(data)
    
    print("Pre-order Traversal:")
    bt.preOrderTraversal(bt.root)
    print("\nIn-order Traversal:")
    bt.inOrderTraversal(bt.root)
    print("\nPost-order Traversal:")
    bt.postOrderTraversal(bt.root)
