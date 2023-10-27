number: int = 10

match number:
    if number in range(10, 49):
        print("")
    if number in range(50, 100):
        print("")
    case _:
        print("")