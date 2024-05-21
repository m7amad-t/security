def caesarCipher(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            ascii_val = ord(char)
            if char.isupper():
                shifted_char = chr((ascii_val - 65 + key) % 26 + 65)
            else:
                shifted_char = chr((ascii_val - 97 + key) % 26 + 97)
            result += shifted_char
        else:
            result += char
    return result
text = "Information Security"
key = 4
encryptedMessage = caesarCipher(text, key)
print("Encrypted Message Is : ", encryptedMessage)
decryptedMessage = caesarCipher(encryptedMessage, -key)
print("Decrypted Message Is : ", decryptedMessage)
