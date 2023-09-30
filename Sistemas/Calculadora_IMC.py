import os


# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de coleta de dados:
def Coletar_Dados():
    limpar_tela()
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso em kg (ex: 65.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    input("\nDados Coletados!  Pressione Enter para continuar...")
    return idade, peso, altura

def Identificar_Biotipo(peso, altura):
    imc = peso / (altura**2)

    if imc < 18.5:
        return "Ectomorfo"
    if imc < 25:
        return "Mesomorfo"
    return "Endomorfo"

def Treino_Para_Biotipo(biotipo):
    limpar_tela()
    print(f"\nSeu biotipo é: {biotipo}\n")
    if biotipo == "Ectomorfo":
        print("""
        Treino para Ectomorfo:
        - Treinamento com peso
        - Consumir mais calorias.
        - Evitar excesso de exercícios aeróbicos.
        """)
    if biotipo == "Mesomorfo":
        print("""
        Treino para Mesomorfo:
        - Treino de força e aeróbico.
        - Dieta equilibrada.
        - Calorias equilibradas.
        """)
    if biotipo == "Endomorfo":
        print("""
        Treino para Endomorfo:
        - Foco em exercícios aeróbicos para perda de gordura.
        - Controlar ingestão calórica.
        - Treino de força para construção muscular.
        """)
    print("\nATENÇÂO")
    print("\nA relação entre IMC e biotipo corporal não é absoluta, variando \nentre indivíduos, genética, estilo de vida e composição corporal \ntambém afetam essa relação.\n")
    input("Pressione Enter para retornar ao menu...")

# Função de menu:
def menu():
    while True:
        limpar_tela()
        print("    Menu    \n".center(50))
        print("1. Identificar o Biotipo e Passar Treino")
        print("2. Sair\n")
        opcao = int(input("Selecione uma Opção: "))

        if opcao == 1:
            idade, peso, altura = Coletar_Dados()
            biotipo = Identificar_Biotipo(peso, altura)
            Treino_Para_Biotipo(biotipo)
        elif opcao == 2:
            print("\nObrigado por utilizar o programa!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            input("Pressione Enter para retornar ao menu...")

if __name__ == "__main__":
    menu()
  
