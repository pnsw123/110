import stdio
import stdrandom
import sys

# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).


def keygen(lo, hi):
    # distinguished prime in range of lo, hi using the _primes
    # Then using choice and the while loop got two distinguished prime numbers
    # Using the prime numbers p and q found n and m

    primes = _primes(lo, hi)
    p = _choice(primes)
    q = _choice(primes)
    while p == q:
        q = _choice(primes)
    n = p * q
    m = (p - 1) * (q - 1)

    # Got a list of primes in range 2 to m-1
    # from the list found e which does not divide by m

    e_primes = _primes(2, m)
    random_sample2 = _sample(e_primes, len(e_primes))
    e = _choice(random_sample2)
    while e % m == 0:
        e = _choice(random_sample2)
    d = 1
    while d < m:
        if e * d % m == 1:
            break
        d += 1
    return n, e, d

# Encrypts x (int) using the public key (n, e) and returns the encrypted value.


def encrypt(x, n, e):
    e_x = (x**e) % n
    return e_x

# Decrypts y (int) using the private key (n, d) and returns the decrypted value.


def decrypt(y, n, d):
    d_y = (y**d) % n
    return d_y

# Returns the least number of bits needed to represent n.


def bitLength(n):
    return len(bin(n)) - 2

# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.


def dec2bin(n, width):
    return format(n, '0%db' % (width))

# Returns the decimal representation of n expressed in binary.


def bin2dec(n):
    return int(n, 2)

# Returns a list of primes from the interval [lo, hi).


def _primes(lo, hi):
    prime_empty = []

    # prime_counter program from project_2 with a bit of
    # modification
    for i in range(lo, hi):
        if i == 0 or i == 1:
            continue
        a = 2
        while a <= i / a:
            if i % a == 0:
                break
            a += 1
        # modification is to add the prime number to the list
        # instead of increasing the prime_counter

        if a > i / a:
            prime_empty += [i]
    return prime_empty

# Returns a list containing a random sample (without replacement) of k items from the list a.


def _sample(a, k):
    b = a[:]     # b is a copy of a
    c = b[:k]    # c is just a list from b up to k
    stdrandom.shuffle(c)
    return c

# Returns a random item from the list a.


def _choice(a):
    c = len(a)
    i = stdrandom.uniformInt(0, c)
    return a[i]

# Unit tests the

# Unit tests the library [DO NOT EDIT].


def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
