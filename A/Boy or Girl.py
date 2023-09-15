s = input()
count = len(set([char for char in s]))
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
