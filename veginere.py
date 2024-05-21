def vigenerEncrypt(plain_text, key):
    encrypted_text = ""
    key_index = 0
    for pi in plain_text:
        if pi.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1
            ki = ord(key_char.lower()) - ord('a')
            if pi.isupper():
                ci = chr((ord(pi) - ord('A') + ki) % 26 + ord('A'))
            else:
                ci = chr((ord(pi) - ord('a') + ki) % 26 + ord('a'))
            encrypted_text += ci
        else:
            encrypted_text += pi
    return encrypted_text
def vigenereDecrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0
    for ci in encrypted_text:
        if ci.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1
            ki = ord(key_char.lower()) - ord('a')
            if ci.isupper():
                pi = chr((ord(ci) - ord('A') - ki) % 26 + ord('A'))
            else:
                pi = chr((ord(ci) - ord('a') - ki) % 26 + ord('a'))
            decrypted_text += pi
        else:
            decrypted_text += ci
    return decrypted_text


plain_text = "Information Security"
key = "Bee"
encrypted_text = vigenerEncrypt(plain_text, key)
print("Encrypted Text Is= ", encrypted_text)
decrypted_text = vigenereDecrypt(encrypted_text, key)
print("Decrypted Text Is = ", decrypted_text)
