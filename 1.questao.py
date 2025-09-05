import os 
os.system("cls")

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo numero: "))
terceiro_numero = float(input("Digite o terceiro numero: "))

soma = primeiro_numero + segundo_numero

if soma < terceiro_numero: 
  print("primeiro_numero + segundo_numero é menor que o terceiro_numero:")
else: soma < terceiro_numero
print("primeiro_numero + segundo_numero é maior que o terceiro_numero:")

print(f"Soma: {soma}")