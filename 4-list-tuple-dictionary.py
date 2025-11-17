# List, Tuple, and dictionary are composite data type
# List
# Sebuah tipe data yang bisa menyimpan banyak nilai. Bersifat mutable
myList = ["Jeruk", "Anggur", "Apel", 50000]
print(type(myList))
print(myList)
print(myList[1])
myList[0] = "Jeruk Bali" # Reaassignment, overriding
print(myList)

# Tuple
# Data type yang mirip dengan list, namun bersifat immutable (tidak bisa di rubah)
myTuple = ("Jeruk Mandarin", "Anggur", "Apel", 50000)
print(type(myTuple))
print(myTuple)
print(myTuple[1])
# myTuple[0] = "Jeruk Bali" # Reaassignment, overriding. Error! Cannot assign new value for myTuple
# print(myTuple)


# Dictionary
# Sama seperti list, namun indeks (key) dapat dicustom. Sama seperti list, bersifat mutable
import json
myDictionary = {
    "buah1": "Jeruk",
    "buah2": "Anggur",
    "buah3": "Apel",
    "harga": 50000
}

print(type(myDictionary))
print(myDictionary)
print(myDictionary["buah2"])
myDictionary["buah1"] = "Jeruk Bali" # Can reassign new value to myDictionary
print(myDictionary)

# print biar rapi
print(json.dumps(myDictionary, indent=4))


#####################
## CHALLENGE TIME! ##
#####################

# 1. Misalkan saya punya list myPorgrammingLang = ["Python", "Shell", "Javascript", "PHP", "Golang", "C++"].
# Bagaimana cara memanggil golang dan C++ hanya dengan menggunakan satu pasang square bracket.

# # 2. Misalkan saya punya complex nested dictionary:
# myComplexDict = {
#     "name": "zauvik rizaldi",
#     "alamat":{
#         "provinsi": "Jawa tengah",
#         "kecamatan": "Laweyan",
#         "desa": "Peramban Indah",
#         "RT": "01",
#         "RW": "02"
#     },
#     "siblings":["azizah", "anisa", "pramudita"]
# }

# Bagaimana cara untuk memunculkan: 
#     Nama zauvik rizaldi, alamat: Laweyan, Peramban Indah RT 01, RW 02. Saudara: azizah, anisa, pramudita

# ANSWER
myPorgrammingLang = ["Python", "Shell", "Javascript", "PHP", "Golang", "C++"]

# cara 1. Start:Stop index
print(myPorgrammingLang[2:4])

# cara 2. Strat: index
print(myPorgrammingLang[4:])

# cara 3. Negative index
print(myPorgrammingLang[-2:])