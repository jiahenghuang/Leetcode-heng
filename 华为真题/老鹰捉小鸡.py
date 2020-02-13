#coding:utf-8
# 第一道题目是一个老鹰捉小鸡的问题，考虑一下边界问题就好了。有一个小鸡序列，有一个攻击序列，如果老鹰攻击小鸡 i， 
# 母鸡保护小鸡 j，如果 i == j 那就攻击失败，否则攻击成功（如果攻击的位置合法，小于队列长度，保护也一样），被
# 攻击的小鸡从队列中移除，最后如果队列只剩一只小鸡则失败，如果n轮后还有超过一只存活则成功。

def isPrime(a):
    for n in range(2,a):
        if a%n==0:
            return False
    return True

while True:
    try:
        n = int(input())
        m = int(n/2)
        for i in range(n):
            if isPrime(m-i) and isPrime(m+i):
                print(m-i)
                print(m+i)
                break
    except:
        break

