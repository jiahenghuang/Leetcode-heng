#coding:utf-8
class Solution():
    def bottle(self, num):
        if num == 1:return 0
        if num == 2:return 1
        if num == 3:return 1
        result = num // 3
        num = num //3 + num % 3
        while num//3 > 0:
            result += num // 3
            num = num // 3 + num % 3
        if num % 3 == 0 or num % 3 == 1:
            return result
        return result + 1

if __name__=='__main__':
    # while int(input()) != 0:
    #     num = int(input())
    #     print(Solution().bottle(num))
    print(Solution().bottle(59))