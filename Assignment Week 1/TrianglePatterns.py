def lower_triangular(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n+1):
        print("* " * i)
    print()

def upper_triangular(n):
    print("Upper Triangular Pattern:")
    for i in range(n):
        print("  " * i + "* " * (n - i))
    print()

def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "* " * (i + 1)
        print(spaces + stars)
    print()

n = int(input("Enter number of rows: "))

lower_triangular(n)
upper_triangular(n)
pyramid(n)