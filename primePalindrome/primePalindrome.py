# time complexity - O(n)
# space complexity -O(1)
def primePalindrome(n):
    """
    Find the smallest prime palindrome greater than n.
    """
    # n is prime if it is odd and the only prime factor is itself
    if n % 2 == 0:
        n += 1
    while True:
        if isPrime(n) and isPalindrome(n):
            return n
        n += 2
def isPrime(n):
    """
    Check if n is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
def isPalindrome(n):
    """
    Check if n is a palindrome.
    """
    return str(n) == str(n)[::-1]

n = int(input())
print(primePalindrome(n))
