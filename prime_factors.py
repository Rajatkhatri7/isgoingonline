def prime_factors(number):
    prime_factors = []
    divisor = 2

    while(divisor <= number):
        if(number%divisor == 0):
            prime_factors.append(divisor)
            number = number//divisor
        else:
            divisor += 1

    return prime_factors


number = int(input("Enter a number: "))

if(number<2):
    print("Prime factors are not defined for numbers less than 2.")
else:
    factors = prime_factors(number)
    if len(factors) > 0:
        print(f"Prime factors of {number} are: {factors}")
    else:
        print(f"{number} has no prime factors.")

