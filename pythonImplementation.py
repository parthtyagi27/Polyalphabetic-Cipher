
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
    encryptedString = ""
    for index, letter in enumerate(key):
        keyArray.insert(index, getPos(letter))

    counter = 0
    for index, letter in enumerate(text):
        if counter >= len(keyArray):
            counter = 0;
        position = getPos(letter)
        print("Shifting " + str(position) + " with " + str(keyArray[counter]))
        position += keyArray[counter]
        if position > len(alphabet):
            position = position % len(alphabet)
        counter += 1
        encryptedString += alphabet[position]
        
    print(keyArray)
    return encryptedString;

print(encrypt("hey", "yeah"))


