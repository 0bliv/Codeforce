n, k = map(int, input().split())
arr = list(map(int, input().split()))
test = arr[k-1]
count = 0

for i in arr:
    if i >= test and i > 0:
        count+=1
    
print(count)



        