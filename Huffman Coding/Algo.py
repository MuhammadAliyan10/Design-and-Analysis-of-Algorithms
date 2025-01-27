class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def buildFrequencyTable(data):
    frequencyTable = {}
    for char in data:
        if char in frequencyTable:
            frequencyTable[char] += 1
        else:
            frequencyTable[char] = 1
    return frequencyTable

def buildHuffmanTree(frequencyTable):
    nodes = [HuffmanNode(char, freq) for char, freq in frequencyTable.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        initialNode = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        nodes.append(initialNode)
    return nodes[0] if nodes else None

def buildCodeTable(root, code="", codeTable=None):
    if codeTable is None:
        codeTable = {}
    if root:
        if root.char is not None:
            codeTable[root.char] = code
        buildCodeTable(root.left, code + "0", codeTable)
        buildCodeTable(root.right, code + "1", codeTable)
    return codeTable

def huffmanEncode(data):
    frequencyTable = buildFrequencyTable(data)
    huffmanTree = buildHuffmanTree(frequencyTable)
    if huffmanTree and huffmanTree.left is None and huffmanTree.right is None:
        codeTable = {huffmanTree.char: "0"}
    else:
        codeTable = buildCodeTable(huffmanTree)
    encodedData = "".join([codeTable[char] for char in data])
    return encodedData, huffmanTree

def huffmanDecode(encodedData, huffmanTree):
    decodedData = []
    currentNode = huffmanTree
    for bit in encodedData:
        if bit == "0":
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
        if currentNode.char is not None:
            decodedData.append(currentNode.char)
            currentNode = huffmanTree
    return "".join(decodedData)

if __name__ == "__main__":
    data = "My name is Muhammad Aliyan."
    encodedData, huffmanTree = huffmanEncode(data)
    print(f"Encoded data: {encodedData}")
    decodedData = huffmanDecode(encodedData, huffmanTree)
    print(f"Decoded data: {decodedData}")
