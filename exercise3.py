number = int(input("Enter an integer: "))
if number < 2:
    print(" the number is not a prime number.")
else:
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = false
            break
    if is_prime :
        print("the number is a prime number.")
    else :
        print("the number is not a prime number.")
