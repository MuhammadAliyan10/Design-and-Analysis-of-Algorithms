class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.value:
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

    def search(self, root, value):
        if root is None:
            return False
        if value == root.value:
            return True
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

if __name__ == "__main__":
    bst = BinarySearchTree()
    data_to_insert = [50, 30, 20, 40, 70, 60, 80]
    
    for data in data_to_insert:
        bst.insert(data)
    
    print("Pre-order Traversal:")
    bst.preOrderTraversal(bst.root)
    print("\nIn-order Traversal:")
    bst.inOrderTraversal(bst.root)
    print("\nPost-order Traversal:")
    bst.postOrderTraversal(bst.root)
    

    search_values = [30, 90]
    for value in search_values:
        print(f"Searching for {value}: {'Found' if bst.search(bst.root, value) else 'Not Found'}")
