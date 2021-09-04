def rg(a: int, b: int, c: int = 1) -> list:
    """Замена RANGE"""
    list1 = []
    n = int(a)
    if c == 0:
        return list1
    elif c > 0:
        while n < b:
            list1.append(n)
            n += c
    elif c < 0:
        while n > b:
            list1.append(n)
            n += c
    return list1


print(rg(-10, -22, 1))
