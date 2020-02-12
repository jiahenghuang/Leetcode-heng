#coding:utf-8
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL     的节点将直接作为新二叉树的节点。
示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

#同样两种方法。递归为深度优先，迭代为广度优先

class Solution():
    def combineTree(self,t1,t2):
        if t1 is None and t2 is None:return None
        if t1 is None and t2 is not None:return t1
        if t1 is not None and t2 is None:return t2

        #但是，这个做加和的时候不能有None,否则会报bug.二叉树做递归，一定要有left和right分开，不然代码是不会知道还有left节点和right节点的
        t1.data += t2.data
        self.combineTree(t1.left,t2.left)
        self.combineTree(t1.right,t2.right)
        return t1


#可以看出都是同样的套路
#迭代：
class Solution():
    def combineTree(self,t1,t2):
        llist=[(t1,t2)]
        while llist:
            node1,node2 = llist.pop(0)
            node1.data += node2.data
            if node1.left and node2.left:
                llist.append((node1.left,node2.left))
            elif node1.left:
                node1.left=node2.left
            if node1.right and node2.right:
                llist.append((node1.right,node2.right))
            elif node1.right:
                node1.right=node2.right
        return t1
