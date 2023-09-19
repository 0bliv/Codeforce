n, b, d = map(int, input().split())
orange_sizes = list(map(int, input().split()))

count = 0  
waste_section = 0  

for orange_size in orange_sizes:
    if orange_size <= b:
        waste_section += orange_size  
        if waste_section > d:
            count += 1
            waste_section = 0  

print(count)
