import tkinter as tk


def acao1():
    print("Ação 1 executada – Cliente: Efraim Cohen")

def acao2():
    print("Ação 2 executada – Telefone: (51) 99999-1122")

def acao3():
    print("Ação 3 executada – E-mail: Eterno@shalom.com")

# Janela principal
root = tk.Tk()
root.title("Exercício 4 - Layout com Pack")
root.geometry("300x200")

# Botões centralizados verticalmente
btn1 = tk.Button(root, text="Ação 1", width=20, command=acao1)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Ação 2", width=20, command=acao2)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Ação 3", width=20, command=acao3)
btn3.pack(pady=10)

# Inicia a interface
root.mainloop()
