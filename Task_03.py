def main():
    import re

    password = input("Enter a password: ")
    while len(password) < 8:
        password = input("Enter another password: ")

    if len(password) >= 8:
        upper = re.search(r'[A-Z]', password)
        lower = re.search(r'[a-z]', password)
        spcl = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
        num = re.search(r'[0-9]', password)

        if upper and lower and spcl and num:
            print("Password is strong")
        elif upper and not lower and spcl and num:
            print("Password is weak, add lower case letters to make it strong")
        elif not upper and lower and spcl and num:
            print("Password is weak, add upper case letters to make it strong")
        elif upper and lower and not spcl and num:
            print("Password is weak, add special characters to make it strong")
        elif upper and lower and spcl and not num:
            print("Password is weak, add numbers to make it strong")
    else:
        print("Password should be of at least 8 letters")


if __name__ == "__main__":
    main()
