prog = ["PHP", "JS", "Dart", "Python"]

dataDiri = {
    "nama" : "Andrian",
    "nim" : 1901050024,
    "jurusan" : "D3 Sistem Informasi",
    "prog" : prog
}


# print(dataDiri.get("nama"))
# print(dataDiri.get("prog"))
# print(dataDiri.keys())
# print(dataDiri.values())
# print(dataDiri.items())

# Mengupdate key
dataDiri["nim"] = 2201010289
# print(dataDiri.get("nim"))
dataDiri.update({"nim" : "1919191919"})
# print(dataDiri.get("nim"))

# Menambah / Mengupdate
# dataDiri.update({"hobi" : "Gak Ada"})

# Menambah key
dataDiri["status"] = "Nganggur"
# print(dataDiri)

# Looping
# for saya in dataDiri :
#     print(f"{saya} : {dataDiri.get(saya)}")

# for value in dataDiri.values() :
#     print(f"value : {value}")
# for item in dataDiri.items() :
#     print(f"item : {item}")
# for key, value in dataDiri.items() :
#     print(f"key : {key} - value : {value}")

dataAnd = dataDiri.copy()
print(dataDiri)
print(dataAnd)
dataAnd.update({"nim" : "48343484834"})
print(dataAnd)
print(dataDiri)

# menghapus data berdasarkan key
dataAnd.pop("nama")
print(dataAnd)
# menghapus item terakhir
dataAnd.popitem()
print(dataAnd)