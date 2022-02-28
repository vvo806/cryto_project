"Making an encrypt and decrypt program"

from calendar import c
from ntpath import join

from numpy import append
'''
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
    count = 1
    for letter in c:
        if letter in letters:
            for l in letters:
                letters[0] = letter
                
                print(letters[0])
            #a = letters[l+key]
        #for l in letters:
            #   print(letters[l+key])
    #print(letters[l+key])

key = int(input('Key: '))
c = input('What text do you want to turn into code: ')
encrypt()