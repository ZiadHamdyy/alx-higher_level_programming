def magic_calculation(a, b, c):
    if a < b:
        result = a + b
        if c < b:
            result *= 10
        else:
            result = c + b
        return result
