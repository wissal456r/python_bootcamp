
total1 = 1 + 11 + 111 + 1111 + 11111 + 111111 + 1111111 + 11111111 + 111111111

total2 = total1 + 1111111111

total3 = total2 + 11111111111

for total in [total1, total2, total3]:
    print("Sum =", total)
    print("Power 2 =", total ** 2)
    print("Power 3 =", total ** 3)
    print("Power 4 =", total ** 4)
    print("Power 5 =", total ** 5)
    print()