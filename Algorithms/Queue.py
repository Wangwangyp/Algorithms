class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    # 入队
    def enqueue(self,item):
        self.items.insert(0,item)

    #出队
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# 传土豆      假设有土豆的孩子在队列头部，将此孩子名字移出队列，再放入队尾，num次后，队头的名字被移除，直至剩最后一个孩子
def hotPotato(namelist,num):
    q=Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

