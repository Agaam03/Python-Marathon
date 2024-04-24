import random
import main

def start():
    while True :
        nomor_tupai = random.randint(1,4)
        goa = ["|__|"] * 4
        goa_kosong = goa

        goa_tupai = goa_kosong.copy()
        goa_tupai[nomor_tupai - 1] = "|0_0|"

        # ----------------------
        goa_kosong = " ".join(goa_kosong)
        goa_tupai = " ".join(goa_tupai)
        # ----------------------

        print(f'Coba perhatikan goa dibawah ini \n\n {goa_kosong}')

        user_input = int(input("Menurut kamu di goa nomer berapa tupai berada? "))
        
        if user_input == nomor_tupai:
            print(goa_tupai) 
            print(f"Selamat Kamu Menang 🤩 [{nomor_tupai}] \n")
        elif user_input > 4:
            print(f"Broo goa hanya ada 4")
        else:
            print(f"\n{goa_tupai}\n")
            print(f"Wah Kamu masih kalah 😪 tupai berada di goa nomor [{nomor_tupai}] \n")
        
        play_again = input("Apakah ingin bermain lagi ? [y/n] ")
        if play_again == "n" and "N":
            main.menu()



if __name__ == '__main__':
    start()