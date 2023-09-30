import os
from time import sleep

userInfo = []




def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpa_tela()
    print("MENU".center(50))
    opcao = int(input("\n1 - Cadastrar usuário \n2 - Procurar usuário \n3 - Deletar Usuarios \n4 - Fechar o programa \n"))
    return opcao
  
def calcular_M(salario):
  # M será o intermediario entre o salario e o Imposto
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

def cadastrar():
    limpa_tela()
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    cpf = str(input("Digite o CPF do usuário: "))
    numero = input("Digite número de telefone do usuário: ")
    salario = float(input("Digite seu salario:"))  
    IRF = calcular_M(salario)
    
    
    verificar = True
    criarUser(nome, idade, cpf, numero, verificar, salario, IRF)
    input("\nUsuário Criado. Aperte ENTER para voltar ao menu.")

def criarUser(nome, idade, cpf, numero, verificar, salario, IRF):
    user = [nome, idade, cpf, numero, verificar, salario, IRF]
    userInfo.append(user)

def procurarNome(nome):
    for user in userInfo:
      if user[0].lower() == nome.lower() and user[4] == True:
         print("\nUsuário encontrado: \nNome:", user[0], "\nIdade:", user[1], "\nCPF:", user[2], "\nNúmero:", user[3], "\nsalario:", user[5], "\nIRF:", user[6])
      if user[4] == False:
        print("\nUsuário não existe")
      return
    

def procurarCpf(cpf):
    for user in userInfo:
      if user[1].lower() == cpf.lower() and user[4] == True:
         print("\nUsuário encontrado: \nNome:", user[0], "\nIdade:", user[1], "\nCPF:", user[2], "\nNúmero:", user[3]), , "\nsalario:", user[5], "\nIRF:", user[6])            
      if user[4] == False:
        print("\nUsuário não existe")
      return
def procurar():
    limpa_tela()
    opcao2 = int(input("Deseja procurar por nome [Digite 1] \nCPF [Digite 2] \n"))
    match(opcao2):
        case 1:
            nome = input("Digite o nome: ")
            procurarNome(nome)
            input("\nAperte ENTER para voltar ao menu.")
        case 2:
            cpf = input("Digite o CPF: ")
            procurarCpf(cpf)
            input("\nAperte ENTER para voltar ao menu.")

def apagarUserNome():      
      nome = input("Qual o nome do usuário deseja deletar?")
      for user in userInfo:
        if user[0].lower() == nome.lower() and  user[4] == True:
          print("\nUsuário deletado do sistema")
          sleep(1.5)
          user[4] = False
      return
if __name__ == "__main__":
  
    while True:
        opcao = menu()

        match opcao:
            case 1:
                cadastrar()
            case 2:
                procurar()
            case 3:
                apagarUserNome()
            case 4:
                print("\n Fim do Programa...")
                break

    print("\n\n\nBy NextCode")
  
