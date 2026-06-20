

import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_decode(characters, frequencies, encoded_string):
    """Decode Huffman encoded string"""
    heap = [HuffmanNode(ch, freq) for ch, freq in zip(characters, frequencies)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        
        heapq.heappush(heap, parent)
    
    root = heap[0]
    decoded = ""
    node = root
    
    for bit in encoded_string:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if node.char is not None:
            decoded += node.char
            node = root
    
    return decoded

print("=" * 70)
print("Huffman Decoding")
print()

print("Test Case 1:")
chars1 = ['a', 'b', 'c', 'd']
freqs1 = [5, 9, 12, 13]
encoded1 = '1101100111110'
result1 = huffman_decode(chars1, freqs1, encoded1)
print(f"Characters: {chars1}")
print(f"Frequencies: {freqs1}")
print(f"Encoded string: {encoded1}")
print(f"Decoded message: {result1}")
print(f"Expected: abacd")
print()

print("Test Case 2:")
chars2 = ['f', 'e', 'd', 'c', 'b', 'a']
freqs2 = [5, 9, 12, 13, 16, 45]
encoded2 = '110011011100101111001011'
result2 = huffman_decode(chars2, freqs2, encoded2)
print(f"Characters: {chars2}")
print(f"Frequencies: {freqs2}")
print(f"Encoded string: {encoded2}")
print(f"Decoded message: {result2}")
print(f"Expected: fcbade")
print("=" * 70)
