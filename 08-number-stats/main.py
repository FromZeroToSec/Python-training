def get_number():
    numbers = []
    while True :
        user_input = input("Enter 'Q' to quit: \nEnter a number: ").upper()
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
    return smallest, bigest, average, addition




if __name__ == "__main__":
    get_number()        





    # fonctions built-in