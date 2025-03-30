import tkinter as tk  # ייבוא ספריית Tkinter ליצירת ממשקים גרפיים


# פונקציה לחישוב המשולש
def calcular_triplo():
    try:
        numero = int(entrada.get())  # קבלת הערך מהמשתמש
        resultado = numero * 3       # חישוב המשולש של המספר
        label_resultado.config(text=f"O triplo de {numero} é {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido.")


# פונקציה למרכז את החלון
def centralizar_janela(janela, largura=400, altura=200):
    largura_tela = janela.winfo_screenwidth()  # רוחב המסך
    altura_tela = janela.winfo_screenheight()  # גובה המסך
    x = (largura_tela - largura) // 2          # חישוב מיקום אופקי
    y = (altura_tela - altura) // 2            # חישוב מיקום אנכי
    janela.geometry(f"{largura}x{altura}+{x}+{y}")  # הגדרת גודל ומיקום החלון


# יצירת החלון הראשי
janela = tk.Tk()
janela.title("Calculadora de Triplo")  # כותרת החלון
centralizar_janela(janela)             # קריאה לפונקציה שמרכזת את החלון

# הגדרת צבע רקע (שחור מט)
janela.configure(bg="#121212")

# תווית הוראות
label_instrucao = tk.Label(
    janela,
    text="Digite um número:",
    font=("Arial", 12),
    fg="#00FFFF",
    bg="#121212"
)
label_instrucao.pack(pady=5)

# שדה קלט (שחור הופך ללבן)
entrada = tk.Entry(
    janela,
    font=("Arial", 14),
    fg="#00FFFF",
    bg="#FFFFFF",
    insertbackground="#00FFFF"
)
entrada.pack(pady=10)

# כפתור לחישוב
botao_calcular = tk.Button(
    janela,
    text="Calcular",
    command=calcular_triplo,
    fg="#00FFFF",
    bg="#1A1A1A",
    activebackground="#00FF00",
    activeforeground="#121212",
    relief="raised",
    bd=3
)
botao_calcular.pack(pady=10)

# תווית להצגת התוצאה
label_resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 14),
    fg="#00FFFF",
    bg="#121212"
)
label_resultado.pack(pady=10)

# הפעלת הממשק הגרפי (לולאת עיקרית)
janela.mainloop()
