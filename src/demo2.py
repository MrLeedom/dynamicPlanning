'''
走楼梯问题
'''
#一颗满的二叉树，时间复杂度2^n
def get_count(n):
    if n==1:return 1
    if n==2:return 2
    else:
        return get_count(n-1)+get_count(n-2)
print(get_count(10))

def get_count1(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        l=[1,2]
        for i in range(3,n):
            l[0],l[1] = l[1],l[0]+l[1]
        return l[0]+l[1]
print(get_count1(10))

#整数拆分问题
def func(n):
    l = [1]
    for i in range(3,n+1):
        m=0
        for j in range(1,i//2+1):
            m=max(m,j*(i-j),j*l[i-j-2])
        l.append(m)
    return l
print(func(10))