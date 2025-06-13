for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print(n, "divisible by 3 and 5")
    elif n % 3 == 0:
        print(n, "divisible by 3")
    elif n % 5 == 0:
        print(n ,"divisible by 5")