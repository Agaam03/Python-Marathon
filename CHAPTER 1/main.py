import random

welcome_message = "WELCOME TO TAWAMURE GAMES!"
nomor_tupai = random.randint(1,4)

print("*******************************")
print(f"** {welcome_message} **")
print("*******************************")

nama_user = input("Masukan nama anda : ")

goa = ["|__|"] * 4
goa_kosong = goa

goa_tupai = goa_kosong.copy()
goa_tupai[nomor_tupai - 1] = "|0_0|"

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini
{" ".join(goa_kosong)}
      ''')

user_input = int(input("Menurut kamu di goa nomer berapa tupai berada? "))

confirm_user = input(f"Apakah kamu yakin memilih no {user_input} ? [y/n]")

if confirm_user == "n":
    print("Program berhenti!!!")
    exit()
elif confirm_user == "y":
    print(f"Pilihan kamu adalah nomor {user_input} \n")
    if user_input == nomor_tupai:
        print(" ".join(goa_tupai)) 
        print(f"Yah benar tupai berada di goa nomor {nomor_tupai} \n")
    elif user_input > 4:
        print(f"Broo goa hanya ada 4")
    else:
        print(" ".join(goa_tupai))
        print(f"Salah tupai! bukan goa nomor {user_input} tapi tupai berada di goa nomor {nomor_tupai} \n")
else:
    print("Silakan Ulang program")
    exit()
    








