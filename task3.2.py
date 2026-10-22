numbers = [
    123456789,
    112233445566778899,
    123456789 * 987654321
]

for number in numbers:
    original_number = number
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    print("Number:", original_number)
    print("Digit sum:", total)
