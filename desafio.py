base_ano = 1000
nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
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
            print(f"Nome válido: {nome_funcionario}")
            print("Nome inserido com sucesso!")
            nome_valido = True
    except ValueError as e:
        print(e)

while salario_valido is not True:
    # Verificação para inserção de salários
    try:
        salario = float(input("Digite o seu salário: "))
        if salario < 0:
            print("Salário inserido incorretamente. Favor inserir valor positivo.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida.")


    # Verificação para inserção de Bônus

while bonus_valido is not True:
    try:
        bonus = float(input("Digite o percentual de bonus: "))
        if bonus < 0:
            print("Bônus inválido. Gentileza inserir valor positivo.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida!")

valor_bonus = (base_ano + salario) * bonus
print(f"Olá {nome_funcionario}, o seu bônus foi de {valor_bonus} !")