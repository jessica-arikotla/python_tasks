#day3 Task1
n = int(input("Enter n value: "))

#Right Triangle Of Stars
print("\nRight Triangle")
for i in range(1, n + 1):
    print("*" * i)

#Inverted Triangle Of Stars
print("\nInverted Triangle Of Stars")
for i in range (n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Pascal Triangle
print("\nPascal Triangle")
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

#Prime numbers up to n
print("\nPrime Numbers")
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
