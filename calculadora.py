import tkinter as tk

# ---------------- FUNÇÕES ---------------- #

def clicar(valor):
    visor.insert(tk.END, valor)

def limpar():
    visor.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# ---------------- JANELA ---------------- #

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("360x600")
janela.config(bg="#0f172a")
janela.resizable(False, False)

# ---------------- VISOR ---------------- #

visor = tk.Entry(
    janela,
    font=("Segoe UI", 30, "bold"),
    bg="#111827",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)

visor.pack(
    fill="both",
    padx=20,
    pady=25,
    ipady=25
)

# ---------------- FRAME ---------------- #

frame = tk.Frame(janela, bg="#0f172a")
frame.pack(expand=True, fill="both", padx=15, pady=10)

# ---------------- BOTÕES ---------------- #

botoes = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=",]
]

cores = {
    "numero": "#1e293b",
    "operador": "#334155",
    "igual": "#22c55e",
    "limpar": "#ef4444"
}

for linha in botoes:

    linha_frame = tk.Frame(frame, bg="#0f172a")
    linha_frame.pack(expand=True, fill="both", pady=5)

    for botao in linha:

        # Escolhe a cor
        if botao == "=":
            cor = cores["igual"]
        elif botao == "C":
            cor = cores["limpar"]
        elif botao in ["+", "-", "/", "×", "(", ")"]:
            cor = cores["operador"]
        else:
            cor = cores["numero"]

        # Define comando
        if botao == "=":
            comando = calcular

        elif botao == "C":
            comando = limpar

        else:
            comando = lambda x=botao.replace("×", "*"): clicar(x)

        # Botão
        b = tk.Button(
            linha_frame,
            text=botao,
            font=("Segoe UI", 18, "bold"),
            bg=cor,
            fg="white",
            activebackground=cor,
            activeforeground="white",
            bd=0,
            relief="flat",
            command=comando,
            cursor="hand2"
        )

        b.pack(
            side="left",
            expand=True,
            fill="both",
            padx=6,
            pady=6,
            ipady=18
        )

# ---------------- LOOP ---------------- #

janela.mainloop()