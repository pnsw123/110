from markov_model import MarkovModel
import stdio
import sys


# Entry point.
def main():
    k = int(sys.argv[1])  # Accept command-line arguments k (int) and n (int).
    n = int(sys.argv[2])
    text = sys.stdin.read().strip()  # Initialize text to text read from standard input
    Markov = MarkovModel(text, k)    # Create a Markov model using text and k.

    random_text = text[:k]  # generate a random text
    for i in range(n - k):
        next_char = Markov.rand(random_text[-k:])
        random_text += next_char
    stdio.writeln(random_text)  # Write the random text to standard output


if __name__ == '__main__':
    main()
