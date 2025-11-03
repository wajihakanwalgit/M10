def sum(n):
    return n*(n+1)//2
def arraysum(arr):
    total = 0
    for num in arr:
        total += num
    return total
a=[1,2,3,4,5]
b=[6,7,8,9,10]
arraysum(a)
arraysum(b)
def summm(n):
    if( n <=0):
        return 0
    return n + summm(n-1)
summm(5)
