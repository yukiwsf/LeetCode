"""深度优先搜索DFS"""
# 非递归用stack记录经过结点
def Preorder(self, root):
    """递归实现先序遍历，根左右"""
    if not root:
        return
    print(root.value)
    self.Preorder(root.left)
    self.Preorder(root.right)

def Inorder(self, root):
    """递归实现中序遍历，左根右"""
    if not root:
        return
    self.Inorder(root.left)
    print(root.value)
    self.Inorder(root.right)

def Postorder(self, root):
    """递归实现后序遍历，左右根"""
    if not root:
        return
    self.Postorder(root.left)
    self.Postorder(root.right)
    print(root.value)

"""广度优先搜索BFS"""
def Breadth(self, root):
    """循环实现层序遍历"""
    if not root:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def Inorder1(self, root):
    """循环实现中序遍历"""
    if not root:
        return list()
    stack = []
    res = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            root = stack.pop()
            res.append(root.value)
            root = root.right
    return res

def Preorder1(self, root):
    """循环实现先序遍历"""
    if not root:
        return list()
    stack = []
    res = []
    while root or stack:
        while root:
            res.append(root.value)
            stack.append(root)
            root = root.left
        if not stack:
            root = stack.pop()
            root = root.right
    return res

def Postorder1(self, root):
    """循环实现后序遍历"""
    if not root:
        return list()
    stack = list()
    res = list()
    prev = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            res.append(root.value)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right
    return res