from fractions import Fraction

yakko, wakko = map(int, input().split())

winning_outcomes = 0

for dot_roll in range(max(yakko, wakko), 7):
    winning_outcomes += 1

total_outcomes = 6
dot_probability = Fraction(winning_outcomes, total_outcomes)

print(f"{dot_probability.numerator}/{dot_probability.denominator}")
