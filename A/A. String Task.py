def remove(s):
    vowels = "AOYEUIaoyeui"
    result = ''.join('.' + char.lower() if char.lower() not in vowels else '' for char in s)
    return result

s = input()
resp = remove(s)
print(resp)
