#coding:utf-8
#动态规划也不知道为啥叫动态规划，根据见过的题目和机器学习算法中遇到的，不过就是发现第n项和前几个项的一种关系。就是f(n)=g(n-1)+s(n-2),如fib(n)=fib(n-1)+fib(n-2)
#然后求出初始值。就可以利用初始值，配合递归，求解出来
#动态规划题目一般分成两类：一维数组和二维数组，都用列表实现即可


#例子1 fibnacci数列问题
fib(1)=1
fib(2)=1
fib(3)=fib(1)+fib(2)
fib(n)=fib(n-1)+fib(n-2)

#求第n项fib值
class Solucion():
    def fib(self,n):
        if n == 1:return 1
        if n == 2:return 1
        if n >2:
            return fib(n-1)+fib(n-2)

#但是问题往往不是那么简单的。很多考官想考逆向思维。需要倒着想
#问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

#思考：记跳上第n个台阶有s(n)种跳法，那跳上第n-1有s(n-1)种跳法。跳上第n-2个台阶有s(n-2)种跳法。
#青蛙如果想跳到第n个阶梯，必须经过第n-1个阶梯（跳一步）或者第n-2个阶梯（跳2个），这样就可以得出s(n)=s(n-1)+s(n-2)

s(1)=1
s(2)=2
s(3)=3
class Solucion():
    def s(self,n):
        if n==1:return 1
        if n==2:return 2
        if n>2:
            return s(n-2)+s(n-1)

#一维数组的题目比较少而且简单，一般题目都是二维数组
#一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。问总共有多少条不同的路径？
#同理，解决这个问题的时候也是考虑，dp[i][j]=?考虑机器人不会飞，只能往右和往下，那dp[i][j]肯定经过dp[i-1][j]或者dp[i][j-1],显然dp[i][j]=dp[i-1][j]+dp[i][j-1]
#规律找到了之后，就是初始值的问题，初始值怎么求
#看到i-1和j-1首先就想到定义域问题
class Solucion():
    def robot(self,row=m,col=n):
        if row == 0:return
        if row== 1:return 1
        if col == 0:return 
        if col == 1:return 1
        for j in range(n):
            robot[0][j]=1
        for i in range(m):
            robot[i][0]=1
        return robot[m-1][n]+robot[m][n-1]

#给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#依然二维数组问题，不同的是求最小和路径。求最优路径问题。一个最简单的思路就是：遍历所有路径求一个min，但是这样肯定会超时
#思路仍然是动态规划，使用递归求解

dp[i][j]=min(dp[i-1][j],dp[i][j-1])+arr[i][j]
#其中dp[i][j]表示经过i，j点的最优路径。
class Solucion():
    def dp(self,row=m,col=n,arr=arr):
        if row == 0:return
        if row== 1:return sum(arr)  #不严谨，只写思想
        if col == 0:return 
        if col == 1:return sum(arr)  #不严谨，只写思想
        for j in range(n):
            dp[0][j]=1
        for i in range(m):
            dp[i][0]=1
        return min(dp[m-1,n],dp[m,n-1])+arr[m][n]

