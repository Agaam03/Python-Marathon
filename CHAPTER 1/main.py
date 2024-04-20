import random

welcome_message = "WELCOME TO TAWAMURE GAMES!"
nomor_tupai = random.randint(1,4)

print("*******************************")
print(f"** {welcome_message} **")
print("*******************************")

nama_user = input("Masukan nama anda : ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini
|_| |_| |_| |_|
 1   2   3   4
      ''')

user_input = int(input("Menurut kamu di goa nomer berapa tupai berada? "))

confirm_user = input(f"Apakah kamu yakin memilih no {user_input} ? [y/n] ")

if confirm_user == "n":
    user_input = int(input("Menurut kamu di goa nomer berapa tupai berada? "))

print(f"Pilihan kamu adalah nomor {user_input}")

if user_input == nomor_tupai:
    print(f"Yah benar tupai berada di goa nomor {nomor_tupai}")
elif user_input > 4:
    print(f"Broo gua hanya ada 4")
else:
    print(f"Salah tupai! bukan goa nomor {user_input} tapi tupai berada di goa nomor {nomor_tupai}")






