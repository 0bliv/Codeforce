n = int(input())
s = input()

# Count the number of '0's and '1's
count_zeros = s.count('0')
count_ones = s.count('1')

# Calculate the minimum length
min_length = abs(count_ones - count_zeros)

print(min_length)
