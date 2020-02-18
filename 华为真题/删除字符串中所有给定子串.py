# 题14 删除字符串中所有给定的子串
# 问题描述：
# 在给定字符串中查找所有特定子串并删除，如果没有找到相应子串，则不作任何操作。 要求实现函数：

# int delete_sub_str(const char * str, const char * sub_str, char * result_str)
# 【输入】
# str：输入的被操作字符串
# sub_str：需要查找并删除的特定子字符串
# 【输出】
# result_str：在str字符串中删除所有sub_str子字符串后的结果
# 【返回】
# 删除的子字符串的个数

# 注意：

# 子串匹配只考虑最左匹配情况，即只需要从左到右进行字串匹配的情况。比如： 在字符串abababab中，采用最左匹配子串aba,可以匹配2个aba字串。如果匹配出从左到右位置2开始的aba，则不是最左匹配，且只能匹配出1个aba字串。
# 输入字符串不会超过100 Bytes，请不用考虑超长字符串的情况。
# 示例
# 输入：str = abcde123abcd123 sub_str = 123
# 输出：result_str = abcdeabcd 返回：2
# 输入：str = abcde123abcd123 sub_str = 1234
# 输出：result_str = abcde123abcd123 返回：0