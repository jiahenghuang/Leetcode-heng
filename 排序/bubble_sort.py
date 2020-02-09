#coding:utf-8
#冒泡排序的思想就是相邻两个排序，如果两个顺序不对则交换

def sort(data):
    if not data:return
    for i in range(len(data)):
        for j in range(0,len(data)-i-1):  #关键点在这里。冒泡排序，每遍历一次这个泡冒到了哪里，冒到了最后一个元素
            if data[j] < data[j+1]:
                tmp=data[j]
                data[j]=data[j+1]
                data[j+1]=tmp
    return data

if __name__=='__main__':
    data=[2,1,4,2,9]
    print(sort(data))
