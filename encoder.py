#samuel xu
def encode(string):
    strlist = [int(i) for i in string]
    for i, a in enumerate(strlist):
        strlist[i] = str(strlist[i] + 3)
    delimiter = ""
    encode = delimiter.join(strlist)
    return encode

def decode(string):
    decoded_password_string = ""
    for i in string:
        i = int(i) - 3
        decoded_password_string += str(i)

    return decoded_password_string
    

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        op = int(input("Please enter an option: "))
        if op == 1:
            pw = input("Please enter your password to encode: ")
            hold = encode(pw)
            print("Your password has been encoded and stored!\n")
        elif op == 2:
            print(f"The encoded password is {hold}, and the original password is {decode(hold)}.\n") # I think the formatting is fine the way it is. I added a period since the example output had one.
        elif op == 3:
            exit()

if __name__ == "__main__":
    main()
