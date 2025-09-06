import os
os.system("cls")

litros = float(input("Digite a quantidade de litros: "))
tipo = int(input("Digite o tipo de combustível (A-Álcool / G-Gasolina): "))

preco_alcool = 3.79
preco_gasolina = 6.59

if tipo == "A":
    preco = preco_alcool
if litros <= 25:
desconto = 0.10  
else:
    desconto = 0.20   

elif tipo == "G":
  preco = preco_gasolina
if litros <= 25:
     desconto = 0.15    
else:
    desconto = 0.30   

else:
    print("Tipo de combustível inválido!")
                                                                

                                                            
    total_sem_desc = litros * preco
   valor_desconto = total_sem_desconto * desconto
    total_pagar = total_sem_desc - valor_desconto

                                    
    print(f"\nTotal sem desconto: R$ {total_sem_desc}")
    print(f"Desconto: R$ {valor_desconto}")
    print(f"Total a pagar: R$ {total_pagar}")