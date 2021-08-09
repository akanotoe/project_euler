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
    for n in range(2, int(number**0.5)):
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
        num_2 = 999
        num_1 -= 1
    return palindrome, factors

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

# 97. Large non-Mersenne prime
def get_last_10_digits(power = 7830457):
    # number = 2
    # count = 1
    # while count < power:
    #     number = number * 2
    #     if len(str(number)) > 8:
    #         number = int(str(number)[1:])
    #     count += 1
    # print("power of 2: " + str(count))
    # return int(str(28433 * number + 1)[-10:])
    return 28433 * pow(2, 7830457, int(1e10)) + 1
