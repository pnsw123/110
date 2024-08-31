from markov_model import MarkovModel
import stdio
import sys


# Entry point.
def main():
    k = int(sys.argv[1])  # Accept k (int) and corrupted (str)
    s = str(sys.argv[2])  # as command-line arguments.
    text = sys.stdin.read()  # Initialize text to text
    Markov = MarkovModel(text, k)  # Create a Markov model using text and k.

    decoded_text = Markov.replace_unknown(s)  # Use the model to decode corrupted.

    stdio.writeln(decoded_text)  # Write the decoded text to standard output


if __name__ == '__main__':
    main()
