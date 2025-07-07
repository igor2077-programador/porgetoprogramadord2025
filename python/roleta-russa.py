from ast import Lambda
import random
import os
import sys
import time 
import webbrowser
import tkinter as tk
from tkinter import messagebox 

def sortear():
   opcao = 6
   numSorteado=random.randint(1,opcao)


                     #print("o numero sorteado e:",numSorteado )
                     #try:
                     #escolha=int(input(f"escolha um numero entre 1 e {opcao}:"))
                     #if escolha <1 or escolha > opcao:
                     # raise ValueError("numere fora de intervalo")
                     #except ValueError as e: 
                     #print(f" entrada invalida: {e} tente de novo! ")
                     #sortear()

   def verificarescolha(escolha):
         if escolha==numSorteado:
            print( "byabya WORD,seu pc ira de vasco")
            time.sleep
            if sys.platform == "win32":
               os.system("shutdown /s /t 1")
         else:
            print("voce etas seguro,por enquanto")
   janela=tk.Toplevel()
   janela.title("roleta russa")
   tk.Label("escoçha um numero entre 1 e 6").pack(pady=10)

   for i in range(1,6):
      tk.Button(janela, text=str(i), command=lambda i=i: [janela.destroy(),verificarescolha(i)]).pack(pady=5)

root= tk.Tk()
root.title("roleta russa")   
tk.Label(root, text="Bem-vindo ao Jogo da roleta russa", font=("arial",14)).pack(pady=15)
tk.Button(root, text="iniciar jogo",width=20 , command=sortear).pack(pady=10)
tk.Button(root, text="regras",width=20 , command=sortear).pack(pady=10)
tk.Button(root, text="sair",width=20 , command=sortear).pack(pady=10)
root.mainloop()      
