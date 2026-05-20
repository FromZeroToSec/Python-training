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
        
if __name__ == "__main__":
    get_number()        