# Challenge:
# 1. Panggil (load) file preproinsulin-seq.txt ke file python ini
# 2. Lakukan cleaning terhadap sisa spasi yang ada pada coding insulin
# 3. Konfirmasi bahwa coding insulin memilik panjang 110 karakter
# 4. Bagi coding insulin yang sudah bersih, kedalam beberapa file:
# - lsinsulin-seq-clean.txt. karakter ke 1–24
# - binsulin-seq-clean.txt. karakter ke 25-54
# - cinsulin-seq-clean.txt, karakter 55–89
# - cinsulin-seq-clean.txt, karakter 90–110

# simpan semua file di dalam folder result


import os
 
print("============TASK 1 : Menampilkan file .txt============ ")
 
with open("preproinsulin-seq.txt", "r") as file:
    isi_file = file.read()
    print(isi_file)
    print("")
 
    print("============TASK 2 : Menghapus spasi karakter ============ ")
 
    hapusSpasi = isi_file.replace(" ", "")
    print(hapusSpasi)
    print("")
 
    print("============TASK 3 : Menghitung jumlah karakter============ ")
    panjang = len(hapusSpasi)
    print(f"Panjang karakter : {panjang} ")
    print("")
   
    print("============TASK 4.1 : simpan karakter 1-24============ ")
    os.makedirs("result", exist_ok=True)
    print(hapusSpasi[:24])
    kata24 = hapusSpasi[:24]
    with open("result/lsinsulin-seq-clean.txt", "w") as file24:
        file24.write(kata24)
    print(f"Berhasil disimpan dan panjang karakter : {len(kata24)} ")
    print("")
 
    print("============TASK 4.2 : simpan karakter 25-54============ ")
    print(hapusSpasi[24:54])
    kata54 = hapusSpasi[24:54]
    with open("result/bsinsulin-seq-clean.txt", "w") as file54:
        file54.write(kata54)
    print(f"Berhasil disimpan dan panjang karakter : {len(kata54)} ")
    print("")
 
    print("============TASK 4.3 : simpan karakter 55-89============ ")
    print(hapusSpasi[54:89])
    kata89 = hapusSpasi[54:89]
    with open("result/cinsulin-seq-clean.txt", "w") as file89:
        file89.write(kata89)
    print(f"Berhasil disimpan dan panjang karakter : {len(kata89)} ")
    print("")
 
    print("============TASK 4.4 : simpan karakter 90-110============ ")
    print(hapusSpasi[89:110])
    kata110 = hapusSpasi[89:110]
    with open("result/ainsulin-seq-clean.txt", "w") as file110:
        file110.write(kata110)
    print(f"Berhasil disimpan dan panjang karakter : {len(kata110)} ")
 
 
 
# Refactored code for TASK 4: Using for
# os.makedirs("result", exist_ok=True)
# tasks = [
#     ("TASK 4.1", 0, 24, "lsinsulin-seq-clean.txt"),
#     ("TASK 4.2", 24, 54, "bsinsulin-seq-clean.txt"),
#     ("TASK 4.3", 54, 89, "cinsulin-seq-clean.txt"),
#     ("TASK 4.4", 89, 110, "ainsulin-seq-clean.txt")
# ]
 
# for name, start, end, filename in tasks:
#     print(f"============{name} : simpan karakter {start+1}-{end}============")
#     kata = hapusSpasi[start:end]
#     print(kata)
#     with open(f"result/{filename}", "w") as file:
#         file.write(kata)
#     print(f"Berhasil disimpan dan panjang karakter : {len(kata)} ")
#     print("")
 
 
   
 
   