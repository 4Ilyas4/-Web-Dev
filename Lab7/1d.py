
array = []
n = int(input())
li = input().split()
for el in li:
    array.append(int(el))
for i in range(n):
    if(i%2==0):
        print(array[i],end=" ")
print("\n or \n")
array = list(map(int,li))
for i in range(n):
    if(i%2==0):
        print(array[i],end=" ")
