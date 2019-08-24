def karatsuba(x: int, y: int):
    """
    Alogrithm to multiply two given integers, denoted x and y.
    More effective than regular, elementary school multiplication.
    If you're using python 3.7+, specify input type.
    :param x: simply our first number. It should be an int.
    :param y: the second one. It should be an int
    :return: their product
    """
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    else:
        n = max(len(str(x)), len(str(y)))

        nby2 = int(n / 2)

        a = int(x / 10 ** nby2)
        b = x % 10 ** (nby2)
        c = int(y / 10 ** nby2)
        d = y % 10 ** (nby2)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)

        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        # helpful n = 2 * nby2, writing it as such helps with odd and even numbers
        return ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd
