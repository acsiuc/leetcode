strings = []

def encode(strings):
    encoded_string = ''

    for string in strings:
        encoded_string+=str(len(string))+"$" + string

    return encoded_string
    
encoded_string = encode(strings)

def decode(encoded_string):
    decoded_strings = []
    length_of_word = ''
    counter = 0
    while counter < len(encoded_string):
        while encoded_string[counter] != '$':
            character = encoded_string[counter]
            length_of_word+=character
            counter+=1
            

        word = encoded_string[counter+1:counter+1+int(length_of_word)] 

        decoded_strings.append(word)

        
        counter += len(word) +1
        length_of_word = ''
        
    
    return decoded_strings
            



if __name__ == "__main__":

    print(encode(strings))
    print(decode(encoded_string))