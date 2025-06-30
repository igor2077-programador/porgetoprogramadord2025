alcool = float(input("insira o valor do alcool: "))
gasolina = float(input("insira o valor do gasolina: "))

resutado = alcool / gasolina

print(resutado)
 
if resutado > 0.7:
    print("abasteca com gasolina")
elif resutado < 0.7:
    print("abasteca com alcool")
else:
    print("siga seu coraçao")