import rsa
import stdio
import sys

# Accept lo (int) and hi (int) as command-line arguments.
lo = int(sys.argv[1])
hi = int(sys.argv[2])

# Get public/private keys as a tuple

keys = rsa.keygen(lo, hi)
n, e, d = keys
# Entry point.
# Write the three values in the tuple, separated by a space.


def main():
    stdio.write(str(n) + " ")
    stdio.write(str(e) + " ")
    stdio.write(str(d) + " ")


if __name__ == '__main__':
    main()
