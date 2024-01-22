from random import randrange

def is_invalid(x):
    return (not x.isdigit() or int(x) <= 1)

print("Welcome to the game!")

while True:
    
    right_number = input("Input right limit number please: ")
    
    while is_invalid(right_number):
            right_number = input("Incorrect input! Please, try again: ")
            
    random_number = randrange(1, int(right_number))
    count_attempts = 1
    left = 1
    right = int(right_number)
    middle = (left + right) // 2
    
    while True:
        if middle > random_number:
            print("Your answer is larger then random_number")
            right = middle
            middle = (left + right) // 2
            count_attempts += 1
        elif middle < random_number:
            print("Your answer is smaller then random_number")
            left = middle
            middle = (left + right) // 2
            count_attempts += 1
        else:
            print("\nPerfect! You choose the correct answer!")
            break
            
    print(f"You done for {count_attempts} attempts!")
        
    play_again = input("\nDo you want play again? Y/y - yes, N/n - no: ")
        
    while play_again.lower() not in ['y', 'n']:
        play_again = input("Incorrect choose! Please try again: ")
        
    if play_again.lower() == 'n':
        break
        
print("\nThank you for playing, see you later!")
