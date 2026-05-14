"""
Calculadora de IMC com Interface Gráfica (Tkinter)
Projeto nível iniciante/estudante.
Funcionalidades:
- Entrada de peso (kg) e altura (m)
- Cálculo do IMC = peso / altura²
- Classificação da OMS
- Validação de entradas
- Exibição imediata do resultado
"""

import tkinter as tk
from tkinter import messagebox

def classificar_imc(imc):
    """Retorna a classificação do IMC conforme tabela da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"

def calcular_imc():
    """Lê os valores, calcula o IMC e exibe o resultado."""
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        if peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Peso e altura devem ser maiores que zero.")
            return
        
        imc = peso / (altura ** 2)
        classificacao = classificar_imc(imc)
        
        resultado_var.set(f"IMC = {imc:.2f} - {classificacao}")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos (use ponto para decimais).")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("400x300")
janela.resizable(False, False)

# Rótulos e campos de entrada
tk.Label(janela, text="Calculadora de IMC", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(janela, text="Peso (kg):").pack(anchor="w", padx=20)
entry_peso = tk.Entry(janela, width=20)
entry_peso.pack(padx=20, pady=5, fill="x")

tk.Label(janela, text="Altura (m):").pack(anchor="w", padx=20)
entry_altura = tk.Entry(janela, width=20)
entry_altura.pack(padx=20, pady=5, fill="x")

# Botão calcular
btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc, bg="#4CAF50", fg="white")
btn_calcular.pack(pady=20)

# Variável para armazenar o resultado
resultado_var = tk.StringVar()
resultado_var.set("Aguardando dados...")
tk.Label(janela, textvariable=resultado_var, font=("Arial", 12), fg="blue", wraplength=350).pack(pady=20)

# Rodapé informativo
tk.Label(janela, text="Baseado na tabela da OMS", font=("Arial", 8), fg="gray").pack(side="bottom", pady=5)

# Iniciar o loop da interface
janela.mainloop()
