def count_sort(arr):
    # Find the range of the array
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    # Create a counting array
    count_array_size = max_val - min_val + 1
    count_array = [0] * count_array_size

    # Count the occurrences of each element
    for num in arr:
        count_array[num - min_val] += 1

    # Modify the count array to store actual positions
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):
        index = count_array[num - min_val] - 1
        output[index] = num
        count_array[num - min_val] -= 1

    return output

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            # Duplicate keys are not allowed
            return root

        self.update_height(root)

        balance = self.balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.key)
            self.inorder_traversal(root.right, result)

    def sort_array(self, arr):
        # Create a new AVL tree
        avl_tree = AVLTree()

        # Insert all elements from the array into the AVL tree
        for item in arr:
            avl_tree.insert_key(item)

        # Perform an inorder traversal to get the sorted array
        sorted_arr = []
        avl_tree.inorder_traversal(avl_tree.root, sorted_arr)

        return sorted_arr