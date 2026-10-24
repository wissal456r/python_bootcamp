values = {
    "dalmatians": 101,
    "pi": 3.14,
    "beast": 666,
    "life": 42,
    "googol": 10 ** 100,
    "jordan": 23
}

print(max(values, key=values.get))
