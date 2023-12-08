"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Too small bro")

    list = []

    prime_count = 0
    cur_num = 2

    while prime_count != number_of_primes:
        print(prime_count, cur_num, number_of_primes)
        prime = True

        for i in range(2, cur_num):
            if cur_num % i == 0:
                prime = False

                break

        if prime:
            list.append(cur_num)
            prime_count += 1
        cur_num += 1



    return list
