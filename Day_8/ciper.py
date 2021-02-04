alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_running = True

while is_running == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, 'exit' to exit program:\n")
    if (direction == "exit"):
        is_running = False
        print("Exiting the program")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceaser(direction, text, shift):
        encoded_text = []
        
        for char in text:
            if char not in alphabet: 
                encoded_text.append(char)
                continue
            else:
                char_index = alphabet.index(char) 
                if direction == "encode":
                    char_index += (shift % 26)
                    if char_index < len(alphabet):
                        encoded_text.append(alphabet[char_index])
                    else:
                        char_index -= len(alphabet)
                        encoded_text.append(alphabet[char_index])
                elif direction == "decode":
                    char_index -= (shift % 26)
                    encoded_text.append(alphabet[char_index])
                else:
                    print("No such a command")
                    break
        print("".join(encoded_text))
    ceaser(direction, text, shift)