# Listing 5.13 - Prime number

NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_PER_LINE = 10
# Count the number of prime numbers
count = 0

#  A number to be tested for primeness
number = 2

print(" The first 50 prime numbers are")

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    isPrime = True  # Is the current number prime?

    # Test if number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # if true, the number is not prime
            isPrime = False  # Set isPrime to False
            break  # Exit the for loop
        divisor += 1

    # Display the prime number and increase the count
    if isPrime:
        count += 1  # Increase the count

        print(format(number, "5d"), end=' ')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print()  # jump to the new line

    # Check if the next number is prime
    number += 1



