import os
os.system

print("""
Fruta \t Ate 5 kg \t Acima de 5 kg
 Morango \t 2,50 por kg \t R$ 2,20 por kg
 Maçã \t 1,80 por kg \t R$ 1,50 por kg     
""")
morangos = float(input("Kg de morangos: "))
macas = float(input("Kg de maçãs: "))

total = (morangos * 2.50) + (macas * 1.80)

if (morangos + macas >= 10) or (total >= 15): 
 desconto = valor_produto * 0.10

print("Valor a pagar: R$ 10% * 2f")