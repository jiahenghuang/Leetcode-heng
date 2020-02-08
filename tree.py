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


#使用迭代实现深度优先和宽度优先
#迭代法需要使用栈和队列

#首先考虑队列的实现
#队列
#使用列表实现队列。因为python的列表是动态顺序表。动态顺序表通过下标访问元素，使用一块连续的存储，当数据量大的时候，就扩充一块存储区
class SQueue():
    def __init__(self,init_len=10):
        self._len=init_len
        self._head=0  #表示首元素的位置
        self._num=0  #队列长度
        self._elems=[0]*init_len  #用列表来模拟，这一块连续的存储区都是0

    def is_empty(self):  #判断队列是否为空
        return self._num == 0
    
    def dequeue(self):  #出列
        #首先判断队列是否为空
        if self._num == 0:return
        #出列的时候指针需要后移1
        self._head += 1
        self._num -= 1  #出列一个元素就要将队列的长度减少一个
        return self._elems[self._head-1]

    def enqueue(self,e):  #入列
        #首先判断队列是否满了
        if self._num == self._len:
            #扩充动态顺序表
            self._elems += [0]*self._len
        #扩充万动态顺序表之后需要将self._len*2
        self._len *= 2
        #将新来元素放在末尾
        self._elems[self._head+self._num]=e
        self._num += 1
        
#实现栈。栈就是后入先出。仍然使用动态顺序表实现栈
def SStack():
    def __init__(self,init_len=10):
        self._num=0
        self._head=0
        self._tail=0
        self._len=init_len
        self._elems=[0]*self._len
    
    def is_empty(self):
        return self._num==self._len

    def pop(self):  #出栈
        if self.is_empty:
            return
        self._elems[self._tail]=0
        self._tail -= 1
        self._num -= 1

    def push(self,e):  #入栈
        #首先判断栈是否满
        if self._len==self._num:
            #扩展栈空间
            self._elems += [0]*self._len
        self._elems[self._tail+1]=e
        self._len *= 2

