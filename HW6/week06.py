from __future__ import annotations
from pympler import asizeof 


class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


def get_frequencies(message):
    freq = {}

    for char in message:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


def remove_smallest(forest):
    smallest = forest[0]

    for node in forest:
        if node.frequency < smallest.frequency:
            smallest = node

    forest.remove(smallest)
    return smallest


def build_huffman_tree(message):
    freq = get_frequencies(message)
    forest = []

    for char in freq:
        forest.append(Node(char, freq[char]))

    while len(forest) > 1:
        n1 = remove_smallest(forest)
        n2 = remove_smallest(forest)

        parent = Node(None, n1.frequency + n2.frequency)
        parent.left = n1
        parent.right = n2

        forest.append(parent)

    return forest[0]


def make_codes(node, code, codes):
    if node.is_leaf():
        if code == "":
            codes[node.symbol] = "0"
        else:
            codes[node.symbol] = code
        return

    make_codes(node.left, code + "0", codes)
    make_codes(node.right, code + "1", codes)


def encode(message, codes):
    encoded = ""

    for char in message:
        encoded += codes[char]

    return encoded


def decode(encoded, root):
    decoded = ""
    node = root

    for bit in encoded:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.is_leaf():
            decoded += node.symbol
            node = root

    return decoded


def report(codes, message, encoded, root):
    print("Original:", message)
    print("Encoded:", encoded)
    print()

    print("Codes:")
    for char in codes:
        if char == " ":
            print("' ':", codes[char])
        else:
            print(char + ":", codes[char])

    print()

    ascii_bits = len(message) * 8
    huffman_bits = len(encoded)
    tree_bits = asizeof.asizeof(root) * 8

    print("ASCII bits:", ascii_bits)
    print("Huffman bits:", huffman_bits)
    print("Bits saved:", ascii_bits - huffman_bits)
    print("Tree size in bits:", tree_bits)


if __name__ == "__main__":
    message = "HELLO WORLD"

    root = build_huffman_tree(message)

    codes = {}
    make_codes(root, "", codes)

    encoded = encode(message, codes)
    decoded = decode(encoded, root)

    report(codes, message, encoded, root)
    print("Decoded:", decoded)