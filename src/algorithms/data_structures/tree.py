from sequence import Queue, Stack

# node for binary tree
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# base binary tree class
class BinaryTree(object):

    def __init__(self, root=None):
        if root is None:
            self.root = None
        else: 
            self.root = Node(root)

    def exists(self, value):
        pass

    def find(self, value):
        pass

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    # return how deep a tree is from a given node
    def height(self, node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)

        return 1 + max(left, right)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def has_bst_property(self):
        if self.root:
            is_satisfied = self._has_bst_property(self.root, self.root.value)

            if is_satisfied is None:
                return True
            return False
        return True
    
    def _has_bst_property(self, current_node, value):
        if current_node.left:
            if value > current_node.left.value:
                return self._has_bst_property(current_node.left, current_node.left.value)
            else:
                return False
        if current_node.right:
            if value < current_node.right.value:
                return self._has_bst_property(current_node.right, current_node.right.value)
            else:
                return False
                
    def print_tree(self, mode='inorder'):
        if mode == 'preorder':
            return self._preorder(self.root, "")
        if mode == 'postorder':
            return self._postorder(self.root, "")
        if mode == 'levelorder':
            return self._levelorder(self.root)
        # if mode == 'levelorder-reverse':
        #     return self._levelorder_reverse(self.root)

        return self._inorder(self.root, "")

    ''' root -> left -> right '''
    def _preorder(self, node, traversal):
        if node:
            traversal += str(node.value) + " "
            traversal = self._preorder(node.left, traversal)
            traversal = self._preorder(node.right, traversal)
        return traversal
    
    ''' left -> root -> right '''
    def _inorder(self, node, traversal):
        if node:
            traversal = self._inorder(node.left, traversal)
            traversal += str(node.value) + " "
            traversal = self._inorder(node.right, traversal)
        return traversal
    
    ''' left -> right -> root '''
    def _postorder(self, node, traversal):
        if node:
            traversal = self._inorder(node.left, traversal)
            traversal = self._inorder(node.right, traversal)
            traversal += str(node.value) + " "
        return traversal

    def _levelorder(self, node):
        if node is None:
            return

        queue = Queue()
        queue.enqueue(node)
        
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek().value) + " "
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
    # def _levelorder_reverse(self, node):
    #     if node is None:
    #         return

    #     queue = Queue()
    #     stack = Stack()

    #     queue.enqueue(node)

    #     traversal = ""
    #     while len(queue) > 0:
    #         node = queue.dequeue()
    #         print(node.value)
    #         stack.push(node)

    #         if node.right:
    #             queue.enqueue(node.right)
    #         if node.left:
    #             queue.enqueue(node.left)
            
    #     while len(stack) > 0:
    #         node = stack.pop()
    #         traversal += str(node.value) + " "
        
    #     return traversal
        



# binary search tree
class BinarySearchTree(BinaryTree):

    # check weather a value exists in binary search tree
    # return True if it exists
    # return False if it does not exist
    # return None if no root node exists
    def exists(self, value):
        if self.root:
            is_found = self._exists(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _exists(self, value, current_node):
        if value < current_node.value and current_node.right:
            return self._exists(value, current_node.right)
        elif value > current_node.value and current_node.left:
            return self._exists(value, current_node.left)
        else:
            return True

    # find a value in binary search tree
    # return node if node.value exists
    # return None if node.value does not exist
    # return None if no root node exists
    def find(self, value):
        if self.root:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left:
            return self._find(value, current_node.left)
        elif value > current_node.value and current_node.right:
            return self._find(value, current_node.right)


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
                current_node.left.parent = current_node
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
                current_node.right.parent = current_node
            else:
                self._insert(value, current_node.right)
        else:
            print(f'Value {value} already exitst in BinarySearchTree')

    def delete_value(self, value):
        return self.delete_node(self.find(value))
        
    def delete_node(self, node):

        # return the node with min value in tree rooted at input node
        def min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        # return the number of children for the specified node
        def num_children(node):
            num_children = 0
            if node.left: num_children += 1
            if node.right: num_children += 1
            return num_children

        # get parent of node to be deleted
        node_parent = node.parent

        # get number of children of the node to be deleted
        node_num_children = num_children(node)

        # break operation into different cases based on the 
        # structure of the tree & node to be deleted

        # case 1 (node has no children)
        if node_num_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        
        # case 2 (node has a single children)
        if node_num_children == 1:
            # get the single child node
            if node.left:
                child = node.left
            else:
                child = node.right

            # replace the node to be deleted with its child
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            # correct the parent poiter in node
            child.parent = node_parent

        # case 3 (node has two children)
        if node_num_children == 2:
            # get the inorder successor of the deleted node
            succesor = min_value_node(node.right)
            
            # copy the inorder successor's value
            node.value = succesor.value

            # delete the inorder succesor now that it's value is
            # copied into the other node
            self.delete_node(succesor)


# below this is testing

binary = BinaryTree(1)
binary.root.left = Node(2)
binary.root.right = Node(3)
binary.root.left.left = Node(4)
binary.root.left.right = Node(5)

print(binary.has_bst_property())
print(binary.size(binary.root))
print(binary.height(binary.root))
print(binary.print_tree(mode='levelorder-reverse'))

print()

tree = BinarySearchTree()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(10)
tree.insert(9)
tree.insert(11)

print(tree.has_bst_property())
print(tree.size(tree.root))
print(tree.height(tree.root))
print(tree.print_tree(mode='levelorder-r'))

tree.delete_value(5)
print(tree.print_tree())

tree.delete_value(4)
print(tree.print_tree())

tree.delete_value(11)
print(tree.print_tree())

tree.delete_value(9)
print(tree.print_tree())