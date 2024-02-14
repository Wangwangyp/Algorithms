# 二叉搜索树    包含BinarySearchTree 和 TreeNode
class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # 返回一个迭代器，用于遍历二叉搜索树中的节点。
    def __iter__(self):
        return self.root.__iter__()

    # 构建二叉搜索树的方法
    def put(self,key,val):
        if self.root:
            self.__put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1

    # 递归辅助函数
    def __put(self,key,val,currentNode):
        if key==currentNode.key:
            currentNode.payload=val
        elif key<currentNode.key:
            if currentNode.hasLeftChild():
                self.__put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self.__put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key,value)

    # 获得值
    def get(self,key):
        if self.root:    # self.root!=None   不是空树
            res=self.__get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:      # self.root==None   是空树
            return None

    # 递归辅助函数
    def __get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return self.__get(key,currentNode.leftChild)
        else:
            return self.__get(key,currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.__get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size>1:
            nodeToRemove=self.__get(key,self.root)
            if nodeToRemove:
                self.__remove(nodeToRemove)
                self.size=self.size-1
            else:
                raise KeyError('Error,key not in tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1
        else:
            raise KeyError('Error,key not in tree')

    def __remove(self,currentNode):
        if currentNode.isLeaf():  # 叶子节点
            if currentNode==currentNode.parent.leftChild:
                currentNode.parent.leftChild=None
            else:
                currentNode.parent.rightChild=None
        elif currentNode.hasBothChildren():   # 有两个子节点
            succ=currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.payload=succ.payload
        else:    # 只有一个子节点
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent=currentNode.parent
                    currentNode.parent.leftChild=currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent=currentNode.parent
                    currentNode.parent.rightChild=currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent=currentNode.parent
                    currentNode.parent.leftChild=currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent=currentNode.parent
                    currentNode.parent.rightChild=currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,currentNode.rightChild.rightChild)


class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload=val  # 有效负载，值
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
        self.balanceFactor=0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild==self

    def isRightChild(self):
        return self.parent and self.parent.rightChild==self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChild(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self

    # 寻找后继节点
    def findSuccessor(self):
        succ=None
        if self.hasRightChild():
            succ=self.rightChild.findMin()
        else:
            if self.parent:
                succ=self.parent
            else:
                self.parent.rightChild=None
                succ=self.parent.findSuccessor()
                self.parent.rightChild=self
        return succ

    # 查找子树中的最小键
    def findMin(self):
        current=self
        while current.hasLeftChild():
            current=current.leftChild
        return current

    # 移除后继节点
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild=None
            else:
                self.parent.rightChild=None
        elif self.hasAnyChild():
            if self.hasLeftChild():
                self.parent.leftChild=self.leftChild
            else:
                self.parent.rightChild=self.leftChild
            self.leftChild.parent=self.parent
        else:
            if self.isLeftChild():
                self.parent.leftChild=self.rightChild
            else:
                self.parent.rightChild=self.rightChild
            self.rightChild.parent=self.parent

    # 二叉搜索树的迭代器
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem