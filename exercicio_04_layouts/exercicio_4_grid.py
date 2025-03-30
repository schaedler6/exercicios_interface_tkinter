import tkinter as tk


def enviar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    genero = var_genero.get()

    print("=== Dados do Formulário (grid) ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Gênero: {genero}")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    var_genero.set(None)

# Janela principal
root = tk.Tk()
root.title("Exercício 4 - Grid")

# Nome
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=0, column=1, pady=5)

# Idade
tk.Label(root, text="Idade:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_idade = tk.Entry(root, width=30)
entry_idade.grid(row=1, column=1, pady=5)

# Gênero
tk.Label(root, text="Gênero:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
var_genero = tk.StringVar()
tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").grid(row=2, column=1, sticky='w')
tk.Radiobutton(root, text="Feminino", variable=var_genero, value="Feminino").grid(row=3, column=1, sticky='w')

# Botões
tk.Button(root, text="Enviar", command=enviar_dados).grid(row=4, column=0, pady=15)
tk.Button(root, text="Limpar", command=limpar_campos).grid(row=4, column=1)

# Preenchimento de exemplo (dados fictícios)
entry_nome.insert(0, "Moisés Ben Levi")
entry_idade.insert(0, "45")
var_genero.set("Masculino")

# Executar
root.mainloop()
