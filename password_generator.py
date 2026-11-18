import random


def main():
    while True:
        option = show_menu()
        if option == 1:
            password_list = generate_password()
            random.shuffle(password_list)
            password = "".join(password_list)

            if password == "":
                print("Please select at least one of the four character types")

            else:
                print(f"This is your password: {password}")

        elif option == 2:
            print("Thank you for using password generator\nGoodbye")
            break
            
        again = input("Generate another password? (y/n)").strip().capitalize()
        if again == "Y" or again == "Yes":
            continue
        else:
            print("Thank you for using password generator\nGoodbye")
            break


#=========================================================
def show_menu():
    menu = '''
    ______________________________
          Password Generator
    ______________________________
    1. Generate password
    2. Exit'''

    print(menu)

    while True:
        try:
            option = int(input("Choose an option: "))
            if option < 1 or option > 2:
                print("Invalid option, please try again.")
                continue
        except ValueError:
            print("Invalid option, please try again.")

        else:
            return option


#=========================================================
def password_quiz():
    pass_dict = {
        "pass_len" : 0,
        "pass_up" : "n",
        "pass_low" : "n",
        "pass_num" : "n",
        "pass_symbol": "n"
    }
    while True:
        try:
            pass_len = int(input("Enter password length: "))
            if pass_len < 4:
                print("Password length must be at least 4 characters")
                continue
            else:
                pass_dict["pass_len"] = pass_len

            pass_up = input("Include uppercase letters? (y/n)").strip().capitalize()
            pass_low = input("Include lowercase letters? (y/n)").strip().capitalize()
            pass_num = input("Include numbers? (y/n)").strip().capitalize()
            pass_symbol = input("Include symbols? (y/n)").strip().capitalize()

            if pass_up == "Yes" or pass_up == "Y":
                pass_dict["pass_up"] = "y"
            
            if pass_low == "Yes" or pass_low == "Y":
                pass_dict["pass_low"] = "y"

            if pass_num == "Yes" or pass_num == "Y":
                pass_dict["pass_num"] = "y"

            if pass_symbol == "Yes" or pass_symbol == "Y":
                pass_dict["pass_symbol"] = "y"

        except ValueError:
            print("Invalid input, please try again.")

        else:
            return pass_dict
        
            
#=========================================================
def generate_password():
    password_dict = password_quiz()

    
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"

    password_char = []

    
    password_len = password_dict["pass_len"]
    i = 0
    while i < password_len:
        if password_dict["pass_up"] == "y":
            p = random.choice(upper_letters)
            password_char.append(p)
            
            if len(password_char) == password_len:
                break

        if password_dict["pass_low"] == "y":
            p = random.choice(lower_letters)
            password_char.append(p)
            
            if len(password_char) == password_len:
                break
        
        if password_dict["pass_num"] == "y":
            p = random.choice(numbers)
            password_char.append(p)

            if len(password_char) == password_len:
                break
            

        if password_dict["pass_symbol"] == "y":
            p = random.choice(symbols)
            password_char.append(p)
            
            if len(password_char) == password_len:
                break

        i += 1
    
    return password_char

main()