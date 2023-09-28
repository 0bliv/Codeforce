def elephant_steps(x):
    steps = x // 5

    if x % 5 != 0:
        steps += 1

    return steps

x = int(input())

print(elephant_steps(x))
