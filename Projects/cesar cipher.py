alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
end_of_the_program=False
while not end_of_the_program :
    direction=input("Type 'encode' to encrypt type 'decode' to decrypt>>")
    text=input("Type your message>>").lower()
    shift=int(input("Type The Shift Number>>"))

    def cesar(direction,text,shift):
        end_text=""
        if direction=="decode":
            shift*=-1
        
        for letter in text:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=position+shift
                end_text+=alphabet[new_position]
            else:
                end_text+=letter
        print(f"The direction>{direction} The text>{end_text}")
    cesar(direction,text,shift)
    exco=input("if you want to exit type (e), if you want to continue type (c)>")
    if exco=="e":
        end_of_the_program=True
    elif exco=="c":
        end_of_the_program=False
    else:
        print("Wrong Input..")
        print("Exited")
        end_of_the_program=True