#coding:utf-8
#输入一个偶数，求出两个素食之和等于该偶数的最接近的素数对
import math

class Solution():
    def is_prime(self, num): 
        sqrt_num = int(math.sqrt(num))
        for j in range(2, sqrt_num + 1):  # 从2到number的算术平方根迭代
            if num % j == 0:  # 判断j是否为number的因数
                return False
        return True

    def neighbour_num(self, num):
        m = num // 2
        for i in range(m):
            if self.is_prime(m-i) and self.is_prime(m-i):
                return m-i,m+i
        return None

if __name__=='__main__':
    num = 987
    print(Solution().neighbour_num(num))
    