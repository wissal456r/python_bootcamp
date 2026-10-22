total = 0
for i in range(1000000):
    total = total + (-1) ** i / (2 * i + 1)

pi = 4 * total

print(round(pi, 6))

