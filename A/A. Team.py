n = int(input()) 
count = 0

for _ in range(n):
    views = list(map(int, input().split()))  
    total_sure = sum(views)  
    if total_sure >= 2:  
        count+=1 
print(count)