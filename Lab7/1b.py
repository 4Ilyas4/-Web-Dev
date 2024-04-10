
a = int(input())
b = int(input())
if(b > a):
    print(b)
else:
    print(a)
print("\n"+"or\n")
print(b if b>a else a)