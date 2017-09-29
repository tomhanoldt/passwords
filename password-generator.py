#!/usr/bin/env python
import os

class PasswordGenerator:
    def __init__(self, chars = None):
        self.chars  = chars

        if not self.chars:
            self.chars = PasswordGenerator.all_printable_chars()

    @staticmethod
    def all_printable_chars():
        return ''.join(chr(x) for x in range(32, 126))

    @staticmethod
    def alpha_numeric_chars():
        str = ''.join(chr(x) for x in range(97, 123))
        str = str + ''.join(chr(x) for x in range(65, 91))
        str = str + ''.join(chr(x) for x in range(48, 58))
        str = str + '._-'
        return str

    def generate_all(self):
        return self.generate(len(self.chars))

    def generate(self, length, prefix = None):
        if length < 1:
            return

        if not prefix:
            prefix = ''

        for char in self.chars:
            permutation = prefix + char

            if length == 1:
                yield permutation

            else:
                for sub_permutation in self.generate(length - 1, prefix = permutation):
                    yield sub_permutation

if __name__ == '__main__':
    generator = PasswordGenerator()
    print 'generating words from: ' + generator.chars
    print ''

    with open("../config/az_printable/5.txt", "a") as f:
        for value in generator.generate(5):
            f.write(value + '\n')
