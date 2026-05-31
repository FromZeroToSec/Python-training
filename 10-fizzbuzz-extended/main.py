def fizzbuzz(number):
    if number % 5 == 0  and number % 3 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
    
def run_fizzbuzz(limit):
    for number in range(1, limit + 1):
        print(fizzbuzz(number))

def main():
    try:
        limit = int(input("Enter the limit: "))
        run_fizzbuzz(limit)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()