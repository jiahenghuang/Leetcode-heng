# 题2
# 通过键盘输入一串小写字母(a~z)组成的字符串。请编写一个字符串压缩程序，将字符串中连续出席的重复字母进行压缩，并输出压缩后的字符串。
# 压缩规则：
# 仅压缩连续重复出现的字符。比如字符串abcbc由于无连续重复字符，压缩后的字符串还是abcbc
# 压缩字段的格式为"字符重复的次数+字符"。例如：字符串xxxyyyyyyz压缩后就成为3x6yz
# 要求实现函数：
# void stringZip(const char * pInputStr, long lInputLen, char * pOutputStr);
# 【输入】
# pInputStr：输入字符串
# lInputLen：输入字符串长度
# 【输出】
# pOutputStr：输出字符串，空间已经开辟好，与输入字符串等长；
# 【注意】
# 只需要完成该函数功能算法，中间不需要有任何IO的输入输出
# 示例
# 输入：cccddecc 输出：3c2de2c
# 输入：adef 输出：adef
# 输入：pppppppp 输出：8p

#依然没用到什么数据结构算法。。。
class Solution():
    def tar_cvf_char(self, s):
        if not s:return
        result = ''
        left_rear,right_rear = 0,0
        while right_rear < len(s):
            if s[left_rear] == s[right_rear]:
                right_rear += 1
            else:
                if right_rear - left_rear > 1:
                    result += str(right_rear - left_rear)+s[left_rear]
                else:
                    result += s[left_rear]
                left_rear = right_rear
        if len(s)-left_rear > 1:
            result += str(len(s)-left_rear)+s[-1]
        else:
            result += s[-1]
        return result
                
if __name__=='__main__':
    s='adefg'
    print(Solution().tar_cvf_char(s))
