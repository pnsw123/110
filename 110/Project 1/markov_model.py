from symboltable import SymbolTable
import stdio
import stdrandom
import sys


# Define a MarkovModel class
class MarkovModel:
    def __init__(self, text, k):
        self._k = int(k)
        self._st = SymbolTable()  # Create an empty symbol table
        circ_text = text + text[:k]  # Make a circular text

        # Iterate over the kgrams in the circular text
        for i in range(len(circ_text) - k):
            kgram = circ_text[i:i + k]
            next_char = circ_text[i + k]
            if kgram not in self._st:
                self._st[kgram] = SymbolTable()

            if next_char not in self._st[kgram]:
                self._st[kgram][next_char] = 0

            self._st[kgram][next_char] += 1

    # Function to get the order of the Markov model
    def order(self):
        return self._k

    # Function to get the frequency of a kgram
    def kgram_freq(self, kgram):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        if kgram not in self._st:
            return 0
        return sum(self._st[kgram].values())

    # Function to get the frequency of a character following a kgram
    def char_freq(self, kgram, c):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        if kgram not in self._st or c not in self._st[kgram]:
            return 0
        return self._st[kgram][c]

    # Function to randomly generate a character following a given kgram
    def rand(self, kgram):
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)

        next_chars = list(self._st[kgram].keys())  # Get the list of characters
        #  # Get the frequencies of these characters
        next_char_values = [self._st[kgram][char] for char in next_chars]
        # Return a random character based on the frequencies
        return next_chars[stdrandom.discrete(next_char_values)]

    # Function to generate a random text with a given length and starting kgram
    def gen(self, kgram, n):
        text = kgram
        for i in range(n - self._k):
            text += self.rand(kgram)
            kgram = text[-self._k:]
        return text

    # Function to replace unknown characters in the text using the Markov model
    def replace_unknown(self, corrupted):
        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram_before = corrupted[i - self._k:i]  # kgram before the unknown character
                kgram_after = corrupted[i + 1: i + self._k + 1]  # kgram after the unknown character
                next_chars = list(self._st[kgram_before].keys())
                probs = []  # Initialize a list
                for next_char in next_chars:
                    s = kgram_before + next_char + kgram_after
                    p = 1.0
                    for j in range(self._k + 1):
                        kgram = s[j: self._k + j]  # Get the kgram at position j in the sequence
                        # Get the character following the kgram at position j+k in the sequence
                        char = s[j + self._k]
                        if kgram not in self._st or char not in self._st[kgram]:
                            p *= 0
                            break
                        else:
                            p *= self.char_freq(kgram, char) / self.kgram_freq(kgram)
                    probs.append(p)  # Append the product of probabilities to the list
                original += next_chars[self._argmax(probs)]
            else:
                original += corrupted[i]  # If the character is known, add it to the original text
        return original

    # Function to get the index of the maximum element in a list
    def _argmax(self, a):
        return a.index(max(a))


# Main function
def _main():
    text = sys.argv[1]
    k = int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        gram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace('-', ' '), char.replace('-', ' ')))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char, model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
