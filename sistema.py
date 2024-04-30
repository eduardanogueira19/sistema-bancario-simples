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

print("Escolha o que deseja fazer: ")


#opção de transação

