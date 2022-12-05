
# nama = input("Nama Kamu ?")
# if nama == "and" : print("Boleh lah")

# umur = int(input("Masukkan Umur : \t"))
# if umur > 25 :
#     print("lu udah tua")
#     print("pasti ngangguran")
# else :
#     print("gk pp")

# print("Diluar kontex")

# if umur < 15 :
#     print("lu masih bocil")
# elif umur >= 15 and umur <= 19 :
#     print("lu masih labil")
# elif umur > 19 and umur <= 25 :
#     print("Lu udah dewa tolol")
# elif umur > 35 :
#     print("lu udah tua bang")
#     if umur == 37 :
#         print("nikah goblok")
#     elif umur == 40 :
#         print("masih susah ? mati aja sana")
# else :
#     print("serah goblok")

# Kalkulator

angka1 = int(input("Masukkan angka 1 : "))
operator = input("Masukkan Operator ")
angka2 = int(input("Masukkan angka 2 : "))

if operator == "+" :
    angka1 += angka2
elif operator == "-" :
    angka1 -= angka2
elif operator == "*" :
    angka1 *= angka2
elif operator == "/" :
    angka1 /= angka2

print(f"Hasil : {angka1}")