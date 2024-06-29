number = int(input("Enter a number to see its multiplication table: "))
i = 0

while i <= number:
    for num in range(0, number):
        num += 1
        print("*", end="")
    i += 1
    if i == number:
        break
    else:
        print()