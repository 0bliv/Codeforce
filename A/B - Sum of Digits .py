def count_operations_to_single_digit(num):
    count = 0
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
        count += 1
    return count

# Input
n = int(input().strip())

# Output
result = count_operations_to_single_digit(n)
print(result)
