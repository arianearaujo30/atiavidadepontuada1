import os
os.system("cls")

primeira_nota = float(input("Digite a primeira nota"))
segunda_nota = float(input("Digite a segunda nota"))

media = (primeira_nota + segunda_nota) / 2

if media >= 6: 
    print("Parabéns estar aprovado")
elif media >= 4.1 and media >= 5.9: 
    print("Recuperação")
else: 
    print("Reprovado")