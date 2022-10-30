import random


def password():
    while True:
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "~!@#$%^&*()_+{}:<>?-=[]\;',./"

        string = lower + upper + numbers + symbols
        x = int(input("Password length: "))
        if x < 4:
            print("Password cannot be less than 4 characters")
        else:
            length = x
            password = "".join(random.sample(string, length))
            print("Your new password is: " + password)
            continue


password()


