global null
null=''
def minDepth(root):
    if not root:
        return 0

    if not root.left:
        return minDepth(root.right) + 1

    if not root.right:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1

class BTree(object):
    # 初始化
    def __init__(self, data=None, left=None, right=None):
        self.data = data    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

# 利用列表构造二叉树
def create_BTree_By_List(array):

    i = 1
    # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
    level_order = []
    sum = 1

    while sum < len(array):
        level_order.append(array[i-1:2*i-1])
        i *= 2
        sum += i
    level_order.append(array[i-1:])

    # BTree_list: 这一层所有的节点组成的列表
    # forword_level: 上一层节点的数据组成的列表
    def Create_BTree_One_Step_Up(BTree_list, forword_level):

        new_BTree_list = []
        i = 0
        for elem in forword_level:
            root = BTree(elem)
            if 2*i < len(BTree_list):
                root.left = BTree_list[2*i]
            if 2*i+1 < len(BTree_list):
                root.right = BTree_list[2*i+1]
            new_BTree_list.append(root)
            i += 1

        return new_BTree_list

    # 如果只有一个节点
    if len(level_order) == 1:
        return BTree(level_order[0][0])
    else: # 二叉树的层数大于1

        # 创建最后一层的节点列表
        BTree_list = [BTree(elem) for elem in level_order[-1]]

        # 从下往上，逐层创建二叉树
        for i in range(len(level_order)-2, -1, -1):
            BTree_list = Create_BTree_One_Step_Up(BTree_list, level_order[i])

        return BTree_list[0]

array = eval(input())
tree = create_BTree_By_List(array)
print(minDepth(tree)-1)
