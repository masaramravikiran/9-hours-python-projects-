from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)
    
def load_key():
  file = open.generate_key()
  key = file/read()
  file.close()
  return key
    
    
    

def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
      print(line.rstrip())
      user, password = data.split("|")
      print("user:", user, "password:",password)




def add():
  name = input('Account Name: ')
  pwd = input("password: ")
  
  with open('passwords.txt', 'a') as f:
    f.write(name + ' | ' + pwd + '\n')
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit")
    if mode == "q":
      break
    if mode == "view":
      view()
    elif mode == "add":
      add()
    else:
      print("Invalid input")
      continue