#20. **To‘g‘ri javob kiritilmaguncha davom et**

#Dastur foydalanuvchidan “O‘zbekiston poytaxti nima?” deb so‘raydi.
#  “Toshkent” deb to‘g‘ri javob berguncha so‘rashda davom etadi.

def savol_ber(savol_matni):
    foydalanuvchi_javobi = input(f"{savol_matni} ").strip()
    return foydalanuvchi_javobi

def javobni_tekshir(foydalanuvchi_javobi, togri_javob):
    natija = foydalanuvchi_javobi.lower() == togri_javob.lower()
    return natija

def asosiy():
    savol_matni = "O'zbekiston poytaxti qayer?"
    togri_javob = "Toshkent"

    foydalanuvchi_javobi = savol_ber(savol_matni)
    javob_togri = javobni_tekshir(foydalanuvchi_javobi, togri_javob)

    if javob_togri:
        print("To'g'ri topdingiz.")
    else:
        print(f"Topolmadingiz, to'g'ri javob \"{togri_javob}\" edi.")

asosiy()
