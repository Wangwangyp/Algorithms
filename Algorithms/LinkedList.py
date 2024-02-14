# 构造节点
class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# 构造链表
class UnorderedList():
    # 初始化链表（默认为空链表）
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表的长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # 记录数量
        count = 0
        while cur != None:
            count += 1
            # 将游标赋给下一个
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            # 打印游标指向的节点
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部增加元素"""
        node = Node(item)
        # 先将新节点的next区域指向第一个节点的值
        node.next = self.__head
        # 再将__head指向新节点
        self.__head = node

    def append(self, item):
        """链表尾部增加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                # 移动游标，当下一个为None，退出循环，当前的cur为最后一个节点
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置插入元素
        :param pos 从0开始!!
        """
        # 空链表
        if pos <= 0:
            self.add(item)
        # 插入值的位置大于链表长度-1，证明在链表末尾
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            # 当循环的次数小于插入指定位置的参数-1，那么当前为要插入位置的前一个位置
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 循环完之后pre指向的是要插入的前一个节点,即pos-1位置
            node = Node(item)
            # 将目标数的next区域指向下一个的值
            node.next = pre.next
            # 将前一个位置的next指向插入值
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        # 被删除元素位置的前一个节点
        pre = None
        while cur != None:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:  # 或写成   if pre==None:
                    self.__head = cur.next
                else:
                    # 将前一个的next指向当前游标的next的指向（即下一个值）
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def get_node(self,pos):
        """查找第pos位元素是什么"""
        node=self.__head
        for i in range(pos):
            node=node.next
        return node.elem


# 有序链表   目前认为是升序排列
class OderedList:
    def __init__(self):
        self.__head=None

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表的长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # 记录数量
        count = 0
        while cur != None:
            count += 1
            # 将游标赋给下一个
            cur = cur.next
        return count

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        # 被删除元素位置的前一个节点
        pre = None
        while cur != None:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:  # 或写成   if pre==None:
                    self.__head = cur.next
                else:
                    # 将前一个的next指向当前游标的next的指向（即下一个值）
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur=self.__head
        found=False
        stop=False
        while cur!=None and not found and not stop:
            if cur.elem==item:
                found=True
            else:
                if cur.elem>item:
                    stop=True
                else:
                    cur=cur.next
        return found

    def add(self,item):
        cur=self.__head
        pre=None
        stop=False
        while cur!=None and not stop:
            if cur.elem>item:
                stop=True
            else:
                pre=cur
                cur=cur.next
        temp=Node(item)
        if pre==None: # 如果是头节点插入
            temp.next=self.__head
            self.__head=temp
        else:
            temp.next=cur
            pre.next=temp


if __name__ == '__main__':
    print("+++UnorderList+++\n")
    ll = UnorderedList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)

    print(ll.is_empty())
    print(ll.length())
    print(ll.get_node(0))

    ll.add(8)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.travel()
    print(ll.get_node(3))

    ll.insert(7, 10)
    ll.travel()

    ll.remove(1)
    ll.travel()
    print("\n+++OrderedList+++\n")
    ll1 = OderedList()
    ll1.add(3)
    ll1.add(2)
    ll1.add(1)
    print(ll1.search(3))
    ll1.add(4)
    print(ll1.search(4))
