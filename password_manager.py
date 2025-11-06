print("Welcome to Passsword Manager.")

master = "1208"

masin = input("Please Enter Your Master Password: " )

if masin != master:
    print("Wrong Password.")
    quit()

def view():
    print("Here is your password list!")
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            a,b = data.split("|")
            print(f"username: {a}\npassword: {b}")
    
def create():
    name = input("Enter your Account Name: ")
    pwd = input("Enter Your password: ")
    with open("password.txt", 'a') as f:
        f.write(name+"|"+pwd+"\n")

while True:
    option = input("Create New Password or View Password List or Remove Password(C/V) ").lower()
    if option == "c":
        create()
    elif option == "v":
        view()
    else:
        quit()