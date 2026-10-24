import random
import time

numbers = [random.randint(0, 1000000) for _ in range(1000000)]

start_time = time.time()
numbers.sort()
end_time = time.time()

print("First 10 numbers:", numbers[:10])
print("Last 10 numbers:", numbers[-10:])
print(
    "Numbers sorted:",
    all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
)
print("Time taken:", round(end_time - start_time, 4), "seconds")
