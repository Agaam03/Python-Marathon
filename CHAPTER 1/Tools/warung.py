import main
def start():
    while True :
        print("Ini Warung Mini")
        play_again = input("Kembali Ke Menu Utama : [y/n]")
        
        if play_again == "y" and "Y":
            main.menu()
        
    
if __name__ == "__main__":
    start()