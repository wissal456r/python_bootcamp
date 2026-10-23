text = input("Enter encrypted message: ").upper()
length = int(input("Enter key length: "))

key = ""

for i in range(length):
    letters = text[i::length]
    best_shift = 0
    best_score = -1

    for shift in range(26):
        score = 0
        for letter in letters:
            if letter.isalpha():
                score += (ord(letter) - ord("A") - shift) % 26 in [4, 19, 0, 8, 13, 18]

        if score > best_score:
            best_score = score
            best_shift = shift

    key += chr(ord("A") + best_shift)

print("Estimated key:", key)

result = ""
i = 0

for letter in text:
    if letter.isalpha():
        shift = ord(key[i % length]) - ord("A")
        result += chr((ord(letter) - ord("A") - shift) % 26 + ord("A"))
        i += 1
    else:
        result += letter

print("Decrypted message:", result)
