
while True:
    number = int(input("Enter an integer: "))

    if number == 0:
        break

    text = input("Enter a string: ")

    if any(vowel in text.lower() for vowel in "aeiou"):
        print(number)

    if number >= 42:
        print(number)

    if not any(vowel in text.lower() for vowel in "aeiou") and number < 42:
        print(text)
