
import random
import string

lenf=int(input("How much length of password do you want:"))

def password():
    global lenf
    char=string.ascii_letters+string.digits
    password=""
    for index in range(lenf):
        password=password+random.choice(char)
    print("Your Password is:",password)
        

password()


