
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
        
    print(f"Here's the {direction}d result: {end_text}")
    

a=False
while a is False:
    d = int(input("Type 1 for 'encode' to encrypt, type 2 'decode' to decrypt:\n"))
    if d==1:
        direction ="encode"
    elif d==2:
        direction="decode"
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

    b=input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if b=="no":
        print("Goodbye")
        a=True
    
