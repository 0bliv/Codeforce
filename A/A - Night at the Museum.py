def min_rotations(s):
    current_char = 'a' 
    rotations = 0
    
    for target_char in s:
        clockwise_rotations = (ord(target_char) - ord(current_char) + 26) % 26
        counterclockwise_rotations = (ord(current_char) - ord(target_char) + 26) % 26
        
        min_rotation = min(clockwise_rotations, counterclockwise_rotations)
        
        current_char = target_char
        rotations += min_rotation
    
    return rotations

s = input()
result = min_rotations(s)
print(result)
