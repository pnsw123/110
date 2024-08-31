import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        # Initialize an empty list for the blobs in pic.
        self._blobs = []

        # Create a 2D list of booleans called marked, having the same dimensions as pic.
        marked = stdarray.create2D(pic.width(), pic.height(), False)

        # Enumerate the pixels of pic, and for each pixel (i, j):
        # Create a Blob object called blob.
        # Call self._findBlob() with the right arguments.
        # Add blob to self.blobs if it has a non-zero mass.
        for i in range(pic.width()):
            for j in range(pic.height()):
                blob = Blob()
                self._findBlob(pic, tau, i, j, marked, blob)
                if blob.mass() > 0:
                    self._blobs.append(blob)

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):
        # Create an empty list called beads.
        beads = []

        # Enumerate the blobs in self._blobs, and for each blob b:
        # If b has mass >= pixels, add b to beads.
        for b in self._blobs:
            if b.mass() >= pixels:
                beads.append(b)

        # Return beads.

        return beads

    # Identifies a blob using depth-first search.
    # The parameters are the picture (pic), luminance threshold (tau), pixel column (i),
    # pixel row (j), 2D boolean matrix (marked), and the blob being identified (blob).
    def _findBlob(self, pic, tau, i, j, marked, blob):
        # Base case: return if pixel (i, j) is out of bounds, or if it is marked, or if its
        # luminance is less than tau.
        if i < 0 or i >= pic.width() or j < 0 or j >= pic.height() or marked[i][j] or \
                luminance.luminance(
                pic.get(i, j)) < tau:
            return None
        # Mark the pixel.
        marked[i][j] = True

        # Add the pixel to blob.
        blob.add(i, j)

        # Recursively call self._findBlob() on the N, E, W, S pixels.
        self._findBlob(pic, tau, i, j + 1, marked, blob)
        self._findBlob(pic, tau, i + 1, j, marked, blob)
        self._findBlob(pic, tau, i, j - 1, marked, blob)
        self._findBlob(pic, tau, i - 1, j, marked, blob)


# Unit tests the data type (DO NOT EDIT).
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef('%d Beads:\n', len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef('%d Blobs:\n', len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == '__main__':
    _main()
