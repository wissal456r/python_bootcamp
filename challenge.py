
import math

for limit in [20, 200, 2000]:
    result = 1

    for number in range(1, limit + 1):
        result = math.lcm(result, number)

    print("From 1 to", limit, ":", result)
