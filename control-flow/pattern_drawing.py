number = int(input("Enter the size of the pattern: "))
i = 0

while i <= number:
    for num in range(0, number):
        num += 1
        print("*", end="")
    i += 1
    print()