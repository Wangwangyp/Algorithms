# 二叉堆
class BinaryHeap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0

    # 向上交换
    def percUp(self,i):
        while i//2>0:
            if self.heaplist[i]<self.heaplist[i//2]:
                temp=self.heaplist[i//2]
                self.heaplist[i//2]=self.heaplist[i]
                self.heaplist[i]=temp
            i=i//2

    # 插入元素，为了保证堆的有序性，需要将新元素与父元素比较大小
    def insert(self,x):
        self.heaplist.append(x)
        self.currentsize=self.currentsize+1
        self.percUp(self.currentsize)

    # 向下交换
    def percDown(self,i):
        while (i*2)<=self.currentsize:
            mc=self.minChild(i)
            if self.heaplist[i]>self.heaplist[mc]:
                temp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[mc]
                self.heaplist[mc]=temp
            i=mc

    # 找最小元素
    def minChild(self,i):
        if i*2+1>self.currentsize:  # 是否有唯一子节点
            return i*2
        else:  # 返回较小的
            if self.heaplist[i*2]<self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1

    # 删除最小元素
    def delMin(self):
        retval=self.heaplist[1]  # 移走堆顶
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize=self.currentsize-1
        self.heaplist.pop()
        self.percDown(1)        # 新顶下移
        return retval  # 这是二叉堆，有序的，堆顶元素就是最小的，所以return它

    # 根据元素列表构建整个堆  O(n)
    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentsize=len(alist)
        self.heaplist=[0]+alist[:]
        while i>0:
            self.percDown(i)
            i=i-1