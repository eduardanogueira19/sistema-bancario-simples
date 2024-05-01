escolha = 0
limite = 2000
saque = 0
deposito = 0
#cadastro
nome_completo = str(input("Digite o seu nome completo: ")).strip()
cpf = str(input("Digite o seu CPF (Somente números): ")).strip()
senha = str(input("Digite uma senha: "))
op = 1
while op != 0:
    #login
    print("Bem-Vindo ao Sistema Bancário")
    cpf_login = str(input("Digite o CPF Cadastrado (Somente número): "))
    senha_login = str(input("Insira a sua senha: "))
    if (cpf_login == cpf) and (senha_login == senha):
        print("Dados corretos!")
        op = 0
    else: 
        print("Dados incorretos!")
#opção de transação
op = 1
while op != 0:
    escolha = int(input("Escolha o que deseja fazer:\n1 - Realizar Saque\n2 - Conferir Limite\n3 - Deposito\n"))
    if escolha == 1:
        saque = float(input("Quanto gostaria de sacar: "))
        if saque <= limite:
            limite = limite - saque
            print("Saque Realizado!")
            op = int(input("Deseja voltar ao menu de escolha?\n0 - Não\n1 - Sim\n"))
            if op == 0:
                print("saindo...")
            else: 
                print("Voltando ao menu...")
        else:
            print("Valor inválido!")
    elif escolha == 2:
        print("Limite: R${:.2f}".format((limite)))
        op = int(input("Deseja voltar ao menu de escolha?\n0 - Não\n1 - Sim\n"))
        if op == 0:
            print("saindo...")
        else: 
            print("Voltando ao menu...")
    elif escolha == 3:
        deposito = float(input("Quanto gostaria de depositar na sua conta: "))
        limite = limite + deposito
        op = int(input("Deseja voltar ao menu de escolha?\n0 - Não\n1 - Sim\n"))
        if op == 0:
            print("saindo...")
        else: 
            print("Voltando ao menu...")
