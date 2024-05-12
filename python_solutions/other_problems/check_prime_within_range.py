def sieve_of_eratosthenes(max_num):
    """
    Returns a list of primes up to max_num (inclusive) using the Sieve of Eratosthenes.

    Args:
    max_num (int): The upper boundary of the range to find primes in.

    Returns:
    list: A list containing all the prime numbers up to max_num.
    """

    # Create a boolean array "is_prime[0..max_num]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (max_num + 1)
    p = 2  # Start with the first prime number.

    # While p squared is less than or equal to max_num, there could still be
    # non-marked multiples of some prime number.
    while (p * p <= max_num):
        # If is_prime[p] is not changed, then it is a prime
        if (is_prime[p] == True):
            # Updating all multiples of p to not prime starting from p^2
            # This is because, the multiples like 2p, 3p, ... were already
            # marked by smaller primes such as 2, 3, etc.
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1  # Move to the next number

    # 0 and 1 are not prime numbers
    is_prime[0], is_prime[1] = False, False

    # Collecting all prime numbers from the array
    primes = [p for p in range(max_num + 1) if is_prime[p]]
    return primes

# Example usage:
# Get all primes up to 30
primes_up_to_30 = sieve_of_eratosthenes(30)
print(primes_up_to_30)
