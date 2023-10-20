#
# b = int(input("Enter 2 for study"))
# c = int(input("Enter 3 for quit"))

print("What do you want to do?")
print("1. Enter 1 to play a game")
print("2. Enter 2 to study")
print("3. Enter 3 to quit")

while True:
    d = int(input("Enter your choice: "))
    
    if d == 1:
        print("I'm happy to play with you. Do you like Tic Tac Toe? (If yes, press 1)")
        a = int(input())
        if a == 1:
            print("Let's play Tic Tac Toe!")
            break
        else:
            print("Not a valid choice. Please enter 1 to play or another choice to go back to the main menu.")
    
    elif d == 2:
        print("I'm happy to study with you. Do you need a calculator? (If yes, press 1)")
        a = int(input())
        if a == 1:
            print("Opening the calculator...")
            break
        else:
            print("Not a valid choice. Please enter 1 for the calculator or another choice to go back to the main menu.")
    
    elif d == 3:
        print("Thank you for using this program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Exiting the program.")
