sum = 0
while True:
    number = input("Enter the price or press q to quit\n")
    if number != "q":
        sum = sum + int(number)
        print(f"order total so far {sum}")
    else:
        print("Thans for using our calculator")
        print(f"your bill total is {sum}")

