n = int(input())
string = input().split(" ")
nums = []
for i in string:
    nums.append(int(i))


class TreeNote(object):  # 创建树的结点
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):  # 创建二叉树
    def __init__(self):
        self.root = None  # 根结点

    def add(self, val):  # 二叉树添加结点
        node = TreeNote(val)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if temp_node.left is None:
                temp_node.left = node
                return
            else:
                queue.append(temp_node.left)
            if temp_node.right is None:
                temp_node.right = node
                return
            else:
                queue.append(temp_node.right)

    def inorderTraversal(self, root):
        if root == None or root.val == -1:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right


t = BinaryTree()

for i in nums:
    t.add(i)

temp = t.inorderTraversal(t.root)
ans = []
if len(temp) > 2:
    for i in range(1, len(temp) - 1):
        ans.append(temp[i - 1] + temp[i + 1])
    ans = [temp[1]] + ans
    ans = ans + [temp[-2]]
    print(ans)
elif len(temp) == 1:
    print(ans)

