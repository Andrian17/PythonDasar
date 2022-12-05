
# mode write
with open('./16_RW_File/text.txt', mode="w", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("Andrianpooooooooooo OKOKOKo")

# mode (a) append ==> menambahkan text diakhir
with open('./16_RW_File/text.txt', mode="a", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("\nsaya adalah naruto dari konoha, teman saya sasuke dan Shikamaru, chiji genndut")

# menimpa hanya pada baris tertentu
with open('./16_RW_File/text.txt', mode="r+", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("\nsaya adalah naruto dari konoha, teman saya sasuke dan Shikamaru, chiji genndut")

with open('./16_RW_File/text.txt', mode="r+", encoding="utf-8") as fileWrite :
    # overwirite / menimpa text sebeumnya
    fileWrite.write("\ns fk perduli gwdut")
