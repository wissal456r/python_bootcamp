result = 0

for n in range(99, 0, -2):
    result = n ** 2 / (6 + result)

pi = 3 + result

print(round(pi, 6))


