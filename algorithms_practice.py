'''
algorithms_practice.py

This program contains algorithm examples for Euclid's Algorithm for calculating
greatest common divisor, the Sieve of Eratosthenes, Trial Division, and
checking Goldbach's Conjecture.

'''


import math

'''
euclid(num1, num2):

Returns the GCD of two integers using Euclid's algorithm. Also prints out the
intermediate steps for Euclid's Algorithm on num1 and num2.

Parameters:
num1 (int): First number for the GCD
num2 (int): Second number for the GCD

Returns:
int: GCD of num1 and num2
'''


def euclid(num1, num2):

    # Create a list for storing strings for each intermediate step, output
    output = []

    while (num1 != 0 and num2 != 0):

        # Append the intermediate step to output[] as a string
        output.append('GCD(' + str(num1) + ',' + str(num2) + ')')

        # Let(a,b) be positive integers, then, GCD(a,b) = GCD(b,a mod b)
        a_mod_b = num1 % num2

        num1 = num2

        num2 = a_mod_b

    # If num1 = 0 then euclid(num1, num2) = num2, since the GCD(0, B) = B.
    if (num1 == 0):
        gcd = num2

        # Append the intermediate step to output[] as a string
        output.append('GCD(' + str(num1) + ',' + str(num2) + ')')

    # If num2 = 0 then euclid(num1, num2) = num1, since the GCD(A, 0) = A.
    elif (num2 == 0):
        gcd = num1

        # Append the intermediate step to output[] as a string
        output.append('GCD(' + str(num1) + ',' + str(num2) + ')')

    # Print the intermediate steps
    print(' = '.join(output))

    # Return the greatest common divisor
    return gcd


'''
prime_gen(n):

Returns a list of prime numbers up to (and including) a certain input integer,
n.

Parameters:
n (int): The target number to generate primes up to.

Returns:
list: List of all prime numbers <= n.
'''


def prime_gen(n):

    # Create a list representing consecutive integers from 0 through n, sieve
    sieve = [True for i in range(n + 1)]

    # Let p equal 2, the smallest prime number
    p = 2

    # Enumerate the multiples of p by counting in incrememts of p from 2p to n,
    # and mark them in the list
    while (n >= p * p):

        # If prime[p] is a prime, then it is True
        if (sieve[p]):

            # Give all nonprime numbers a value of False
            for i in range((p * p), (n + 1), p):
                sieve[i] = False

        # Increment p
        p += 1

    # Create a list of the indexes of values where sieve[p] == True, primes
    primes = [p for p, n in enumerate(sieve) if n]

    # Remove the 0 and 1 values from primes as they should not be included
    primes = primes[2:]

    # Return the list of prime numbers
    return primes


'''
prime_check_trial(n):

Returns a boolean value (True or False) depending on whether the input n is
prime.

Parameters:
n (int): The target integer to check primality.

Returns:
boolean: True if n is prime, False if n is not prime.
'''


def prime_check_trial(n):

    # Create a boolean value for whether or not n is a prime number, prime
    prime = True

    # If n is less than 2, it is not a prime number
    if (n < 2):
        prime = False

    # If n is divisible by any number up to sqrt(n), it is not a prime number
    for i in range(2, int(math.sqrt(n) + 1)):
        print(i)
        if (n % i == 0):
            prime = False

    return prime


'''
prime_check_sieve(n):

Returns a boolean value (True or False) depending on whether the input n is
prime.

Parameters:
n (int): The target integer to check primality.

Returns:
boolean: True if n is prime, False if n is not prime.
'''


def prime_check_sieve(n):

    # Check if n is found in prime_gen(n) and return a boolean, prime
    prime = n in prime_gen(n)

    return prime


'''
Returns a list of two prime integers that sum up to n.

Parameters:
n (int): The target even integer to check Goldbach's Conjecture for.

Returns:
list: A list of length 2 containing 2 ints that sum up to n.
'''


def check_goldbach(n):

    # Create a boolean value for whether the conjecture holds true, primes
    primes = []

    # Create a list of prime numbers up to n using prime_gen(n), prime_list
    prime_list = prime_gen(n)

    # Subtract each item in prime_list from n and see if the difference is in
    # prime_list
    for num in prime_list:

        # If the difference is in prime_list, the conjecture holds true
        if ((n - num) in prime_list):
            primes = [n - num, num]

    return primes


