#14. **Document type aniqlash**

#Fayl nomi `.pdf`, `.docx`, yoki `.txt` bilan tugashini tekshiring

#| Input          | Output  |
#| -------------- | ------- |
#| `"report.pdf"` | `True`  |
#| `"photo.jpeg"` | `False` |

document = input("Fayl nomini kiriting: ")

if document.endswith(".txt") or document.endswith(".docx") or document.endswith(".pdf"):
    print(True)
else:
    print(False)