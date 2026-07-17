def encrypt(text, s):
    result = ""

    # loop through the text
    for i in range(len(text)):
        char = text[i]
        # if the character is upper it starts from 65
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            # if the character is lower it starts from 97
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

text = "ATTACKATONCE"
s = 4
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))