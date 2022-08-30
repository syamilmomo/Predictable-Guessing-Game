#introduction

import random
print("1. zink")
print("2. magnesium")
print("3. kalium")
print("4. natrium")
print("5. aurum")  
print("6. argentum")
print("7. aluminium")

#define main()function

def main():
    """Mulakan teka unsur."""
    print("mari teka unsur!")

    logam = [
        "zink",
        "magnesium",
        "kalium",
        "natrium",
        "aurum",
        "argentum",
        "aluminium"
        ]
#generate random choice    
    
        
    x = random.choice(logam)
    guess = None

    while x != guess:
        guess = str(input("Masukkan unsur:  "))
        if x == guess:
                print("You guessed {}. TAHNIAH ANDA BENAR!".format(guess))
        elif x == "zink":
            print(" MAAF ANDA SALAH.SILA CUBA LAGI! berwarna kelabu kebiru-biruan dan bersifat sederhana reaktif")
        elif x == "magnesium":
            print(" MAAF ANDA SALAH.SILA CUBA LAGI!unsur kimia di dalam jadual berkala yang mempunyai simbol Mg")
        elif x == "kalium":
            print(" MAAF ANDA SALAH.SILA CUBA LAGI! unsur kimia dalam jadual berkala. Ia mempunyai simbol K")
        elif x == "natrium":
            print(" MAAF ANDA SALAH.SILA CUBA LAGI! unsur kimia dalam jadual berkala yang mempunyai simbol Na")
        elif x == "aurum":
            print(" MAAF ANDA SALAH.SILA CUBA LAGI! unsur kimia dalam jadual berkala yang mempunyai simbol Au dan nombor atom 79")
        elif x =="argentum":
            print(" MAAF ANDA SALAH.SILA CUBA LAGI!sejenis logam kimia keunsuran yang mempunyai simbol Ag dan nombor atom 47. Perak berwarna putih berkilau dan adalah sejenis logam peralihan.")
        elif x == "aluminium":
            print(" MAAF ANDA SALAH.SILA CUBA LAGI!unsur kimia dalam jadual berkala yang mempunyai simbol Al dan nombor atom 13. Ia merupakan ahli kumpulan dalam unsur kimia yang bernama logam lemah dan mempunyai ciri keperakan dan mulur. ")
            
        elif x != guess:
                print("You guessed {}. MAAF ANDA SALAH.SILA CUBA LAGI!".format(guess))


main()
