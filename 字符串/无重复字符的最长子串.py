# #coding:utf-8
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

#思路：双指针+set判断元素是否出现
class Solution():
    def LengthOfLongestString(self, s):
        if not s:return 0
        length = len(s)
        i,j,result=0,0,0
        letter = set()
        while i < length and j < length:
            if s[j] not in letter:
                letter.add(s[j])
                j += 1
                result = max(j-i, result)
                print(letter)
            else:
                letter.remove(s[i])
                i += 1
        return result

#增加一个问题，返回最长子串
class Solution():
    def LengthOfLongestString(self, s):
        if not s:return 0
        length = len(s)
        i,j,result=0,0,''
        letter = set()
        while i < length and j < length:
            if s[j] not in letter:
                letter.add(s[j])
                j += 1
                if j - i > len(result):
                    result = s[i:j]
            else:
                letter.remove(s[i])
                i += 1
        return result


if __name__=='__main__':
    s='aasdffdaweasdfsadff'
    print(Solution().LengthOfLongestString(s))

