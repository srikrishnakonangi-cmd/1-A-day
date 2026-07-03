def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    #adjustment for decryption
    if mode == 'decrypt':
       shift = -shift
    for char in text:
       #Upercase change
        if char.isupper():
        result += chr((ord(char) + shift - 65) % 26 + 65)
        #lowercase change
        elif char.islower():
        result += chr((ord(char) + shift - 97) % 26 + 97)
        #numbers and symbols non alphabets stay same
        else:
            result += char
  return result
