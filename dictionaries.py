def alternativ():
    print("Vad vill du göra?")
    print("=================")
    print("1. lägga till eller ändra en adress \n2. söka en adress \n3. ta bort en adress ur listan \n4. visa hela registret \n0. avsluta \n")


def init():  
    register = {}
    svar = None
    while svar != 0:
        alternativ()
        svar = int(input("Välj 1 - 4 eller 0: "))
        if svar == 1:
            namn = input("namn: ")
            email = input("email: ")

            if email in register.values():
                ny_email = input("Mata in din nya email adress: ")
                register[namn] = ny_email   
                print(f"{namn}'s email har ändrats till {email}\n")
            else: 
                print(f"{namn} har lagts till i registret med emailen {email}\n")
                register[namn] = email
                

        elif svar == 2:
            email = input("Sök efter en email adress: ")

            if email in register.values():
                print(f"Den här adressen fanns i registret: {email}\n")
            else:
                print("Emailen finns inte i registret\n")

        elif svar == 3:
            email = input("Sök efter en email adress att ta bort: ")
            if email in register.values():
                for key, value in register.items():
                    if value == email:
                        del register[key]  
                        print(f"adressen: {email} är borttagen\n")
                        break
            else:
                print(f"{email} fanns inte i registret\n")

        elif svar == 4:
            if not register:
                print("Registret är tomt")
            else:
                for key, value in register.items():
                    print(f"namn: {key}, email: {value}")
        elif svar == 0:
            break

init()










