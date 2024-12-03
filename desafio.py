base_ano = 1000

try:
    nome_funcionario = input("Digite o seu nome: ")
    # Verifica se o nome foi preenchido
    if len(nome_funcionario) == 0:
        print("Nome não preenchido. Gentileza inserir o seu nome para realização de cálculo.")
    # Verifica se nome foi preenchido somente com espaços em branco
    elif nome_funcionario.isspace() == True:
        print("Nome preenchido somente com espaços. Realizar entrada válida.")
    # Verificação se houve inserção de números no campo string
    elif any(char.isdigit() for char in nome_funcionario):
        print("Entrada não aceita números. Inserir nome válido")
    else:
        print("Nome inserido com sucesso!")
except ValueError as e:
    print(e)

    # Verificação para inserção de salários
try:
    salario = float(input("Digite o seu salário: "))
    if salario < 0:
        print("Salário inserido incorretamente. Favor inserir valor positivo.")
except ValueError:
    print("Entrada inválida.")

    # Verificação para inserção de Bônus
try:
    bonus = float(input("Digite o percentual de bonus: "))
    if bonus < 0:
        print("Bônus inválido. Gentileza inserir valor positivo.")
except ValueError:
    print("Entrada inválida!")

valor_bonus = (base_ano + salario) * bonus
print(f"Olá {nome_funcionario}, o seu bônus foi de {valor_bonus} !")