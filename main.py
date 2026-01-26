from auth import register, login

while True:
    choice = input("\n1 Register\n2 Login\n3 Exit\n> ")

    if choice == "1":
        u = input("Username: ")
        p = input("Password: ")
        print(register(u, p))

    elif choice == "2":
        u = input("Username: ")
        p = input("Password: ")
        print(login(u, p))

    elif choice == "3":
        break
