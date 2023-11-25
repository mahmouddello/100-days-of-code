def prime_checker(number):
    is_prime = True  # boolean variable to trigger it if the number is prime
    for checker in range(2, number):
        if number % checker == 0:
            # not prime
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input("number to check : "))
prime_checker(number=n)
