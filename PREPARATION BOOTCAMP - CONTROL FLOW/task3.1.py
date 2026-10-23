text = input("Enter the message: ")
shift = int(input("Enter the shift: "))

encrypted = ""

for character in text:
    if character.isalpha() and character.isascii():
        base = ord("A") if character.isupper() else ord("a")
        new_character = chr((ord(character) - base + shift) % 26 + base)
        encrypted += new_character
    else:
        encrypted += character

print(encrypted)
