#coding:utf-8
#归并排序
#归并排序
  
def merge(left, right):
    result = []
    i = j = 0
    while len(left) > i and len(right)>j:
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(l):
    if len(l) <= 1:
        return l
    moddle = len(l)//2
    left = merge_sort(l[0: moddle])
    right = merge_sort(l[moddle: len(l)])
    print('left:', left) 
    print('right:', right)
    return merge(left, right)

if __name__=='__main__':
    arr=[3,21,1,4,8,32,9,2]
    print(merge_sort(arr))