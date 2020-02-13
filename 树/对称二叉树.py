给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 ```[1,2,2,3,4,4,3]`` 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
    3   3
说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

#递归
class Solution():
    def symmetryTree(self,root):
        if root is None:return
        if root.left.data == root.right.data:
            return True
        else:
            return False
        if root.left  is None and root.right is None:
            return True
        if root.left is None and root.right is not None:
            return False
        if root.left is not None and root.right is None:
            return False
        return self.symmetryTree(root.left,root.right) and self.symmetryTree(root.right,root.left)
        
class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root or not (root.left or root.right):
			return True
		# 用队列保存节点	
		queue = [root.left,root.right]
		while queue:
			# 从队列中取出两个节点，再比较这两个节点
			left = queue.pop(0)
			right = queue.pop(0)
			# 如果两个节点都为空就继续循环，两者有一个为空就返回false
			if not (left or right):
				continue
			if not (left and right):
				return False
			if left.val!=right.val:
				return False
			# 将左节点的左孩子， 右节点的右孩子放入队列
			queue.append(left.left)
			queue.append(right.right)
			# 将左节点的右孩子，右节点的左孩子放入队列
			queue.append(left.right)
			queue.append(right.left)
		return True