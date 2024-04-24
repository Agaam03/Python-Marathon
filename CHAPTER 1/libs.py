import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome_message():
    style = "*" * (len(PC_NAME) + 6)
    print(style)
    print(f"** {PC_NAME} **")
    print(style)

def exit_program():
    print("\n PROGRAM AKAN BERHENTI")
    start = 3
    while start > 0 :   
        sleep(1)
        print(f"{start}...")
        start -= 1
    print("PROGRAM TELAH SELESAI!!!")
    
if __name__ == '__main__':
    welcome_message()
    exit_program()