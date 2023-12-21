import random
letters=['a','b','c','d','e','f','h','h','i','j','k','l','m','n',
         'o','p','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X'
 ,'Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']

symbols=['!','#','$','%','&','&','*','+']
def password_creater(nr_letters, nr_numbers, nr_symbols):
    password=""
    i=0
    while i <nr_letters:
        letter=random.choice(letters)
        if  letter not in password:
            password+=letter
        else:
            i-=1
        i+=1
    j=0
    while j< nr_numbers:
        number=random.choice(numbers)
        if number not in password:
            password+=number
        else:
            j-=1
        j+=1

    k=0
    while k < nr_symbols:
        symbol=random.choice(symbols)
        if symbol not in password:
            password+=symbol
        else:
            k-=1
        k+=1
    p_list=[]
    for char in password:
        p_list.append(char)
    mix_password=""            
    for i in range(len(p_list)):
        char=random.choice(p_list)
        mix_password+=char
        p_list.remove(char)
    return f"Your password is {mix_password}"
nr_letters=int(input("How many letters would you like in your password>"))
nr_numbers=int(input("How many number would you like in your password>"))
nr_symbols=int(input("How many symbol would you like in your password>"))
while True:
    print(password_creater(nr_letters,nr_numbers,nr_symbols))
    choice=input("Do you like your password if you want to create a new one press (y) if you like press(e)")
    if choice=="y":
        continue
    elif choice=="e":
        print("Sonlandi")
        break