from time import sleep
def cabecalho(msg):
    print('-'*50)
    print(msg)
    print('-'*50)

def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3 
    usuarios = []
    contas = []
    numero_conta = 1


    while True:
        opcao = menu()
        sleep(1)
        if opcao == 'd':
            cabecalho("== Depositar == ".center(50))
            deposito = float(input("\n  Informe a quantidade a depositar: "))
            saldo, extrato = depositar(saldo, deposito, extrato)
            
        elif opcao == 's':
            cabecalho("=== Sacar ===".center(50))
            valor = float(input("\n  Qual valor você gostaria de sacar : "))
            saldo, extrato, numero_saques = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques= numero_saques ,LIMITE_SAQUES = LIMITE_SAQUES,)
            
        elif opcao == 'e':
            exibir_extrato(saldo,numero_saques, extrato= extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            conta = criar_conta(AGENCIA,numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta+=1
        
        elif opcao == 'lc':
            listar_contas(contas)
            
        elif opcao == 'q':
            cabecalho(" == Saindo do sistema == ".center(50))
            break
        else:
            print('Por favor escolhar opção válida.')
          
def menu():

    menu = """  
        Bem vindo ao nosso sistema Bancário.
            Selecione a opção desejada:

        [d]  Depositar
        [s]  Sacar
        [e]  Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q]  Sair  
    => """
    return input(menu)

def depositar(saldo, deposito, extrato,/):
    if deposito > 0:
        saldo += deposito
        extrato += f'\tDepósito: \tR$ {deposito:.2f}\n'
        print(f"== Depósito de R$ {deposito:.2f} realizado com sucesso. ==")
    else:
        print("== Impossível realizar a operação. == ")
    return saldo, extrato

def sacar(*,saldo,valor, limite,numero_saques, LIMITE_SAQUES, extrato):
    if valor > saldo:
        print("Você não possui saldo suficiente.")
    elif valor > limite:
        print("Valor inválido, o seu limite de saque é de R$ 500,00")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você não tem limites para saque. Por favor utilizar a opção de saque em outro dia.")
    elif valor > 0:
        saldo -= valor
        extrato += f'\tSaque : \tR$ {valor:.2f}\n'
        numero_saques += 1
        print(f'Você sacou R$ {valor:.2f} e seu saldo atual é de R$ {saldo:.2f}')
    else:
        print("== Impossível realizar a operação ==")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo,numero_saques,/,*,extrato):
    cabecalho("=== Extrato ===".center(50))
    print(extrato)
    print(f'\nSeu Saldo é de R$ {saldo:.2f}. E você tem {3 - numero_saques} saques disponíveis.')

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        cabecalho("== Usuário já cadastrado ==".center(50))
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input('Informe o endereço (Logradouro, número e complemento se houver - bairro - cidade/sigla estado): ')

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})
    
    cabecalho("== Usúario cadastrado com sucesso !!! ==".center(50))

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o cpf (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        cabecalho(" == Conta criada com sucesso == ".center(50))
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    cabecalho("Usuário não encontrado, por favor cadastrar usuário".center(50))

def listar_contas(contas):
    for conta in contas:
        print(f'O cliente {conta["usuario"]["nome"]} tem conta em nossa agência {conta["agencia"]} com o número de c/c {conta["numero_conta"]}')
    

main()
