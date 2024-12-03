### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

try:
    quantidade = int(input("Insira a quantidade desejada: "))
    preco = float(input("Insira o preço do item: "))
    if quantidade > 0 and preco > 0:
        print("Dados Válidos")
    else:
        print("Dados Inválidos")
except ValueError:
    print("Dados inseridos não atendem ao solicitado")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
    # Temperatura < 18°C é 'Baixa'
    # Temperatura >= 18°C e <= 26°C é 'Normal'
    # Temperatura > 26°C é 'Alta'

try: 
    temperatura = float(input("Insira aqui a temperatura para classificação: "))

    if temperatura < 18:
        print("Baixa")
    elif temperatura >= 18 and temperatura <= 26:
        print("Normal")
    else:
        print("Alta")
except ValueError:
    print("Valor inserido não se enquadra no formato requerido.")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

mensagem = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if mensagem["level"] == 'ERROR':
    print(mensagem["message"])


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:
    idade = int(input("Inserir sua idade: "))
    email = input("Inserir e-mail de contato: ")

    if idade <= 18 and idade <= 65:
        print("Idade fora do intervalo permitido!")
    elif "@" not in email or "." not in email:
        print("E-mail inválido!")
    else:
        print("Dados de usuário válidos!")
except ValueError:
    print("Inserir dados conforme formatações desejadas")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}
if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação normal")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem [palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

validos = [usuario for usuario in usuarios if usuario["email"]]

print(validos) 

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
sequencia = range(num1, num2)
pares = [x for x in sequencia if x % 2 == 0]
print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_categoria:
        total_categoria[categoria] += valor
    else:
        total_categoria[categoria] = valor
print(total_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

def leitura_dados():
    print("Digite os dados (digite 'sair' para encerrar):")
    dados = []
    
    while True:
        entrada = input("Entrada: ")
        if entrada.lower() == "sair":
            break
        dados.append(entrada)
    
    print("\nDados fornecidos:")
    for dado in dados:
        print(dado)

# Chamar a função para execução
leitura_dados()


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero = int(input("Digite um número entre 1 e 10: "))

while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))
print("Número válido!")


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
paginas_totais = 10

while pagina_atual < paginas_totais:
    print(f"Processando página atual {pagina_atual} de um total de {paginas_totais} páginas")
    pagina_atual += 1
print("Todas as páginas foram processadas!")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

limite = 10
tentativa = 1

while tentativa < limite:
    print(f"Tentando conexão...tentativa {tentativa}.")
    if True:
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Todas as tentativas foram utilizadas!")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

i = 0

while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada.")
        break
    print(f"Processando item: {itens[i]}")
    i += 1
