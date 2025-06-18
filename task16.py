#16. **Yoshga bog'liq chegirma**

#**Vazifa:** 
#Chipta narxi 100 so'm. Foydalanuvchidan yoshini so'rang va chegirmani qo'llang:
#- 7 yoshgacha (0-6): 50% chegirma
#- 7-17 yosh: 20% chegirma  
#- 60 yoshdan katta: 30% chegirma

prace = 100
age = int(input("yoshinggizni kiriting: "))

if 0 < age <= 6:
    print(prace*1/2)
if 6 < age <= 17:
    print(prace*0.2)
if 60 < age:
    print(prace*0.7)