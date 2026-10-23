text = input("Enter the message: ")
key = input("Enter the keyword: ").lower()
action = input("Encrypt or decrypt? (e/d): ").lower()

if not key.isalpha() or not key.isascii():
    print("The keyword must contain English letters only.")
elif action not in ("e", "d"):
    print("Choose e to encrypt or d to decrypt.")
else:
    result = ""
    key_index = 0

    for character in text:
        if character.isalpha() and character.isascii():
            base = ord("A") if character.isupper() else ord("a")
            shift = ord(key[key_index % len(key)]) - ord("a")

            if action == "d":
                shift = -shift

            new_character = chr(
                (ord(character) - base + shift) % 26 + base
            )
            result += new_character
            key_index += 1
        else:
            result += character

    print(result)
