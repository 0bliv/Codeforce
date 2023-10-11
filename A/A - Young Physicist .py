n = int(input())
forces = []

for _ in range(n):
    force = list(map(int,input().split()))
    forces.append(force)   

sum_forces = [0,0,0]

for i in forces:
    sum_forces[0] += i[0]
    sum_forces[1] += i[1]
    sum_forces[2] += i[2]

if (sum_forces == [0,0,0]):
    print("YES")
else:
    print("NO")
