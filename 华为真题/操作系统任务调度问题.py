# 题12 操作系统任务调度问题。
# 操作系统任务分为系统任务和用户任务两种。其中，系统任务的优先级 < 50，用户任务的优先级 >= 50且 <= 255。优先级大于255的为非法任务，应予以剔除。现有一任务队列task[]，长度为n，task中的元素值表示任务的优先级，数值越小，优先级越高。函数scheduler实现如下功能，将task[]中的任务按照系统任务、用户任务依次存放到 system_task[]数组和user_task[]数组中（数组中元素的值是任务在task[]数组中的下标），并且优先级高的任务排在前面，优先级相同的任务按照入队顺序排列（即先入队的任务排在前面），数组元素为-1表示结束。 例如：

# task[] = {0, 30, 155, 1, 80, 300, 170, 40, 99}
# system_task[] = {0, 3, 1, 7, -1}
# user_task[] = {4, 8, 2, 6, -1}

# 函数接口

# void scheduler(int task[], int n, int system_task[], int user_task[])