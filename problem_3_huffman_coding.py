'''
Overview - Data Compression

In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data).
The compressed data, in turn, helps to reduce the transmission time from a sender to receiver.
The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data,
there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm.

You will have to implement the logic for both encoding and decoding in the following template. Also, you will need to create the sizing schemas to present a summary.
'''

import sys
import heapq
from itertools import count

UNIQUE = count()  # used for the min heap sorting in case there is a tie in the priority, since nodes can't be compared

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class HuffmanTree:
    def __init__(self):
        self.root = None

    def add_root(self, node):
        self.root = node

    def get_root(self):
        return self.root


def huffman_tree(min_heap):
    # creates the huffman tree from min heap
    huff_tree = HuffmanTree()
    while len(min_heap) > 1: # the construction of a huffman tree takes O(n) if the input is sorted which is the case
        new_node = Node()
        new_node.left = heapq.heappop(min_heap)
        new_node.right = heapq.heappop(min_heap)
        new_node.set_value(new_node.left[0] + new_node.right[0])
        heapq.heappush(min_heap, (new_node.get_value(), next(UNIQUE), new_node))
    huff_tree.add_root(min_heap.pop())
    return huff_tree


def generate_encoded_data(mapping, data):
    # encodes the given data with the mapping dictionary
    encoded_data = ""
    for char in data:  # O(n) for n chars and a mapping time of O(1)
        encoded_data += mapping[char]
    return encoded_data


def char_freq_mapping(data):
    # creates and returns a table of chars and their frequency sorted by frequency
    mapping = dict()
    for char in data: # O(n)
        mapping[char] = mapping.get(char, 0) + 1
    return [(val, next(UNIQUE), key) for key, val in sorted(mapping.items(), key=lambda x: x[1])]  # O(2n log n)
    # sorting is done in O(n log n)


def create_char_mapping(huff_tree):
    # traverses the huffman tree and maps each char to the corresponding new value
    # tuples indices 0 and 1 are priority values for sorting, idx 2 is the relevant node
    root = huff_tree.get_root()
    mapping = dict()

    def traverse(node, string=""): # O(n)
        if node:
            if type(node) is str:
                mapping[node] = string
            else:
                traverse(node.left[2], string + "0")
                traverse(node.right[2], string + "1")

    traverse(root[2])
    return mapping


def huffman_encoding(data):
    # takes a string and encodes it
    # returns the encoded data and the huffman tree for decoding
    if data == "":
        return data, None
    char_freq = char_freq_mapping(data)
    min_heap = list()
    for tup in char_freq:  # O(n) for n tuples
        heapq.heappush(min_heap, tup)

    # build huffman tree from min heap
    huff_tree = huffman_tree(min_heap)
    mapping = create_char_mapping(huff_tree)
    encoded_data = generate_encoded_data(mapping, data)
    return encoded_data, huff_tree


def huffman_decoding(data, tree):
    # takes a string of encoded data and decodes it using the appropriate huffman tree
    if tree is None:
        return data

    decoded_data = ""
    root = tree.get_root()[2]
    substring = ""
    for char in data:  # O(n) with n chars in data
        if char == "0":
            substring += "0"
            root = root.left[2]
            if type(root) is str:
                decoded_data += root
                root = tree.get_root()[2]
                substring = ""

        elif char == "1":
            substring += "1"
            root = root.right[2]
            if type(root) is str:
                decoded_data += root
                root = tree.get_root()[2]
                substring = ""

    return decoded_data


if __name__ == "__main__":
    codes = {}

    # Testcase 1
    print("----- Testcase 1 -----")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))
    binary = "".join([format(ord(letter), 'b') for letter in a_great_sentence])
    print("The binary content of the data is: {}\n".format(binary))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Testcase 2
    print("----- Testcase 2 -----")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    binary = "".join([format(ord(letter), 'b') for letter in a_great_sentence])
    print("The binary content of the data is: {}\n".format(binary))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Testcase 3
    print("----- Testcase 3 -----")
    a_great_sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ßüäöÜÄÖ!§$%&/()=?éè^^"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    binary = "".join([format(ord(letter), 'b') for letter in a_great_sentence])
    print("The binary content of the data is: {}\n".format(binary))
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))