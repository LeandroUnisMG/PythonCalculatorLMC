import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)

        if imc < 18.5:
            resultado = f"IMC: {imc:.2f} - Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado = f"IMC: {imc:.2f} - Peso normal"
        elif 25 <= imc < 29.9:
            resultado = f"IMC: {imc:.2f} - Sobrepeso"
        else:
            resultado = f"IMC: {imc:.2f} - Obesidade"

        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="Resultado")

def sair():
    root.destroy()

root = tk.Tk()
root.title("Cálculo do IMC - Índice de Massa Corporal")

tk.Label(root, text="Nome do Paciente:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Endereço Completo:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_endereco = tk.Entry(root, width=40)
entry_endereco.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Altura (cm):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_altura = tk.Entry(root, width=10)
entry_altura.grid(row=2, column=1, padx=5, pady=5, sticky="w")

tk.Label(root, text="Peso (Kg):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_peso = tk.Entry(root, width=10)
entry_peso.grid(row=3, column=1, padx=5, pady=5, sticky="w")

label_resultado = tk.Label(root, text="Resultado", bg="white", width=30, height=5, relief="sunken", anchor="center")
label_resultado.grid(row=2, column=2, rowspan=2, padx=10, pady=5)

tk.Button(root, text="Calcular", command=calcular_imc).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Reiniciar", command=reiniciar).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Sair", command=sair).grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
