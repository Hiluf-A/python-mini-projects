from cryptography.fernet import Fernet
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key) 



def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user , "| Pasword:", fer.decrypt(passw.encode()).decode())
            


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
    

mode = input("Would you like to add a new password or view existing ones (view/add) or press q to quit: ").strip().lower()

while True:
    if mode == "q":
        break
    elif mode == "view":
        view()
        mode = input("Would you like to add a new password or view existing ones (view/add) or press q to quit: ").strip().lower()
    elif mode == "add":
        add()
        mode = input("Would you like to add a new password or view existing ones (view/add) or press q to quit: ").strip().lower()
    else:
        print("Invalid mode")
        mode = input("Would you like to add a new password or view existing ones (view/add) or press q to quit: ").strip().lower()
    
        
