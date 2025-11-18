# Tanpa for untuk mencetak angka 1 - n
print("angka 1")
print("angka 2")
print("angka 3")
print("angka 4")
print("angka 5")

print("====")
# Refacoring kode diatas menggunakan loop for
for x in range(1,6):
    print(f"angka {x}")
    
print("==range variation==")
myList = list(range(6))
print(myList)
myList = list(range(1,6))
print(myList)
myList = list(range(1,6,2))
print(myList)

for i, z in enumerate(myList):
    print(f"Nilai my list idex ke {i} adalah {z}")
    
# study case
namaSiswa = ["Prithvi", "Ginda", "Abdul", "Christoper"]
for nm in namaSiswa:
    print(f"{nm} Hadir")
    
listNumbers = [1, 2, 4, 100]
tempSum = 0
for ln in listNumbers:
    tempSum = tempSum + ln
    
print(tempSum)