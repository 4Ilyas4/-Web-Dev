def swap(a,b,v):
    temp = v[a]
    v[a] = v[b]
    v[b] = temp 

def heapify(arr, N, i):
    tmax = i
    left = 2*i + 1
    right = 2*i + 2
    if(left < N and arr[left][0][0] > arr[tmax][0][0]):
        tmax = left
    if(right < N and arr[right][0][0] > arr[tmax][0][0]):
        tmax = right
    if(tmax != i):
        swap(i,tmax,arr)
        heapify(arr,N,tmax)

def heapSort(arr, N):
    for i in range(int(N / 2 - 1), 0, -1):
        heapify(arr, N, i)
    for i in range(N - 1, 0, -1):
        swap(0,i,arr)
        heapify(arr,i,0)

if __name__ == '__main__':
    records = []
    mins = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    minr = records[0][1]
    for rec in records:
        if(rec[1]<minr or rec[1]==minr):
            mins.append(rec)
            minr = rec[1]
    heapSort(mins,len(mins))
    #mins = sorted(mins, key=lambda x: x[0])
    for m in mins:
        print(m[0])