import tkinter as tk

def enviar(event=None):  # o event=None é importante pro Enter funcionar
    valor = entrada.get()
    texto.config(text=f"Você digitou: {valor}")
    entrada.delete(0, tk.END)

# janela
janela = tk.Tk()
janela.geometry("300x200")

texto = tk.Label(janela, text="Digite algo:")
texto.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack(pady=10)

# 🔥 aqui acontece a mágica (Enter do teclado)
janela.bind("<Return>", enviar)

janela.mainloop()