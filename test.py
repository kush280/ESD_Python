#
# b = int(input("Enter 2 for study"))
# c = int(input("Enter 3 for quit"))

print("What do you want to do \n1. Enter 1 for play game\n2. Enter 2 for study\n3. Enter 3 for quit")
d = int(input("Enter your choice\n"))
while d == 1 or d == 2 or d == 3:
    if d == 1:
        print("I am happy to play with you do you like Tic Tak Toe? (If yes press 1)")
        a = int(input())
        if a == 1:
            print("TIC")
            break
        elif a > 1:
            print("not valid")
            break
    elif d == 2:
        print("I am happy to Study with you do you need Calculator? (If yes press 1)")
        a = int(input())
        if a == 1:
            print("Calculator")
            break
        elif a > 1:
            print("not valid")
            break
    elif d == 3:
        print("Thank you")
        break

if d > 3:
    print("Try with valid input")
    print("What do you want to do \n1. Enter 1 for play game\n2. Enter 2 for study\n3. Enter 3 for quit")
    d = int(input("Enter your choice\n"))
    while d == 1 or d == 2 or d == 3:
        if d == 1:
            print("I am happy to play with you do you like Tic Tak Toe? (If yes press 1)")
            a = int(input())
            if a == 1:
                print("TIC")
                break
            elif a > 1:
                print("not valid")
                break
        elif d == 2:
            print("I am happy to Study with you do you need Calculator? (If yes press 1)")
            a = int(input())
            if a == 1:
                print("Calculator")
                break
            elif a > 1:
                print("not valid")
                break
        elif d == 3:
            print("Thank you")
            break
    if d > 3:
        print("Fuck off and run program again")
