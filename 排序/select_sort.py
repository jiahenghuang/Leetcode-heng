#coding:utf-8
#选择排序的思想就是：找到列表里面所有的最小的元素放在第一个位置，交换第一个位置和最小元素的位置，然后找第二个最小的元素，找到之后交换位置....

# class SelectSort:
def sort(data):
    if not data:return
    for i in range(len(data)-1):
        min=i
        for j in range(i+1,len(data)):
            if data[j]<data[min]:
                min=j
        if min != i:
            tmp=data[min]
            data[min]=data[i]
            data[i]=tmp
    return data

if __name__=='__main__':
    data=[1,8,2,10]
    print(sort(data))

