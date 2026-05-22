def get_number():
    numbers = []
    while True :
        user_input = input("Enter 'Q' to quit or Enter a number: ").upper()
        if user_input == "Q": 
                break
        try:    
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers
        

def calculate_stats(numbers):
    smallest = min(numbers)
    biggest = max(numbers)
    addition =sum(numbers)
    average = sum(numbers) / len(numbers)
    return smallest, biggest, average, addition


def main():
    number = get_number()
    smallest, biggest, average, addition = calculate_stats(number)
    print(50 * "-")
    print(f"Smallest number: {smallest}")
    print(f"Biggest number: {biggest}")
    print(f"Sum: {addition}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()