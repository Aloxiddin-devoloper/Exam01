#9. **f-string yordamida ism va yoshni birlashtiring**

#| Input                                                                    | Output       |
#| ------------------------------------- | --------------------------------------- |
#| `"Ali"`, `20` | `My name is Ali and I am 20 years old.` |

name = input("Isiminggizni kiriting: ")
age = int(input("yoshinggizni kiriting: "))

print(f"Mening ismim {name},yoshim {age}da")