# EXP77.py - Huffman Tree and Huffman Codes

import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(characters, frequencies):
    """Build Huffman tree and generate codes"""
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
    codes = {}
    
    def generate_codes(node, code):
        if node is None:
            return
        
        if node.char is not None:
            codes[node.char] = code if code else '0'
            return
        
        generate_codes(node.left, code + '0')
        generate_codes(node.right, code + '1')
    
    generate_codes(root, '')
    return sorted(codes.items())

print("=" * 70)
print("Huffman Tree and Huffman Codes")
print()

print("Test Case 1:")
chars1 = ['a', 'b', 'c', 'd']
freqs1 = [5, 9, 12, 13]
result1 = build_huffman_tree(chars1, freqs1)
print(f"Characters: {chars1}")
print(f"Frequencies: {freqs1}")
print(f"Huffman Codes: {result1}")
print()

print("Test Case 2:")
chars2 = ['f', 'e', 'd', 'c', 'b', 'a']
freqs2 = [5, 9, 12, 13, 16, 45]
result2 = build_huffman_tree(chars2, freqs2)
print(f"Characters: {chars2}")
print(f"Frequencies: {freqs2}")
print(f"Huffman Codes: {result2}")
print("=" * 70)
