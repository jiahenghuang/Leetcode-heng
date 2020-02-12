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
