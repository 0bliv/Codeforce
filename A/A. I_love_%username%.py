def count_amazing_performances(n, points):
    # Initialize variables to store best and worst performances
    best_performance = points[0]
    worst_performance = points[0]
    amazing_count = 0

    # Iterate through the points
    for i in range(1, n):
        # Check if the current performance is amazing
        if points[i] > best_performance:
            best_performance = points[i]
            amazing_count += 1
        elif points[i] < worst_performance:
            worst_performance = points[i]
            amazing_count += 1

    return amazing_count

n = int(input())
points = list(map(int, input().split()))

result = count_amazing_performances(n, points)
print(result)
