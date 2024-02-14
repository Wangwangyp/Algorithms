# 二分搜索   前提是有序表
# 非递归
def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if alist[mid]==item:
            found=True
        else:
            if item<alist[mid]:
                last=mid-1
            else:
                first=mid=1
    return found
# 递归
def binarySearch_new(alist,item):
    if len(alist)==0:
        return False
    else:
        mid=len(alist)//2
        if alist[mid]==item:
            return True
        else:
            if item<alist[mid]:
                return binarySearch_new(alist[:mid],item)
            else:
                return binarySearch_new(alist[mid+1:],item)