text = input("Enter the encrypted message: ")
shift = int(input("Enter the shift: "))

decrypted = ""

for character in text:
    if character.isalpha() and character.isascii():
        base = ord("A") if character.isupper() else ord("a")
        new_character = chr((ord(character) - base - shift) % 26 + base)
        decrypted += new_character
    else:
        decrypted += character

print(decrypted)
