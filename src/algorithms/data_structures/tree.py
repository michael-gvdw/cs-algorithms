# Binary Tree
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type='preorder'):
        return self.preorder_print(self.root, '')

    def preorder_print(self, node, traversal):
        if node:
            traversal += str(node.value) + "-"
            traversal = self.preorder_print(node.left, traversal)
            traversal = self.preorder_print(node.right, traversal)
        return traversal.rstrip(traversal[-1])

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree())
