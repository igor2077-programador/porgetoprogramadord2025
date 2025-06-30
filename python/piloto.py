print("ola mundo")

#ntrada de dados
nota1 = float(input("insira a primeira nota:"))
nota2 = float(input("insira a segunda nota:"))
nota3 = float(input("insira a tersceira nota:"))
nota4 = float(input("insira a quarta nota:"))

#processamento dos dados
notafinal = (nota1 + nota2 + nota3 + nota4) /4

#saida 
print("A NOTA FINAL E:" , notafinal)

if notafinal <60:
    print("oluno esta reprovado!")
elif(notafinal <70):
    print("o resutadao foi mediaano")
elif (notafinal <80):
    print( "resutado foi bom")
elif(notafinal <90):
    print ("resutado foi excelente" )
elif(notafinal <101):
    print("voce vai para Harvard :)")
        