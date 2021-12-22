# 1. Multiples of 3 or 5

# Old method
# def get_sum(num):
    # sum_3 = 0
    # threes = 3
    # sum_5 = 0
    # fives = 5
    # while threes < num:
    #     sum_3 += threes
    #     threes += 3
    # while fives < num:
    #     sum_5 += fives
    #     fives += 5
    # return sum_3 + sum_5

def get_sum(num):
    # Use triangular numbers to obtain sums of threes and fives
    if num % 3 == 0:
        n_threes = int(num/3) - 1
    else:
        n_threes = int(num/3)
    print(n_threes)
    if num % 5 == 0:
        n_fives = int(num/5) - 1
    else:
        n_fives = int(num/5)
    # Multiples of 15 are double counted, so we must subtract them once
    n_15 = int(n_fives/3)
    print(n_fives)
    return 3 * n_threes * (n_threes + 1)/2 + 5 * n_fives * (n_fives + 1)/2 - n_15 * (n_15 +1) / 2 * 15


# 2. Even Fibonacci numbers
def sum_even_fibo(max_num = 4e6):
    prev_fibo = 1
    fibo = 1
    index = 2
    sum = 0
    # Every third Fibonacci number is even, so use the index to add them
    while fibo < max_num:
        new_fibo = fibo + prev_fibo
        prev_fibo = fibo
        fibo = new_fibo
        index += 1
        if index % 3 == 0:
            sum += fibo
    return sum

# 3. Largest Prime Factor
def get_largest_factor(num):
    sqrt = int(num**0.5)
    for integer in range(sqrt, 2, -1):
        if num % integer == 0 and is_prime(integer):
            return integer
    return "Could not find largest prime factor."

def is_prime(number):
    if number < 1:
        return False
    if number == int(number**0.5)**2:
        return False
    if number == 2:
        return True
    elif number % 2 == 0:
        return False
    for n in range(int(number**0.5), 2, -1):
        if number % n == 0:
            return False
    return True

# 4.
def get_palindrome():
    num_1 = 999
    num_2 = 999
    palindrome = 1
    while num_1 > 100:
        while num_2 > 100:
            prod = num_1 * num_2
            if is_palindrome(prod) and prod > palindrome:
                palindrome = prod
                factors = [num_1, num_2]
            num_2 -= 1
        num_2 = 999 # resets second factor
        num_1 -= 1
    return palindrome, factors

def is_palindrome(num):
    '''Determines if a number is a palindrome (same backwards as forwards).'''
    if str(num) == str(num)[::-1]:
        return True
    return False

# 5. Smallest multiple
def get_smallest_multiple():
    return 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19

# 6. Sum square difference
def get_sum_square_difference(num):
    sum_of_squares = 0
    for n in range(num+1):
        sum_of_squares += n**2
    square_of_sum = num**2 * (num + 1)**2/4
    return square_of_sum - sum_of_squares

# 7. 10001st prime
def get_nth_prime(n):
    number = 2
    count = 1
    while count < n:
        number += 1
        if is_prime(number):
            count += 1
    return number

# 8. Largest product in a series
def get_largest_product(n_factors):
    with open('8-series.txt') as file:
        number = file.read().replace('\n', '')
    largest_product = 1
    for i in range(n_factors, len(number)):
        factor_string = number[int(i-n_factors):i]
        product = 1
        for digit in factor_string:
            product = product * int(digit)
        if product > largest_product:
            largest_product = product
    return largest_product

# 9. Special Pythagorean triplet
def get_pythagorean_triplet():
    a = [1]
    pass

# 20. Factorial digit sum
def get_factorial_digit_sum(n):
    number = factorial(n)
    number = str(number)
    digits = []
    for char in number:
        digits.append(int(char))
    return sum(digits)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
get_factorial_digit_sum(100)

# 25. 1000-digit Fibonacci number
def get_1000_digit_fibo():
    # F_n \approx \phi^n/\sqrt{5}
    # when does floor(n\log(\phi) - 0.5\log(5)) + 1 = 1000?
    phi = (1 + 5**0.5)/2
    index = (999 + .5*np.log10(5))/np.log10(phi)
    return index

# 97. Large non-Mersenne prime
def get_last_10_digits(power = 7830457):
    return 28433 * pow(2, 7830457, int(1e10)) + 1
# Below is my first attempt which I scrapped.
    # number = 2
    # count = 1
    # while count < power:
    #     number = number * 2
    #     if len(str(number)) > 8:
    #         number = int(str(number)[1:])
    #     count += 1
    # print("power of 2: " + str(count))
    # return int(str(28433 * number + 1)[-10:])

# Alternative method:
def largest_nonmersenne_prime(p = 7830457):
    num = 1
    for power in range(p):
        num *= 2
        num = num % int(1e10)
    num *= 28433
    num += 1
    num = num % int(1e10)
    return int(num)
