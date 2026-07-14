while(True):
    try:
        user_prompt = input("Enter the price of an item and I will tell you what the price of the item + sales tax is: ")
        result = int(user_prompt)
        total = result * 1.07
        print(f"the total of the item with tax is: {total}$")
        break
    except:
        print("Invalid item price, enter a valid item price")
        continue