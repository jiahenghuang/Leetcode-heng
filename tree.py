#coding：utf-8
#二叉树节点类
class BinTNode:
    def __init__(self,dat,left=None,right=None):
        self.data=dat
        self.left=left
        self.right=right
    
#创建一颗树
t=BinTNode(1,BinTNode(1),BinTNode(2))

#统计树中节点个数
def countBinTNode(t):
    if t is None:
        return 0
    return 1+countBinTNode(t.left)+countBinTNode(t.right)

#为什么要加1？ 
#递归看起来比较别扭，怎么理解？
#来看t这棵树。当执行到countBinTNode(t)的时候，会返回1+countBinTNode(t.left)+countBinTNode(t.right)=1+countBinTNode(BinTNode(1))+countBinTNode(BinTNode(2))
#=1+（1+countBinTNode(BinTNode(1).left)+countBinTNode(BinTNode(1).right)）+（1+countBinTNode(BinTNode(2).left)+countBinTNode(BinTNode(2).right）)
#=1+(1+countBinTNode(None)+countBinTNode(None))+(1+countBinTNode(None)+countBinTNode(None))=1+1+1=3
print(countBinTNode(t))

#统计一颗二叉树里面所有数值的和
def sum_BinTNodes(t):
    if t is None:
        return 0
    return t.dat+sum_BinTNodes(t.left)+sum_BinTNodes(t.right)

print(sum_BinTNodes(t))
#1+sum_BinTNodes(t.left)+sum_BinTNodes(t.right)=1+sum_BinTNodes(BinTNode(1))+sum_BinTNodes(BinTNode(2))
#=1+(1+sum_BinTNodes(BinTNode(1).left)+sum_BinTNodes(BinTNode(1).right))+(2+sum_BinTNodes(BinTNode(2).left)+sum_BinTNodes(BinTNode(2).right))
#=1+1+2=4

#比较两者不同，一个return里面有加1一个不加，为什么？
#1可以理解为根节点。碰到不知道要不要加的问题的时候可以想一种特殊情况，仅仅有一个根节点的树。这个时候如果不加1会直接返回0，明显不对。
#另外一种思路就是统计书中节点的时候1其实就是t的某个属性，这个根节点的属性就是1


