# ask user to enter a string
while(True):
    try:
        result = input("Enter a String: ")
        print(result[::])
        if result[::].lower() == result[::-1].lower():
            print("The string is a palindrome")
        else:
            print("The string is not a palindrome")
        break
    except:
        print("You did not enter a valid string, enter a valid string? ")
        continue