import numbers

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

symbol = ['!', '@', '#', '$', '%', '^', '&', '*' , '(' , ')' , '_' , ' ']


def ceaser(text, shift,direction):
    """Ceaser function takes three parameters: text that to be encrypted or decrypted , shift - the key (number to shift the text),
    direction to know whether to encrypt or decrypt"""
    end_text = ""
    for char in text:

        if char in alphabet:
                #   if shift value is greater than size of list
                if shift > len(alphabet) - 1:
                    shift = shift % len(alphabet)

                if direction == "encode":
                    index_char = alphabet.index(char) + shift
                else:
                    index_char = alphabet.index(char) - shift

                # if index becomes greater than size of list
                if index_char > len(alphabet) - 1:
                    index_char = index_char % len(alphabet)

                end_text += alphabet[index_char]
        else:
            end_text += char
    print(f"{direction}d message:{end_text}")



isCiphering = "yes"
while isCiphering == "yes" or isCiphering == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text,shift,direction)

    isCiphering = input("Do you want to continue ciphering(y/n): ").lower()
    if isCiphering == "no" or isCiphering == 'n':
        print("GoodBye! Do come again for ciphering your messages.")
