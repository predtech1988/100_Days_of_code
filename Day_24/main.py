#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []

with open("./Input/Names/invited_names.txt")as f:
    names_list = (f.read().split("\n"))

def replace_name(name):
    with open("./Input/Letters/starting_letter.txt")as letter:
        letter_text = letter.read().replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.docx", "w") as output_letter:
            output_letter.write(letter_text)



def save_letter():
    for name in names_list:
        replace_name(name)

save_letter()
