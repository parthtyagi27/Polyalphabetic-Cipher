
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def getPos(n):
    for index, letter in enumerate(alphabet):
        if n.lower() == letter.lower():
            return index;
    return -1;

def encrypt(key, text):
    key = list(key)
    text = list(text)
    keyArray = []
    textArray = []
    for index, letter in enumerate(key):
        keyArray.insert(index, getPos(letter))

    for index, letter in enumerate(text):
        textArray.insert(index, getPos(letter))

    print(keyArray)
    print(textArray)

encrypt("hey", "yeah")


