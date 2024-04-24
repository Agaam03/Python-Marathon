from libs import welcome_message, exit_program
from Games import tupai
from Tools import warung


def menu():
    user_option = int(input("Menu Program : \n 1. Games Tawamure \n 2. Warung Mini \n 3. Keluar Program\n\n Silahkan Pilih : "))

    if user_option == 1 :
        tupai.start()
    elif user_option == 2 :
        warung.start()
    elif user_option == 3 :
        exit_program()
    else :
        print("Hanya boleh pilih program yang tersedia")

def main():
    welcome_message()
    menu() 
    
if __name__ == '__main__':
    main()






