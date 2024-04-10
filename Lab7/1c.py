
a = int(input())
b = int(input())
for i in range(a,b):
    if(i%2==0):
        print(i, end=" ")
print("\n or \n")
li = range(a,b)[::2]
print(' '.join(map(str, li))) 
#list(map(print,li))