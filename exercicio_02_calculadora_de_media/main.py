import tkinter as tk  # ייבוא ספריית Tkinter ליצירת ממשקים גרפיים

# פונקציה לחישוב הממוצע
def calcular_media():
    try:
        numero1 = float(entrada1.get())  # קבלת הערך הראשון מהמשתמש
        numero2 = float(entrada2.get())  # קבלת הערך השני מהמשתמש
        media = (numero1 + numero2) / 2  # חישוב הממוצע
        label_resultado.config(text=f"A média de {numero1} e {numero2} é {media}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

# פונקציה לניקוי הנתונים
def limpar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    label_resultado.config(text="")

# פונקציה למרכז את החלון
def centralizar_janela(janela, largura=400, altura=300):
    largura_tela = janela.winfo_screenwidth()  # רוחב המסך
    altura_tela = janela.winfo_screenheight()  # גובה המסך
    x = (largura_tela - largura) // 2  # חישוב מיקום אופקי
    y = (altura_tela - altura) // 2    # חישוב מיקום אנכי
    janela.geometry(f"{largura}x{altura}+{x}+{y}")  # הגדרת גודל ומיקום החלון

# יצירת החלון הראשי
janela = tk.Tk()
janela.title("Calculadora de Média")  # כותרת החלון
centralizar_janela(janela)  # קריאה לפונקציה שמרכזת את החלון
janela.configure(bg="#121212")  # הגדרת צבע רקע שחור

# הוראות
label_instrucao = tk.Label(
    janela, 
    text="Digite dois números:", 
    font=("Arial", 12), 
    fg="#00FFFF", 
    bg="#121212"
)
label_instrucao.pack(pady=5)

# שדות קלט (הופך את השחור ללבן)
entrada1 = tk.Entry(janela, font=("Arial", 14), fg="#00FFFF", bg="#FFFFFF", insertbackground="#00FFFF")
entrada1.pack(pady=5)

entrada2 = tk.Entry(janela, font=("Arial", 14), fg="#00FFFF", bg="#FFFFFF", insertbackground="#00FFFF")
entrada2.pack(pady=5)

# כפתור לחישוב
botao_calcular = tk.Button(
    janela, 
    text="Calcular", 
    command=calcular_media, 
    fg="#00FFFF", 
    bg="#1A1A1A", 
    activebackground="#00FF00", 
    activeforeground="#121212", 
    relief="raised", 
    bd=3
)
botao_calcular.pack(pady=5)

# כפתור לניקוי הנתונים
botao_limpar = tk.Button(
    janela, 
    text="Limpar", 
    command=limpar, 
    fg="#00FFFF", 
    bg="#1A1A1A", 
    activebackground="#FF0000", 
    activeforeground="#FFFFFF", 
    relief="raised", 
    bd=3
)
botao_limpar.pack(pady=5)

# תווית להצגת התוצאה
label_resultado = tk.Label(janela, text="", font=("Arial", 14), fg="#00FFFF", bg="#121212")
label_resultado.pack(pady=10)

# לוגיקת הפעלה (קריאה להמשכת התוכנית הראשית)
janela.mainloop()
