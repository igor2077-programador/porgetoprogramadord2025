import random
import os
import sys
import time
import webbrowser
import tkinter as tk
from tkinter import messagebox


def sortear():
    opcao = 6
    numSorteado = random.randint(1, opcao)
 

    def verificarEscolha(escolha):
        if escolha == numSorteado:
            print("Bye Bye word, seu pc será desligado!👻 ")
            messagebox.showerror("Perdeu!", "O computador Será desligado! 👻")

            time.sleep(5)
            if sys.platform == "win32":
                os.system("shutdown /s /t 1")
            elif sys.platform == 'linux' or sys.platform == 'linux2':
                os.system("shutdown now")
            elif sys.platform == "dar32 win":
                os.system("shutdown -h now")

        else:
            print("Você está seguro, por enquanto! ")
            messagebox.showinfo("Ufa!","Você está seguro, por enquanto! 😊")
            sortear()
            

    janela = tk.Toplevel()
    janela.title("Algoritmo de sorteio")
    tk.Label(janela, text="Escolha um número entre 1 e 6").pack(pady=10)

    for i in range(1,7):
        tk.Button(janela, text=str(i), command=lambda i=i: [janela.destroy(),verificarEscolha(i)]).pack(pady=5)


def exibirRegras():
    regras = (
        "Regras do Jogo: \n"
        "1. Escolha um número entre 1 e 6. \n"
        "2. Se você escolher o nº sorteado, o PC será desligado! \n"
        "3. Se não for, o jogo continua. \n"
        "4. Boa sorte, vai precisar!"
    )
    messagebox.showinfo("Regras", regras)

def sair():
    root.destroy()

root = tk.Tk()
root.title("Jogo do evento aleatório")
tk.Label(root, text="Bem-vindo ao Jogo de Evento Aleatório!", font=("Arial", 20)).pack(pady=15)
tk.Button(root, text="Iniciar Jogo", width=20, command=sortear).pack(pady=10)
tk.Button(root, text="Ver regras", width=20, command=exibirRegras).pack(pady=10)
tk.Button(root, text="Sair", width=20, command=sair).pack(pady=10)
root.mainloop()
