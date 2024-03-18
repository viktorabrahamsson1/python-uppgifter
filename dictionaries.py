def print_menu():
    print("Vad vill du göra?")
    print("=================")
    print("1. Lägga till eller ändra en adress")
    print("2. Söka en adress")
    print("3. Ta bort en adress ur listan")
    print("4. Visa hela registret")
    print("0. Avsluta")


def is_valid_email(email):
    if "@" in email and email.index("@") > 0 and email.find(".") > email.index("@"):
        return True
    return False



def add_or_update_address(register):
    namn = input("Namn: ")
    email = input("Email: ")

    if is_valid_email(email):
        if email in register.values():
            ny_email = input("Mata in din nya email adress: ")
            register[namn] = ny_email
            print(f"{namn}'s email har ändrats till {ny_email}\n")
        else:
            print(f"{namn} har lagts till i registret med emailen {email}\n")
            register[namn] = email
    else:
        print("Ogiltig emailadress. Försök igen.")


def search_address(register):
    email = input("Sök efter en email adress: ")

    if email in register.values():
        print(f"Emailadressen {email} finns i registret.\n")
    else:
        print("Email adressen finns inte i registret.\n")


def remove_address(register):
    email = input("Sök efter en email adress att ta bort: ")

    if email in register.values():
        for key, value in register.items():
            if value == email:
                del register[key]
                print(f"Email adressen {email} är borttagen från registret.\n")
                break
    else:
        print("Email adressen fanns inte i registret.\n")


def print_register(register):
    if not register:
        print("Registret är tomt.")
    else:
        for key, value in register.items():
            print(f"Namn: {key}, Email: {value}")
    print()


def init():
    register = {}
    while True:
        print_menu()
        try:
            svar = int(input("Välj 1 - 4 eller 0: "))
            if svar == 1:
                add_or_update_address(register)
            elif svar == 2:
                search_address(register)
            elif svar == 3:
                remove_address(register)
            elif svar == 4:
                print_register(register)
            elif svar == 0:
                break
            else:
                print("Ogiltigt val. Försök igen.\n")
        except ValueError:
            print("Ogiltigt val. Ange en siffra.\n")


if __name__ == "__main__":
    init()

