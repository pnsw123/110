import rsa
import stdio
import sys


# Entry point.
def main():
    # Input of n and d values

    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # compute number of bits per character needed for encryption.

    width = rsa.bitLength(n)

    # accept message(as a binary string) from a standard output

    message = stdio.readAll()

    # create a for loop for i e[0, l-1]

    for i in range(0, (len(message)-1), width):
        s = message[i: i + width]

        # Set y to decimal representation of the binary string s.

        y = rsa.bin2dec(s)
        x = rsa.decrypt(y, n, d)

        # decrypt

        stdio.write(chr(x))


if __name__ == '__main__':
    main()
