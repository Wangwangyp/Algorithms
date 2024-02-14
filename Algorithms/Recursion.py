'''
递归算法必须具备基本结束条件
递归算法必须要减小规模，改变状态，像基本结束条件演进
递归算法必须要调用自身
'''
# 汉诺塔(递归实现)
def moveTower(height,fromPole,withPole,toPole):
    if height>=1:
        moveTower(height-1,fromPole,toPole,withPole)
        moveDisk(height,fromPole,toPole)
        moveTower(height-1,withPole,fromPole,toPole)
def moveDisk(disk,fp,tp):
    print(f"moveing disk[{disk}] from {fp} to {tp} ")

moveTower(3,"#1","#2","#3")

# 找零问题(非动态规划)
def recDC(coinValueList,change,knownResults):
    minCoins=change
    if change in coinValueList:
        return 1
    elif knownResults[change]>0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c<=change]:
            coinNum=1+recDC(coinValueList,change-i,knownResults)
            if coinNum<minCoins:
                minCoins=coinNum
                knownResults[change]=minCoins
    return minCoins

print(recDC([1, 5, 10, 25], 62, [0] * 63))

# 找零问题(动态规划)
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount=cents
        newCoin=1
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        minCoins[cents]=coinCount
        coinsUsed[cents]=newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin=change
    while coin>0:
        thisCoin=coinsUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin

coinsUsed=[0]*64
coinCount=[0]*64
dpMakeChange([1,5,10,21,25],63,coinCount,coinsUsed)
printCoins(coinsUsed,63)
printCoins(coinsUsed,52)
print(coinsUsed)

# 博物馆大盗问题(01背包—>动态规划 ->递推实现) P130
print("博物馆大盗问题(01背包—>动态规划 ->递推实现)")
# 宝物的重量和价值
tr=[None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]
# 大盗最大承重
max_w=20
# 初始化二维表格m[(i,w)]
# 表示前i个宝物中，最大重量w的组合，所得到的最大价值
# 当i==0 or w==0 时，价值均为0
m={(i,w):0 for i in range(len(tr)) for w in range(max_w+1)} # 将字典的初始值都设为0
# 逐个填写二维表格
for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        if tr[i]['w']>w:  # 装不下第i个宝物
            m[(i,w)]=m[(i-1),w]
        else:
            # 不装第i个宝物，装第i个宝物，两种情况下最大价值
            m[(i,w)]=max(m[(i-1,w)],m[(i-1,w-tr[i]['w'])]+tr[i]['v'])
# 输出结果
print(m[(len(tr)-1,max_w)])

# 博物馆大盗问题(01背包—>动态规划 ->递归实现) P130
print("博物馆大盗问题(01背包—>动态规划 ->递归实现)")
# 宝物的重量和价值
tr={(2,3),(3,4),(4,8),(5,8),(9,10)}
max_w=20
# 初始化记忆化表格m
# key是(宝物组合，最大重量),value是最大价值
m={}
def thief(tr,w):
    if tr==set() or w==0:
        m[(tuple(tr),w)]=0 # tuple是key的要求
        return 0
    elif (tuple(tr),w) in m:
        return m[(tuple(tr),w)]
    else:
        vmax=0
        for t in tr:
            if t[0]<=w:
                # 逐个从集合中去掉某个宝物，递归调用
                # 选出所有价值中的最大值
                v=thief(tr-{t},w-t[0])+t[1]
                vmax=max(vmax,v)
        m[(tuple(tr),w)]=vmax
        return vmax
print(thief(tr,max_w))


