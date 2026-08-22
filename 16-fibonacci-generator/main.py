
def main():
    a = 0
    b = 1
    for i in range(10):
        print(a)
        old_a = a
        a = a + b
        b = old_a
        print(fibonacci_recursive(i))


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    main()