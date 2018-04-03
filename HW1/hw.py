import random
#turn text into list of numbers (ASCII values)
def encode(text):
    text = text.lower()
    lst = [(ord(letter) - ord('a')) for letter in text if letter.isalpha()]
    return lst

#turn list of ASCII values into text
def decode(lst):
    text = ''.join([chr(ord('a')+code) for code in lst])
    return text

def shift(pt,k):
    'plaintext pt, shift k'
    ptlst = encode(pt)
    ctlst = [(x+k) % 26 for x in ptlst]
    return decode(ctlst)


## My Code

def simpleshiftbreak(ct):
    countList = [(ct.count(letter)) for letter in ct if letter.isalpha()]
    supposedlyEIndex = countList.index(max(countList))
    supposedlyE = ct[supposedlyEIndex]
    key = (ord(supposedlyE) - ord('e')) % 26
    return key

def clean(text):
    return ''.join([l for l in text.lower() if l.isalpha()])

# a and b define range of text-length, inclusively
# tests is number of tests to be run each text-length
def testsimple(a, b, tests=200):
    infile = open('innocents.txt', 'r')
    text = infile.read()
    infile.close()
    text = clean(text)
    for size in range(a, b + 1):
        accuracy = testTextSize(size, text, tests)
        print(size, accuracy)

def consCypher(length, text):
    pt = text[0:length]
    text = text[length:]
    key = random.randint(1, 26)
    cypher = shift(pt, key)
    return (cypher, key, text)

def testTextSize(size, text, tests):
    hits = 0
    for test in range(0, tests):
        cypher = consCypher(size, text)
        text = cypher[2]
        potentialKey = simpleshiftbreak(cypher[0])
        #print(cypher[0], cypher[1], potentialKey)
        if potentialKey is cypher[1]:
            hits += 1

    return hits / tests
