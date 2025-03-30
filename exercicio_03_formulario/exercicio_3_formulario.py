import tkinter as tk


def exibir_dados():
    nome = entry_nome.get()
    email = entry_email.get()
    preferencia = var_preferencia.get()

    print("=== Dados do Formulário ===")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Preferência de contato: {preferencia}")

# Janela principal
root = tk.Tk()
root.title("Exercício 3 - Mini-Formulário")

# Campo: Nome
tk.Label(root, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(root, width=40)
entry_nome.pack()

# Campo: E-mail
tk.Label(root, text="E-mail:").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack()

# Campo: Preferência de Contato
tk.Label(root, text="Preferência de contato:").pack(pady=5)

var_preferencia = tk.StringVar()
var_preferencia.set("E-mail")  # valor padrão

tk.Radiobutton(root, text="E-mail", variable=var_preferencia, value="E-mail").pack()
tk.Radiobutton(root, text="Telefone", variable=var_preferencia, value="Telefone").pack()

# Botão: Exibir dados
tk.Button(root, text="Exibir dados no terminal", command=exibir_dados).pack(pady=15)

# Executa a janela
root.mainloop()
