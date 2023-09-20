n = int(input())
resp = []

for _ in range(n):
    word = input()
    
    if len(word) > 10:
        abbreviation = word[0] + str(len(word) - 2) + word[-1]
        resp.append(abbreviation)
    else:
        resp.append(word)
        
for abbreviation in resp:
    print(abbreviation)
