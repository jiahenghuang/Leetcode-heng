#coding:utf-8
#堆排序这个东西可恶心了。因为它涉及到的东西很多。。
#首先必须知道堆是啥东西.
#堆是完全二叉树。分为大顶堆和小顶堆。大顶堆就是根节点大于左右叶子节点。
#完全二叉树是：倒数第二层全是满堆，只有最后一层可能不满。但是都指向左边元素。意思就是有左叶子结点才能有右叶子节点。
#优先队列可以使用堆进行实现，这样时间复杂度比较低。优先队列可以用来排序，降低时间复杂度。优先队列指的是堆从根节点到叶子节点是有一个优先顺序的。因为大顶堆和小顶堆的特点。。
#完全二叉树有个特点，就是根节点和子节点的位置是可以推算出来的。譬如父节点是i，那么左右孩子节点是2*i和2*i+1。反过来知道
# 思想参考：https://www.jianshu.com/p/d174f1862601

#思路是首先构建一个大顶堆。当给出一个数组的时候，意味着第一个大顶堆谁当儿子谁当爸爸已经确定了。构建一个大顶堆并没有将所有元素都排好序列。只是局部排序。
#怎样构建第一个大顶堆？ 从下往上，从右往左。

def buildMaxHeap(arr):
    for i in range(len(arr)//2,-1,-1):#构建堆由下往上构建所以用-1
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1  #每次踢掉求出的最大值
        heapify(arr, 0)
    return arr

if __name__=='__main__':
    arr=[1,3,2,4,6,2,1000,9]
    print(heapSort(arr))