def triangle(lvl):
    if lvl > 0:
        triangle(lvl - 1)
        print("*" * lvl)
