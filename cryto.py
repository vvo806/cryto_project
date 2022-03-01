"Making an encrypt and decrypt program"

from calendar import c
from ntpath import join

'''
"Ignore this. This is code using letters and numbers"
def encrypt():
    for letter in c:
        v = ord(f'{letter}') #when using ord(), 'a' = 97, 'b' = 98, etc.
        s = v - 96
        v = s

        for letter in c:
            if v > 9:
                v -= 9

        print(v)

def decrypt():
    n = chr(c)
    print(n)

choice = input('Do you want to encrypt or decrypt?(E/D): ')
if choice == 'E':
    c = input('What text do you want to turn into code?: ')
    encrypt()

else:
    c = int(input('Type number: '))
    decrypt()

'''
def encrypt():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    code = []
    for letter in c:
        l = letters.index(letter) #taking in the number of where the letter is in the list
        x = l + key #adding how much do they want to move in the list

        if x <= 25:
            code.append(letters[x]) #moving the encoded letters in the code list
        else: #if x moves out of list
            y = 25 - l
            s = key - y
            code.append(letters[s - 1])

    join = "".join(code) #printing the list together
    print(join)

def decrypt():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    code = []
    for letter in c:
        l = letters.index(letter) #taking in the number of where the letter is in the list
        x = l - key #adding how much do they want to move in the list

        if x <= 25:
            code.append(letters[x]) #moving the encoded letters in the code list
        else: #if x moves out of list
            y = 25 + l
            s = key + y
            code.append(letters[s + 1])

    join = "".join(code) #printing the list together
    print(join)

choice = input('Do you want to encrypt or decrypt?(E/D): ')
if choice == 'E':
    key = int(input('Key: ')) #how much letters to skip to make the code
    c = input('Text: ')
    encrypt()

else:
    key = int(input('Key: '))
    c = input('Code: ')
    decrypt()