#coding:utf-8

# 给出一个字符串，将重复的字符去除，仅保留第一次出现的字符，且保持去重后的字符在原字符串中的顺序不变。
# 输入数据是一个字符串（不包含空格）
# 输出去重后的字符串
# 输入：12ere2
# 输出：12er

#考的是hash的概念
#python中set查找使用hash实现，时间复杂度为o(1)
#本次实现复杂度o（n）
class Solution():
    def remove_repeat(self,s):
        chara_set = set()
        result = ''
        for i in s:
            if chara_set.__contains__(i)==False:
                result += i
                chara_set.add(i)
        return result

if __name__=='__main__':
    s = '12ere2'
    print(Solution().remove_repeat(s))

