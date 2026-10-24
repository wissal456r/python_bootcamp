def is_palindrome(text):
    text = ''.join(char.lower() for char in text if char.isalnum())

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


text = input("Enter a word or sentence: ")
print(is_palindrome(text))
