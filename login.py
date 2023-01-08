from time import sleep
import random
import string
import secrets


def register():
    db = open("accounts.txt", "r")
    Username = input("Enter a username:")
    print('1. Manual password setting'
        '\n2. Auto generated password setting')
    pass_sel = input('Please select any option: ')
    
    if pass_sel == '1':
        Password = input("Create password:")
        Password1 = input("Confirm Password:")
        
        d = []
        f = []
        for i in db:
            a,b = i.split(";")
            b = b.strip()
            #c = a,b
            d.append(a)
            f.append(b)
        data = dict(zip(d,f))

        if Password != Password1:
            print('Password does not match')
            register()
        else:
            if len(Password)<=4:
                print('Password is too short')
                register()
            elif Username in d:
                print('User already exists')
                register()
            else:
                db = open("accounts.txt", "a")
                db.write(Username + ';' + Password + '\n')
                print('Successfully registered')

    elif pass_sel == '2':
        char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:<=>?@[\]^_`{|}~"
        Password = ''.join(secrets.choice(char_seq) for i in range(8))
        #print(password)
        d = []
        f = []
        for i in db:
            a,b = i.split(";")
            b = b.strip()
            #c = a,b
            d.append(a)
            f.append(b)
        data = dict(zip(d,f))
        db = open("accounts.txt", "a")
        db.write(Username + ';' + Password + '\n')
        print('Successfully registered')
                
    else:
        print('Select correct option. Please try again.')
    



def access():
    Username = input("Enter your username:")
    Password = input("Enter your Password:")
    db = open("accounts.txt", "r")
    
    if not len(Username or Password) < 1:
        d = []
        f = []
        for i in db:
            a,b = i.split(";")
            b = b.strip()
            #c = a,b
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))   
        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print('Login success')
                    else:
                        print('Username or Password incorrect')
                except:
                    print('Incorrect username or password')
            else:
                print('Username or Password does not exist')
        except:
                print('Username or Password does not exists')
    else:
        print('Please enter a value: ')


def view():
    file = open('accounts.txt', 'r')
    print(file.read())




while True:
    f = open('accounts.txt','a')
    print('-----Menu-----')
    print('1. Login'
        '\n2. Register'
        '\n3. View'
        '\n4. Exit')
    select = input('Enter your selection: ')

    if select == '1':
        access()
    elif select == '2':
        register()
    elif select == '3':
        view()
    elif select == '4':
        sleep(2)
        print("Exit successful")
        exit()
    else:
        print('Invalid character. Please try again. ')

