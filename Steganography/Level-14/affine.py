# Prints a transposition table for an affine cipher.
# a must be coprime to m=26.
def affine(a: int, b: int) -> None:
    for i in range(26):
        print(chr(i+ord('A')) + ": " + chr(((a*i+b)%26)+ord('A')))

# An example call
affine(5, 10)