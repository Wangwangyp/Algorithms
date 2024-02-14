# 解析树

import operator
from Algorithms import Stack
from Algorithms import Tree

# 创建二叉解析树
def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack.Stack()
    eTree=Tree.BinaryTree('')
    pStack.push(eTree)
    currentree=eTree
    for i in fplist:
        if i=='(':
            currentree.insertLeft('')
            pStack.push(currentree)
            currentree=currentree.getLeftChild()
        elif i not in '+-*/)':
            currentree.setRootVal(eval(i))
            parent=pStack.pop()
            currentree=parent
        elif i in '+-*/':
            currentree.setRootVal(i)
            currentree.insertRight('')
            pStack.push(currentree)
            currentree=currentree.getRightChild()
        elif i == ')':
            currentree=pStack.pop()
        else:
            raise ValueError("Unknown Operator: "+i)
    return eTree

# 计算二叉解析树的递归函数


def evaluate(parseTree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRightChild()
    if leftC and rightC:
        fn=opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()