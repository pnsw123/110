import rsa
import stdio
import sys

# Entry point.


def main():

    # Accept public-key n (int) and e (int) as command-line arguments.

    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # compute number of bits per character needed for encryption.

    width = rsa.bitLength(n)

    # accept message(as a binary string) from a standard output

    message = stdio.readAll()
    for c in message:
        x = ord(c)

        # encrypt

        encrypt = rsa.encrypt(x, n, e)
        y = rsa.dec2bin(encrypt, width)

        # Output

        stdio.write(y)


if __name__ == '__main__':
    main()
