def power(base, exponent):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base

        base *= base
        exponent //= 2

    return result


print(power(42, 84))
print(power(42, 168))
