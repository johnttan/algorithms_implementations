import heapq
# Huffman encoding for strings to binary
def encodeHuffmanTree(string):
	string = list(string)
	freqTable = {}
	stringArray = []
# 	Creates table of frequencies.
	for i in string:
		if i in freqTable:
			freqTable[i] += 1
		else:
			freqTable[i] = 1

	minHeap = []
	entry = 0
	# Loads each char into min-heap
	for i in freqTable.keys():
		iO = {
			'char': i,
			'left': False,
			'right': False
		}

		charO = [freqTable[i], entry, iO]
		heapq.heappush(minHeap, charO)
		entry += 1
	# Builds huffman tree from heap. 
	for i in range(len(freqTable.keys())-1):
		left = heapq.heappop(minHeap)
		right = heapq.heappop(minHeap)
		iO = {
			'left': left,
			'right': right
		}
		node = [int(left[0] + right[0]), entry, iO]
		heapq.heappush(minHeap, node)
		entry += 1
	encodedTree = heapq.heappop(minHeap)
	encoding = []

	return encodedTree

def traverseTree(tree, path=[], encoding={}):
	# traverses huffman tree to find encoding for each char
	if not tree[2]['left'] and not tree[2]['right']:
		print("".join([str(x) for x in path]), tree[2]['char'])
		encoding[tree[2]['char']] = "".join([str(x) for x in path])
		return
	else:
	# 0 for left child, 1 for right child
		traverseTree(tree[2]['left'], path + [0])
		traverseTree(tree[2]['right'], path + [1])
	# Returns dict of encodings for each character
	return encoding
def encodeFunc(text, encoding):
	encodeBinary = ""
	currentFrame = ""
	for i in text:
		currentFrame += i
		if encoding[currentFrame]:
			encodeBinary += encoding[currentFrame]
			currentFrame = ""
	return encodeBinary
def decodeFunc(binary, encodingTable):
	decodingTable = {}
	for i in encodingTable.keys():
		decodingTable[encodingTable[i]] = i
	currentFrame = ""
	decodedString = ""
	print(decodingTable)
	for i in binary:
		currentFrame += i
		if currentFrame in decodingTable:
			decodedString += decodingTable[currentFrame]
			currentFrame = ""
	return decodedString
def huffman(text, encode=True, encodingTable=False):
	if encode:
		encoderTree = encodeHuffmanTree(text)
		encodingTable = traverseTree(encoderTree)
		encoded = encodeFunc(text, encodingTable)
		print(encoded)
		return encoded, encodingTable
	elif not encode and encodingTable:
		decoded = decodeFunc(text, encodingTable)
		print(decoded)
		return decoded

text = 'aaaabbbccd'
encodedString, encodingTable = huffman(text)
huffman(encodedString, False, encodingTable)
