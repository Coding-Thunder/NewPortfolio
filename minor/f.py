# PROBLEM NO.1 = Calculate  the factorial of a given number
#               fac = n * (n-1)
#               for.ex, factorial of 7 will be 7*6*5*4*3*2*1 = factorial

# PROBLEM NO.2 = Find the number of trailing zeros im that factorial

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)
def facTrailingZeros(number):
    count = 0
    i = 5
    while number/i != 0:
        count += int(number/i)
        i = i*5
        return count



if __name__ == '__main__':
    number = int(input("Enter a number:\n"))
#forfac
    # fac = factorial(number)
    #print(f"the factorial is {fac}")
# for trailing zeros
    print(facTrailingZeros(number))

