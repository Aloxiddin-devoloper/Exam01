#17. **Baholash tizimi**

#**Vazifa:** Foydalanuvchidan ball (0-100) so'rang va bahoni chiqaring:
#- 90-100: "A (A'lo)"
#- 80-89: "B (Yaxshi)"  
#- 70-79: "C (Qoniqarli)"
# 60-69: "D (Qoniqarsiz)"
#- 0-59: "F (Rad)"

#Agar 0-100 oralig'idan tashqari son kiritilsa, `"Ball 0-100 oralig'ida bo'lishi kerak!"` deb chiqaring.


ball = int(input("Ballni kiriting (0-100): "))

if 90 <= ball <= 100:
    print("A (A'lo)")
elif 80 <= ball <= 89:
    print("B (Yaxshi)")
elif 70 <= ball <= 79:
    print("C (Qoniqarli)")
elif 60 <= ball <= 69:
    print("D (Qoniqarsiz)")
elif 0 <= ball <= 59:
    print("F (Rad)")
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")
