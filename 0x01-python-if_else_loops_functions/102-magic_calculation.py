def magic_calculation(a, b, c):
    if a < b:
        result = a * b
    elif c < b:
        result = b - c
    else:
        result = a + b + c

    return result
