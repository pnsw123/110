import sys
import math
from picture import Picture
from blob_finder import BlobFinder
import stdio

# ENTRY POINT


def main():
    # Get command-line arguments

    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frame = sys.argv[4:]
    # Read image from file

    pic = Picture(frame[0])
    # Create a BlobFinder object

    bf = BlobFinder(pic, tau)
    # Find previous beads

    prevbeads = bf.getBeads(pixels)
    for i in range(5, len(sys.argv)):

        # Read image from file
        pic = Picture(sys.argv[i])

        # Create a BlobFinder object
        bf = BlobFinder(pic, tau)

        # Find current beads
        currbeads = bf.getBeads(pixels)

        # For each bead currBead in currBeads
        for currbead in currbeads:

            closest = math.inf
            # find a bead prevBead from prevBeads that
            # is no further than delta and is closest to currBead.

            for prevbead in prevbeads:
                dist = currbead.distanceTo(prevbead)
                if dist <= delta and dist < closest:

                    closest = dist
                    # if such a bead is found, write its distance
                    # (using format string ’%.4f\n’) after saving in closest.
            if closest != math.inf:
                stdio.writef('%.4f\n', closest)
        stdio.writeln()
        # Set prevBeads to currBeads.
        prevbeads = currbeads


if __name__ == '__main__':
    main()
