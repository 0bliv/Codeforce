def solution(events):
    police = 0
    crimes = 0

    for event in events:
        if event > 0:
            police += event
        else:
            if police >= abs(event):
                police-= abs(event)
            else:
                crimes+=1
    return crimes

# main
n = input()
events = list(map(int,input().split()))

print(solution(events))