# TEST CASES
if __name__ == '__main__':

    print("---------------------------------------")
    print("Euclid's Algorithm")
    print("---------------------------------------")
    euclid_test_1 = [252, 105]
    print("Test Case 1: GCD of", euclid_test_1[0], "and", euclid_test_1[1])
    print("Test Case 1 Steps: ")
    ans = euclid(euclid_test_1[0], euclid_test_1[1])
    print("Test Case 1 (Your Answer):", ans)
    print("Test Case 1 (Correct Answer):", 21)
    print("Test Case 1:", ("# PASSED! #"
                           if ans == 21
                           else "# INCORRECT #"))
    print()
    euclid_test_2 = [1071, 462]
    print("Test Case 2: GCD of", euclid_test_2[0], "and", euclid_test_2[1])
    print("Test Case 2 Steps: ")
    ans = euclid(euclid_test_2[0], euclid_test_2[1])
    print("Test Case 2 (Your Answer):", ans)
    print("Test Case 2 (Correct Answer):", 21)
    print("Test Case 2:", ("# PASSED! #"
                           if ans == 21
                           else "# INCORRECT #"))
    print()
    euclid_test_3 = [85523, 3212]
    print("Test Case 3: GCD of", euclid_test_3[0], "and", euclid_test_3[1])
    print("Test Case 3 Steps: ")
    ans = euclid(euclid_test_3[0], euclid_test_3[1])
    print("Test Case 3 (Your Answer):", ans)
    print("Test Case 3 (Correct Answer):", 1)
    print("Test Case 3:", ("# PASSED! #"
                           if ans == 1
                           else "# INCORRECT #"))

    print("---------------------------------------")
    print("Prime Number Generation")
    print("---------------------------------------")
    prime_gen_test_1 = 42
    prime_gen_test_1_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    print("Test Case 1: Prime Numbers Up To:", prime_gen_test_1)
    print("Test Case 1 (Your Answer):", prime_gen(prime_gen_test_1))
    print("Test Case 1 (Correct Answer):", prime_gen_test_1_ans)
    print("Test Case 1:", ("# PASSED! #"
                           if prime_gen(prime_gen_test_1) ==
                           prime_gen_test_1_ans
                           else "# INCORRECT #"))
    print()
    prime_gen_test_2 = 314
    prime_gen_test_2_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
    131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313]
    print("Test Case 2: Prime Numbers Up To:", prime_gen_test_2)
    print("Test Case 2 (Your Answer):", prime_gen(prime_gen_test_2))
    print("Test Case 2 (Correct Answer):", prime_gen_test_2_ans)
    print("Test Case 2:", ("# PASSED! #"
                           if prime_gen(prime_gen_test_2) ==
                           prime_gen_test_2_ans
                           else "# INCORRECT #"))
    print()
    prime_gen_test_3 = 884
    prime_gen_test_3_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
    113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
    199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
    491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883]
    print("Test Case 3: Prime Numbers Up To:", prime_gen_test_3)
    print("Test Case 3 (Your Answer):", prime_gen(prime_gen_test_3))
    print("Test Case 3 (Correct Answer):", prime_gen_test_3_ans)
    print("Test Case 3:", ("# PASSED! #"
                           if prime_gen(prime_gen_test_3) ==
                           prime_gen_test_3_ans
                           else "# INCORRECT #"))
                           
    print("---------------------------------------")
    print("Primality Testing")
    print("---------------------------------------")
    primality_test_1 = 8
    primality_test_1_ans = False
    print("Test Case 1: Check Primality For:", primality_test_1)
    print("Test Case 1 (Your Trial Division Answer):", prime_check_trial(
            primality_test_1))
    print("Test Case 1 (Your Sieve Answer):", prime_check_sieve(
            primality_test_1))
    print("Test Case 1 (Correct Answer):", primality_test_1_ans)
    print("Test Case 1:", ("# PASSED! #"
                           if prime_check_trial(
                                   primality_test_1) ==
                           prime_check_sieve(primality_test_1) ==
                           primality_test_1_ans
                           else "# INCORRECT #"))
    print()
    primality_test_2 = 482
    primality_test_2_ans = False
    print("Test Case 2: Check Primality For:", primality_test_2)
    print("Test Case 2 (Your Trial Division Answer):", prime_check_trial(
            primality_test_2))
    print("Test Case 2 (Your Sieve Answer):", prime_check_sieve(
            primality_test_2))
    print("Test Case 2 (Correct Answer):", primality_test_2_ans)
    print("Test Case 2:", ("# PASSED! #"
                           if prime_check_trial(primality_test_2) ==
                           prime_check_sieve(primality_test_2) ==
                           primality_test_2_ans
                           else "# INCORRECT #"))
    print()
    primality_test_3 = 853
    primality_test_3_ans = True
    print("Test Case 3: Check Primality For:", primality_test_3)
    print("Test Case 3 (Your Trial Division Answer):", prime_check_trial
          (primality_test_3))
    print("Test Case 3 (Your Sieve Answer):", prime_check_sieve(
            primality_test_3))
    print("Test Case 3 (Correct Answer):", primality_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if prime_check_trial(primality_test_3)
                           == prime_check_sieve(primality_test_3) ==
                           primality_test_3_ans
                           else "# INCORRECT #"))

    print("---------------------------------------")
    print("Goldbach's Conjecture")
    print("---------------------------------------")
    goldbach_test_1 = 8
    goldbach_test_1_ans = [3, 5]
    ans = check_goldbach(goldbach_test_1)
    print("Test Case 1: 2 Primes For:", goldbach_test_1)
    print("Test Case 1 (Your Answer):", check_goldbach(goldbach_test_1))
    print("Test Case 1 (A Correct Answer):", goldbach_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if ans[0] + ans[1] == goldbach_test_1
                           else "# INCORRECT #"))
    print()
    goldbach_test_2 = 482
    goldbach_test_2_ans = [3, 479]
    ans = check_goldbach(goldbach_test_2)
    print("Test Case 2: 2 Primes For:", goldbach_test_2)
    print("Test Case 2 (Your Answer):", check_goldbach(goldbach_test_2))
    print("Test Case 2 (A Correct Answer):", goldbach_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if ans[0] + ans[1] == goldbach_test_2
                           else "# INCORRECT #"))
    print()
    goldbach_test_3 = 1152
    goldbach_test_3_ans = [23, 1129]
    ans = check_goldbach(goldbach_test_3)
    print("Test Case 3: 2 Primes For:", goldbach_test_3)
    print("Test Case 3 (Your Answer):", check_goldbach(goldbach_test_3))
    print("Test Case 3 (A Correct Answer):", goldbach_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if ans[0] + ans[1] == goldbach_test_3
                           else "# INCORRECT #"))
