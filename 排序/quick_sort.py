#coding:utf-8
#快排的思想就是分治法
#首先选择一个基准，一般取数组中间值，将一个数组划分成三块，大于的小于的等于的，递归的分别进行排序即可。

def quick_sort(arr):
    if len(arr)<=1:return arr
    pivot=arr[len(arr)//2]
    left=[i for i in arr if i < pivot]
    middle=[i for i in arr if i == pivot]
    right=[i for i in arr if i>pivot]
    return quick_sort(left)+quick_sort(middle)+quick_sort(right)



def quick_sort(arr, start, end):
    if start >= end:
        return
    left = start
    right = end
    mid = arr[left]
    while left < right:
        while left < right and arr[right] >= mid:
            right -= 1
        li[left] = li[right]
        while left < right and arr[left] < mid:
            left += 1
        arr[right] = arr[left]
    arr[left] = mid
    quick_sort(arr, start, left-1)

if __name__=='__main__':
    arr=[1,3,2,9,5,8,4]
    print(quick_sort(arr))


