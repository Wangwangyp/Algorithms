# 双端队列
class Deque:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    # 将元素添加到双端队列的前端
    def addFront(self,item):
        self.items.append(item)

    # 将元素添加到双端队列的后端
    def addRear(self,item):
        self.items.insert(0,item)

    # 从双端队列前端移除一个元素
    def removeFront(self):
        return self.items.pop()

    # 从双端队列后端移除一个元素
    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# 回文检测器
def palchecker(string):
    d=Deque()

    for ch in string:
        d.addRear(ch)

    stillEqual=True

    while d.size()>1 and stillEqual:
        first=d.removeFront()
        last=d.removeRear()
        if first!=last:
            stillEqual=False

    return stillEqual