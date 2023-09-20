n, x = map(int,input().split())
count = 0

for i in range(n):
    # read
    op, number = input().split()
    number = int(number)
    if op == '+':
        x+=number
    else:
        if x < number:
            count+=1
        else:
            x -= number
print(x,count)