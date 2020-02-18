# 题8 子串分离
# 通过键盘输入任意一个字符串序列，字符串可能包含多个子串，子串以空格分隔。请编写一个程序，自动分离出各个子串，并使用,将其分隔，并且在最后也补充一个,并将子串存储。 如果输入abc def gh i d，结果将是abc,def,gh,i,d,

# 要求实现函数：

# void DivideString(const char * pInputStr, long lInputLen, char * pOutputStr); 
# 【输入】
# pInputStr：输入字符串
# lInputLen：输入字符串长度

# 【输出】
# pOutputStr：输出字符串，空间已经开辟好，与输入字符串等长；

# 【注意】
# 只需要完成该函数功能算法，中间不需要有任何IO 的输入输出

# 示例
# 输入：abc def gh i d
# 输出：abc,def,gh,i,d,