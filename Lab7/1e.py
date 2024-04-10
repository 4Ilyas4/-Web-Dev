
def minf(a,b,c,d):
    m = a
    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.append(d)
    for e in arr:
        if(e < m):
            m = e
    print(m)
li = input().split()
a = int(li[0])
b = int(li[1])
c = int(li[2])
d = int(li[3])
minf(a,b,c,d)
print("\n or \n")
def minf(a, b, c, d):
    return min(a, b, c, d)
a, b, c, d = map(int, input().split())
print(minf(a, b, c, d))