import tkinter as tk


def mostrar_mensagem1():
    print("Cliente: Shlomo Levi")

def mostrar_mensagem2():
    print("Endereço: Rua Theodor Herzl, Canoas - RS")

def mostrar_mensagem3():
    print("Contato: Eterno@historia.com / (51) 99888-5566")

# Janela principal
root = tk.Tk()
root.title("Exercício 4 - Layout com Place")
root.geometry("400x250")

# Rótulos
tk.Label(root, text="Informações", font=('Arial', 12, 'bold')).place(x=150, y=20)
tk.Label(root, text="Cliente:").place(x=30, y=70)
tk.Label(root, text="Endereço:").place(x=30, y=110)
tk.Label(root, text="Contato:").place(x=30, y=150)

# Botões
tk.Button(root, text="Mostrar Cliente", command=mostrar_mensagem1).place(x=200, y=65)
tk.Button(root, text="Mostrar Endereço", command=mostrar_mensagem2).place(x=200, y=105)
tk.Button(root, text="Mostrar Contato", command=mostrar_mensagem3).place(x=200, y=145)

root.mainloop()
