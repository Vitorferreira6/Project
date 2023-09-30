import tkinter as tk
from tkinter import messagebox

# Função de coleta de dados:
def Coletar_Dados():
    idade = idade_entry.get()
    peso = peso_entry.get()
    altura = altura_entry.get()

    try:
        idade = int(idade)
        peso = float(peso)
        altura = float(altura)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")
        return

    biotipo = Identificar_Biotipo(peso, altura)
    Treino_Para_Biotipo(biotipo)

def Identificar_Biotipo(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        return "Ectomorfo"
    elif imc < 25:
        return "Mesomorfo"
    else:
        return "Endomorfo"

def Treino_Para_Biotipo(biotipo):
    if biotipo == "Ectomorfo":
        recomendacao = """
        Treino para Ectomorfo:
        - Treinamento com peso
        - Consumir mais calorias.
        - Evitar excesso de exercícios aeróbicos.
        """
    elif biotipo == "Mesomorfo":
        recomendacao = """
        Treino para Mesomorfo:
        - Treino de força e aeróbico.
        - Dieta equilibrada.
        - Calorias equilibradas.
        """
    elif biotipo == "Endomorfo":
        recomendacao = """
        Treino para Endomorfo:
        - Foco em exercícios aeróbicos para perda de gordura.
        - Controlar ingestão calórica.
        - Treino de força para construção muscular.
        """

    resultado_label.config(text=recomendacao)

app = tk.Tk()
app.title("Identificador de Biotipo")

label_idade = tk.Label(app, text="Idade:")
label_idade.pack(pady=10)
idade_entry = tk.Entry(app)
idade_entry.pack(pady=10)

label_peso = tk.Label(app, text="Peso (kg):")
label_peso.pack(pady=10)
peso_entry = tk.Entry(app)
peso_entry.pack(pady=10)

label_altura = tk.Label(app, text="Altura (m):")
label_altura.pack(pady=10)
altura_entry = tk.Entry(app)
altura_entry.pack(pady=10)

btn_submit = tk.Button(app, text="Identificar Biotipo", command=Coletar_Dados)
btn_submit.pack(pady=20)

resultado_label = tk.Label(app, text="")
resultado_label.pack(pady=20)

app.mainloop()
