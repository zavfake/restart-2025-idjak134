import random

keepRestart = True
while keepRestart:
    systemNumber = random.randint(1,10)
    print(f"contekan nih bos: {systemNumber}")
    guessNumber = input("Tebak angka lo (1-10)...")

    if(systemNumber == int(guessNumber)):
        print("You are win bro!")
        keepRestart = False
    else:
        print("Ulangi lagi deh, salah nih")