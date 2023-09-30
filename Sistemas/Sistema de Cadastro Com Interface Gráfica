import tkinter as tk
from tkinter import messagebox

def login():
    senha_digitada = senha_entry.get()
    if senha_digitada == "123":
        root.deiconify()  # Exibir a janela principal após a autenticação bem-sucedida
        senha_entry.delete(0, tk.END)  # Limpar o campo de senha
        login_window.withdraw()  # Ocultar a janela de login
    else:
        messagebox.showerror("Erro", "Senha incorreta!")

def sair():
    root.quit()

def cadastrar():
    nome = nome_entry.get()
    idade = idade_entry.get()
    cpf = cpf_entry.get()
    numero = numero_entry.get()
    salario = salario_entry.get()
    IRF = calcular_M(float(salario))
    
    verificar = True
    criarUser(nome, idade, cpf, numero, verificar, salario, IRF)
    resultado_label.config(text="Usuário Criado.")
    nome_entry.delete(0, tk.END)
    idade_entry.delete(0, tk.END)
    cpf_entry.delete(0, tk.END)
    numero_entry.delete(0, tk.END)
    salario_entry.delete(0, tk.END)

def criarUser(nome, idade, cpf, numero, verificar, salario, IRF):
    user = [nome, idade, cpf, numero, verificar, salario, IRF]
    userInfo.append(user)

def procurarNome():
    nome_procurar = nome_procurar_entry.get()
    resultado_text.delete(1.0, tk.END)
    
    for user in userInfo:
        if user[0].lower() == nome_procurar.lower() and user[4] == True:
            resultado_text.insert(tk.END, f"Nome: {user[0]}\nIdade: {user[1]}\nCPF: {user[2]}\nNúmero: {user[3]}\nSalário: {user[5]}\nIRF: {user[6]}\n\n")
            return
    
    resultado_text.insert(tk.END, "Usuário não encontrado.\n")

def apagarUserNome():
    nome_apagar = nome_apagar_entry.get()
    
    for user in userInfo:
        if user[0].lower() == nome_apagar.lower() and user[4] == True:
            user[4] = False
            resultado_label.config(text="Usuário deletado do sistema")
            return
    
    resultado_label.config(text="Usuário não encontrado.")
    

def calcular_M(salario):
    if salario <= 1983.98:
         M = 0
    elif salario <= 2836.65:
         M = salario * 0.075
    elif salario <= 3751.05:
        M = salario * 0.15
    elif salario <= 4664.68:
        M = salario * 0.225
    else:
        M = salario * 0.275
    return M

# Janela de autenticação
login_window = tk.Tk()
login_window.title("Autenticação")
login_window.geometry("300x100")

senha_label = tk.Label(login_window, text="Senha:")
senha_label.pack()

senha_entry = tk.Entry(login_window, show="*")
senha_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

# Janela principal
root = tk.Tk()
root.title("Sistema de Cadastro")
root.geometry("400x400")
root.withdraw()  # Inicialmente, a janela principal é ocultada

frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True)

frame2 = tk.Frame(root)
frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(root)
frame3.pack(fill="both", expand=True)

frame4 = tk.Frame(root)
frame4.pack(fill="both", expand=True)

frame5 = tk.Frame(root)
frame5.pack(fill="both", expand=True)

frame6 = tk.Frame(root)
frame6.pack(fill="both", expand=True)

frame7 = tk.Frame(root)
frame7.pack(fill="both", expand=True)

label1 = tk.Label(frame1, text="Nome:")
label1.pack(side=tk.LEFT)
nome_entry = tk.Entry(frame1)
nome_entry.pack(side=tk.LEFT)

label2 = tk.Label(frame2, text="Idade:")
label2.pack(side=tk.LEFT)
idade_entry = tk.Entry(frame2)
idade_entry.pack(side=tk.LEFT)

label3 = tk.Label(frame3, text="CPF:")
label3.pack(side=tk.LEFT)
cpf_entry = tk.Entry(frame3)
cpf_entry.pack(side=tk.LEFT)

label4 = tk.Label(frame4, text="Número:")
label4.pack(side=tk.LEFT)
numero_entry = tk.Entry(frame4)
numero_entry.pack(side=tk.LEFT)

label5 = tk.Label(frame5, text="Salário:")
label5.pack(side=tk.LEFT)
salario_entry = tk.Entry(frame5)
salario_entry.pack(side=tk.LEFT)

cadastrar_button = tk.Button(frame6, text="Cadastrar", command=cadastrar)
cadastrar_button.pack(side=tk.LEFT)

label6 = tk.Label(frame7, text="Resultado:")
label6.pack(side=tk.LEFT)
resultado_label = tk.Label(frame7, text="", wraplength=200)
resultado_label.pack(side=tk.LEFT)

frame8 = tk.Frame(root)
frame8.pack(fill="both", expand=True)

label7 = tk.Label(frame8, text="Procurar por nome:")
label7.pack(side=tk.LEFT)
nome_procurar_entry = tk.Entry(frame8)
nome_procurar_entry.pack(side=tk.LEFT)

procurar_button = tk.Button(frame8, text="Procurar", command=procurarNome)
procurar_button.pack(side=tk.LEFT)

frame9 = tk.Frame(root)
frame9.pack(fill="both", expand=True)

label8 = tk.Label(frame9, text="Resultado da pesquisa:")
label8.pack(side=tk.LEFT)
resultado_text = tk.Text(frame9, width=40, height=10)
resultado_text.pack(side=tk.LEFT)

frame10 = tk.Frame(root)
frame10.pack(fill="both", expand=True)

label9 = tk.Label(frame10, text="Apagar usuário por nome:")
label9.pack(side=tk.LEFT)
nome_apagar_entry = tk.Entry(frame10)
nome_apagar_entry.pack(side=tk.LEFT)

apagar_button = tk.Button(frame10, text="Apagar", command=apagarUserNome)
apagar_button.pack(side=tk.LEFT)

root.mainloop()
