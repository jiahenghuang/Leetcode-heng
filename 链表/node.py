#coding:utf-8
#线性表包括顺序表、单链表、双链表、循环链表等。
#顺序表怎样实现？
#python中等list就是动态顺序表。动态等意思是存储空间用完了会再申请一个同样大小的存储区。
#动态顺序表的有点：
#1. 基于下标访问，非常高效，时间复杂度为o(1)
#2. 尾端插入时间复杂度为o(1),其他位置插入，需要移动元素，因为是连续存储区。平均时间复杂度是o(n^2)
#3. 计算动态顺序表大小len(.)是o(1)时间复杂度，因为表中会计算元素个数。
#4. 删除顺序表的时间复杂度是o(1)具体原因不需要知道。
#5. 删除单链表的时间复杂度也是o(1)，原因很简单，设置表头节点的指针域为none即可

#单链表
#为什么需要单链表？
#1. 顺序表缺点：插入元素和删除元素时间复杂度高，因为需要移动元素。
#   为了改进移动元素的时间复杂度，将指针引入线性表。就是当前元素会用指针指向下一个元素。当插入或者删除元素的时候，只需要改变某个元素的指针即可。
#2. 但是从上面可以看出单链表的缺点是：查找比较麻烦。因为不具备顺序表里面的下标访问。意味着查找需要耗费平均o(n)的时间复杂度，但是真正使用的时候可以配合hash一起使用
#   另外一个缺点，指针需要耗费内存。
#   一个优点：不像顺序表那样需要一块连续存储区，可以利用碎片化的存储。
#3. 单链表需要一个表节点，表头变量，表头指针。就是当你打算用单链表存储数据的时候，第一个表节点是没有数据的。为什么呢？
#   假如说判断一个单链表是否是空表，如果没有表头你怎么判断呢？
#   没办法判断。一般判断方法是head.next是否为none。但是第一个表头的数据域也是需要存储数据的，但是这个数据可以随意设置，我们看的是表头的 指针域

#实现一个单链表：
class LNode():
    def __init__(self,elem, next_=None):
        self.elem=elem
        self.next=next_

#举个例子，你需要将1，2，3，4，5 使用单链表顺序存储
head=LNode(0)
head.next=LNode(1)
LNode(1).next=LNode(2)
LNode(2).next=LNode(3)
LNode(3).next=LNode(4)
LNode(4).next=LNode(5)
LNode(5).next=None

#表元素删除：
#如果要删除表头，则
head.next=LNode(2)即可
#如果想删除3这个元素：
LNode(2).next=LNode(4)
#给定一个链表，删除尾端元素。电脑是不会知道最后一个元素是什么的。
#双指针
if head is None:return 
fast=head

while fast.next:
    slow=fast
    fast=fast.next
slow.next=None

或者
while fast.next.next:
    fast=fast.next
fast.next=None

从链表里面查找一个元素，并将其删除
def find(e):
    p=head
    while p.next:
        if p.next.elem==e:
            break
        p=p.next
    p.next=p.next.next

#单链表的缺点
尾端插入需要遍历所有元素
#循环单链表就是为了改进单链表的这个缺点，将指针放在尾部，指向最后一个元素，最后一个元素右指向首元素。
#因为指针知道，很容易查找到最后一个元素，rear.next,也很好查找到第一个元素rear.next.next,时间复杂度都是o(1)
class LNode():
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_
#一个疑问，这里用了self._rear这个指针，之前首节点都是用一个包括数据域和指针域，其实无所谓，首节点数据无意义，不用也罢，这个实现感觉更规范一些
class LCList:
    def __init__(self):
        self._rear = None
    
    def is_empty(self):
        return self._rear is None
    
    def pre_append(self,e): #前端插入
        p = LNode(e)
        if self._rear is None:
            self._rear=p #self._rear就是head.next
            p.next=p #指针指向首元素，也就是自身
        else:
            p.next=self._rear.next  #首先将首元素作为p.next节点
            self._rear.next=p

    def append(self,e):   #尾端插入
        p = LNode(e)
        if self._rear is None:
            self._rear=p #self._rear就是head.next
            p.next=p #指针指向首元素，也就是自身
        else:
            p.next=self._rear.next
            self._rear.next=p
            self._rear=p

    def pre_del(self):  #首元素删除
        if self._rear is None:return
        self._rear.next=self._rear.next.next

    def tail_del(self):
        #尾端删除不是循环单链表的强处，需要o(n)时间复杂度

#对链表的所有想法进行遍历，肯定会想到双链表
#双链表不过是多了个前向指针，并且head节点的pre指针指向了尾元素
def DLNode(LNode):
    def __init__(self,elem,prev=None,next_=None)
        LNode.__init__(self,elem,next_)
        self.prev=prev

class DLList:
    def __init__(self):
        self.head=None
        self.rear=None
    
    def append(self,elem):
        p=DLNode(elem)
        if self.head is None:
            self.head=p
            self.rear=p
        else:
            p.next=self.rear.next
            p.prev=self.rear
            self.rear=p
    
    def head_insert(self, elem):
        p=DLNode(elem)
        if self.head is None:
            self.head=p
            self.rear=p
        else:
            self.head.next.prev=p
            self.rear.next=p
            self.head=p

    def head_del(self)
        if self.head is None:raise False
        self.head=self.head.next
    
    def tail_del(self):
        if self.head is None:raise error
        self.tail.prev=self.tail.next

#循环双链表没什么用，功能使用双链表就能实现







