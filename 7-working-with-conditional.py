# if(True):
#     print("I am always executed")

# if(False):
#     print("I am never executed")

# Dari experiment diatas, disimpulkan bawah kode di dalam conditional, 
# hanya akan dieksekusi jika parameter bernilai true

# print("=== If there are 2 conditon or less, you should use if - else")
# if(True):
#     print("Iam execucuted woy")
# else:
#     print("Iam the else woy")

# print("=== More than 2 conditions, you should use elif between if - else ====")
# if(False):
#     print("Never executed")
# elif(False):
#     print("Never executed")
# elif(True):
#     print("executed oe")
# elif(False):
#     print("Never executed")
# else:
#     print("Because all of the conditions above are false, I am executed")
    
    
# Logical comparison: Always return true or false, so we can passed this as parameter in conditional statement
# example of logical comparison: ==, <=, < , > , >=, !=
# print(8<5)
# print(8>5)
# print(10==10.5)
# print(10!=10.5)

# Di day to day as a programmer, we ussualy combine logical comparison with conditional statement
# myVar1 = 10
# myVar2 = input("Tebak nomor yang lebih besar dari sistem (0-20)...")
# if(int(myVar2) > myVar1):
#     print("Yey your number is greater than the system's number")
# elif(int(myVar2) == myVar1):
#     print("Oh, your number is equal with the system's number")
# else:
#     print("you number is lower than the system's number")
    
    
# Logical operator conjution/logical gate
# example: or, and
# True & True = True, True & False = False, False & True = False, False & False = False
# True | True = True, True | False = True, False | True = True, False | False = False

# print("Sebutkan nama cloud platform yang betul: a. AWS, b. GCP, c. Indihome")
# answer = input("Masukkan jawaban anda...")
# if(answer == "a" or answer == "b"):
#     print("Yey benar")
# else:
#     print("anda kurang tepat, silahkan coba kembali")

print("1. Sebutkan nama cloud platform yang betul: a. AWS, b. GCP, c. Indihome")
answer1 = input("Masukkan jawaban anda...")
answer1Result = False
if(answer1 == "a" or answer1 == "b"):
    print("Yey benar")
    answer1Result = True
    
print("2. Sebutkan nama provider internet: a. XL, b. Indosat, c. GCP")
answer2 = input("Masukkan jawaban anda...")
answer2Result = False
if(answer2 == "a" or answer2 == "b"):
    print("Yey benar")
    answer2Result = True

# Grading    
if(answer1Result and answer2Result):
    print("Nilai anda 100")
elif(answer1Result or answer2Result):
    print("Nilai anda 50")
else:
    print("Nilai 0")
