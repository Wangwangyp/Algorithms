class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 括号匹配--简单版  只判断[]
def parChecker_simple(string):
    s=Stack()
    balenced=True
    index=0
    while index<len(string) and balenced:
        symbol=string[index]
        if symbol=='[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balenced=False
            else:
                s.pop()
        index=index+1
    if balenced and s.isEmpty():
        return True
    else:
        return False

#括号匹配  复杂{}()[]
def parChecker_complex(string):
    s=Stack()
    balenced=True
    index=0
    while index<len(string) and balenced:
        symbol=string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balenced=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balenced=False
        index=index+1
    if balenced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens="([{"
    closers=")]}"

    return opens.index(open)==closers.index(close)  # 获得子字符串的索引

# 将十进制转为二进制  模二取余，余数倒排
def tenToTwo(num):
    s=Stack()

    while num>0:
        rem=num%2
        s.push(rem)
        num=num//2

    result=""
    while not s.isEmpty():
        result=result+str(s.pop())

    return result

#十进制转任意
def tenToAny(num,kind):
    s=Stack()

    digits="0123456789ABCDEF"  #为16进制设计,其他进制(<16)也可以使用

    while num>0:
        rem=num%kind
        s.push(rem)
        num=num//kind

    result=""
    while not s.isEmpty():
        result=result+digits[s.pop()]

    return result

#中序表达式转后序表达式
import string
def infixToPostfix(infixexpr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1

    opStack=Stack() # 保存运算符的空栈
    postfixList=[]  # 保存结果的空列表

    tokenList=list(infixexpr)  #标记列表

    for token in tokenList:
        if token in string.ascii_uppercase:  # 操作数
            postfixList.append(token)
        elif token=='(':                     # (
            opStack.push(token)
        elif token==')':                     # )
            topToken=opStack.pop()
            while topToken !='(':
                postfixList.append(topToken)
                topToken=opStack.pop()
        else:                                # 操作符
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ' '.join(postfixList)

# 计算后序表达式
def postfixEval(postfixExpr):
    operandStack=Stack()

    tokenList=postfixExpr.split()  # 以空格分割，输入时记得加空格

    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2=operandStack.pop()
            operand1=operandStack.pop()
            result=doMath(token,operand1,operand2)
            operandStack.push(result)

    return operandStack.pop()

def doMath(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op=="/":
        return op1/op2
    elif op=="+":
        return op1+op2
    else:
        return op1-op2

