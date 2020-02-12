#coding:utf-8
翻转一棵二叉树。
示例：
输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

#分析：可以采用迭代也可以采用递归
#递归
class Solution():
    def invertTree(self, root):
        #首先判断树是否非空
        if root is None:return None

        #采用递归的时候，一定要有一个初始值，不然就是个死循环，返回不出结果。
        #交换左右节点就是初始值。递归到最后的时候要做的事情就是：
        root.left,root.right=root.right,root.left
        #递归一个树的时候,为什么不是 self.invertTree(root)？而是：
        self.invertTree(root.left)
        self.invertTree(root.right)
        #因为如果是self.invertTree(root)，那第一步骤root.left,root.right=root.right,root.left就白交换了，导致第二层的树并没有交换
        #下面行代码是写死的
        return root


#迭代：
class Solution():
    def invertTree(self, root):
        if root is None:return None
        #使用队列来存储数据
        llist=[root]
        while llist:
            node=llist.pop(0)
            node.left,node.right=node.right,node.left
            if node.left:
                llist.append(node.left)
            if node.right:
                llist.append(node.right)
        return root





