# 题16 字符串四则运算
# 问题描述： 输入一个只包含个位数字的简单四则运算表达式字符串，计算该表达式的值。

# 注意：

# 表达式只含 +, -, *, / 四则运算符，不含括号
# 表达式数值只包含个位整数(0-9)，且不会出现0作为除数的情况
# 要考虑加减乘除按通常四则运算规定的计算优先级
# 除法用整数除法，即仅保留除法运算结果的整数部分。比如8/3=2。输入表达式保证无0作为除数情况发生
# 输入字符串一定是符合题意合法的表达式，其中只包括数字字符和四则运算符字符，除此之外不含其它任何字符，不会出现计算溢出情况
# 要求实现函数：

# int calculate(int len,char * expStr)
# 【输入】
# int len: 字符串长度； char *expStr: 表达式字符串;
# 【输出】
# 无
# 【返回】
# 计算结果

# 示例:

# 输入：char * expStr = “1+4*5-8/3” 函数返回：19
# 输入：char * expStr = “8/3*3” 函数返回：6
