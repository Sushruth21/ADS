'''2. Implement following tree traversals
a. Inorder
b. Preorder
c. Postorder
d. Levelorder'''

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder_traversal(root):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.key)
        result += inorder_traversal(root.right)
    return result

def preorder_traversal(root):
    result = []
    if root:
        result.append(root.key)
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
    return result

def postorder_traversal(root):
    result = []
    if root:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.key)
    return result

def levelorder_traversal(root):
    result = []
    if not root:
        return result

    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.key)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Example usage and assertions:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Inorder Traversal
assert inorder_traversal(root) == [4, 2, 5, 1, 6, 3, 7]

# Preorder Traversal
assert preorder_traversal(root) == [1, 2, 4, 5, 3, 6, 7]

# Postorder Traversal
assert postorder_traversal(root) == [4, 5, 2, 6, 7, 3, 1]

# Levelorder Traversal
assert levelorder_traversal(root) == [1, 2, 3, 4, 5, 6, 7]

print("All assertions passed!")
