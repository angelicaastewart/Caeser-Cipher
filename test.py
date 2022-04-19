'''
CSCI 120 programming assignment [100pts]
Assumptions:
* plain_text only contains letters from 
the english alphabet
* we can have both lower and upper case
letters in the plain_text
* plain_text can be of any length
* key is an arbitrary valued integer

Hint: lookup ord( )	and chr( ) function in Python

'''
ALPHABET_START = ord('A')
ALPHABET_END = ord('Z')

alphabet_start = ord('a')
alphabet_end = ord('z')

def caesar_encrypt(plain_text, key) -> str:
    '''
    function to encrypt given plain_text with
    key using caesar cipher 
    '''
    key %= 26	#ensure 0<=key<=26
    cipher_text = ''
    '''
    TODO:
    [50pts]
    * Implement caesar cypher below so that 
    each letter in plain_text is shifted by 
    key steps to the right
    
    * Return the resulting cipher text
    
    '''
    #loop through to get each value of the orginal ascii
    for i in range(0, len(plain_text)):
    #get the original ascii of plaintext
        original_ascii = ord(plain_text[i]) #returns an int
    #check if uppercase
        if original_ascii >= ALPHABET_START and original_ascii  <= ALPHABET_END:
    #loop through each letter in plain text

#encrypts capital letter
            if original_ascii + key > ALPHABET_END:
                original_ascii= original_ascii - (26-key)
            else:
                original_ascii = original_ascii + key
#check if lowercase
        elif original_ascii >= alphabet_start and original_ascii <= alphabet_end:
#encrypt lowercase
            if original_ascii + key > alphabet_end:
                original_ascii= original_ascii - (26-key)
            else:
                original_ascii = original_ascii + key

        else:
            original_ascii=original_ascii

        cipher_text= cipher_text+chr(original_ascii)

    return cipher_text


def caesar_decrypt(cipher_text,key) -> str:
    '''
    function to decrypt given cipher_text with
    # key using caesar cipher 	
    # '''
    key %= 26 #ensure 0<=key<=26
    plain_text = ''
    # '''
    # TODO:
    # [50pts]
    # * Using your knowledge of caesar cipher, decrypt the given
    # cipher_text by shifting each letter in cipher_text string to
    # the left by key steps
    
    # * Return the resulting plain text
    
    # '''	
    #get the original ascii value of the plain cipher_text
    for i in range (0, len(cipher_text)):
        original_ascii = ord(cipher_text[i]) #returns an int
#checks uppercase
        if original_ascii >= ALPHABET_START and original_ascii<= ALPHABET_END:
            if original_ascii - key < ALPHABET_START:
                original_ascii= original_ascii + (26-cipher_number)
            else:
                original_ascii= original_ascii - key
#checks lowercase
        elif original_ascii >= alphabet_start and original_ascii <=  alphabet_end:
            if original_ascii - key < alphabet_start:
                original_ascii= original_ascii + (26-key)
            else:
                original_ascii= original_ascii - key
        else:
            original_ascii = original_ascii

        plain_text= plain_text + chr(original_ascii)

    return plain_text

plain_text = "Attack at Dawn"  #Define the message
key = 412  #Define the key

#encrypt and store cypher text
cipher_text = caesar_encrypt(plain_text,key) 

#decrypt and store plain text
decrypted_msg = caesar_decrypt(cipher_text,key)
