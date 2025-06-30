import random
import os
import sys
import time 
import webbrowser

def sortear():
    opcao = 6
    numSorteado=random.randint(1,opcao)
    #print("o numero sorteado e:",numSorteado )

    try:
        escolha=int(input(f"escolha um numero entre 1 e {opcao}:"))
        if escolha <1 or escolha > opcao:
         raise ValueError("numere fora de intervalo")
    except ValueError as e: 
       print(f" entrada invalida: {e} tente de novo! ")
       sortear()
    if escolha==numSorteado:
       print( "byabya WORD,seu pc ira de vasco")
       time.sleep
       if sys.platform == "win32":
          os.system("shutdown")
        elif sys.platform == 'linox' or sys.platform == 'linox2':
          os.system("shutdown now")
        elif sys.platform == "darwin":
          os.system("shutdown -h now") 


    else:
       print("voce etas seguro,por enquanto")  
sortear()

