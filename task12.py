#12. **Matnda ma’lum bir so‘zning boshlanish pozitsiyasini topish**

#`Python` so‘zi qayerdan boshlanganini toping.

#| Input                                                       | Output |
#| ----------------------------------------------------------- | ------ |
#| `"Men Python dasturlash tilini o‘rganaman"`, `"Python"` | `4`    |

text = input("Matnni kiriting: ")
result = text.find("Python")

print(result)