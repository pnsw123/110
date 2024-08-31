import stdio
import math


# Entry point.
# The Constants for the program.
ETA = 9.135e-4
RHO = 0.5e-6
T = 297.0
R = 8.31457
METER_PER_PIXEL = 0.175e-6
# standard Input
displacements = stdio.readAllFloats()
# number of displacements
n = len(displacements)


# main function to calculate the diffusion coefficient
def main():
    K = (6 * math.pi * _var() * ETA * RHO) / T
    NA = R / K
    # write the result
    stdio.writef(str('%e') + " " + str('%e'), K, NA)  # type: ignore


# var function to calculate the sum of the square of the displacements
def _var():
    total = 0
    for i in range(n):
        total += (displacements[i] * METER_PER_PIXEL) ** 2
    return total / (2 * n)


if __name__ == '__main__':
    main()
