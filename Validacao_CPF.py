def formataCPF(numeros):
    # Validação: 11 caracteres e todos numéricos
    if len(numeros) != 11 or not numeros.isdigit():
        return None
    # Fatiamento para montar os blocos
    return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"

# Lista que guarda os cadastros enquanto o programa roda
pessoas = []

def cadastrar():
    nome = input("Digite o nome: ")
    cpf = formataCPF(input("Digite o CPF (apenas números): "))

    if cpf is None:
        print("CPF inválido! Deve ter 11 dígitos numéricos.")
        return

    pessoas.append({"nome": nome, "cpf": cpf})
    print(f"Cadastro realizado: {nome} - CPF {cpf}")

def listar():
    if not pessoas:
        print("Nenhum cadastro encontrado.")
        return
    for i, p in enumerate(pessoas, start=1):
        print(f"{i} | {p['nome']} | CPF: {p['cpf']}")

def remover():
    listar()
    if not pessoas:
        return
    indice = int(input("Digite o número para remover: ")) - 1
    if 0 <= indice < len(pessoas):
        removida = pessoas.pop(indice)
        print(f"Removido: {removida['nome']}")
    else:
        print("Número inválido.")

# --- Menu principal ---
while True:
    print("\n--- Cadastro de CPF ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Remover")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        remover()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")