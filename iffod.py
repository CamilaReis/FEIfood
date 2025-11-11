# Created on iPad.
#Objetivo: O objetivo do projeto FEIFood é construir uma plataforma de pedidos de comida
# Você pode se inspirar na Plataforma iFood, pois a ideia é a mesma
# Obs: não precisa implementar a lógica de mudança de status do pedido,pagamento e acompanhamento da entrega
# Tecnologias que devem ser usadas no desenvolvimento do projeto: Linguagem Python e arquivos de tex

# 1º Cadastrar novo usuário
# 2º Login de usuário
# 3º Buscar por alimento
# 4º Listar informações de alimentos buscados
# 5º Cadastrar pedido* - Criar, editar, excluir pedidos - Adicionar/remover alimentos da lista de pedidos
# 6º Avaliar pedido** - Atribuir de 0 a 5 estrelas para o pedido

# CADASTRA USUARIO
print("faca o seu cadastro")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")
with open("usuarios.txt", "a") as arquivo:
# O modo "a" significa "append" (acrescentar): ele adiciona as novas informações no final do arquivo
    arquivo.write(f"{nome}|{email}|{senha}\n")
print("Usuário cadastrado com sucesso!")

#LOGIN USUARIO
#pedir email e senha do usuario 
print("faca o seu login")
email = input("Digite o seu e-mail: ").strip() # strip e,e tura os espacis extras 
senha = input("Digite sua senha: ").strip()

with open("usuarios.txt", "r") as arquivo: # abre o arquivo
    usuarios = arquivo.readlines() #ler todas as linhas do arquivou

login_encontrado = False # controla-se o login foi encontrado
#tive que fazer isso pois estava dando problema no meu código
for linha in usuarios: #percorre as linhas da lista usuario 
    linha = linha.strip() # aqui está tirando os espaços
    if linha == "": # se a linha tiver vazia pular pra próxima
        continue
    partes = linha.split("|") # separar as informações que eu estou pedindo
    if len(partes) != 3: #garante que a linha tenha nome,email e senha
        continue
    nome_salvo, email_salvo, senha_salva = partes #guarda as minhas informações

    # faz uma comparação pra ver se está tudo certo
    if email.strip()==email_salvo.strip()and senha.strip()==senha_salva.strip():
        login_encontrado = True
        nome_usuario = nome_salvo.strip()
        break

if login_encontrado:
    print(f"Login realizado com sucesso! Bem-vindo(a),{nome_usuario}!")
else:
    print("Login não realizado. Verifique e-mail e senha.")
    exit()

#BUSCAR ALIMENTO
print("buscar alimentos disponiveis")
# Pede o nome do alimento
busca = input("Digite o nome do alimento que deseja procurar: ")
with open("alimentos.txt", "r") as arquivo:
    alimentos = arquivo.readlines()
# Cria uma lista para guardar os resultados encontrados
resultados = []
for linha in alimentos:
    linha = linha.strip()
    if linha == "":
        continue 
    partes = linha.split("|")
    if len(partes) != 3:
        continue  # Ignora linhas com erro
    nome, tipo, preco = partes
    # Verifica se o texto digitado aparece no nome do alimento
    if busca in nome:
        resultados.append((nome, tipo, preco))
# Mostra os resultados encontrados
if resultados:
    print("Alimentos encontrados:")
    for nome, tipo, preco in resultados:
        print(f"- {nome} ({tipo}) - R$ {preco}\n")
else:
    print("Nenhum alimento encontrado com esse nome.")

#LISTAR INFORMACAO DOS ALIMENTOS LISTADOS
busca = input("Digite o nome do alimento: ")
with open("alimentos.txt", "r") as arquivo:
    alimentos = [linha.strip().split("|") for linha in arquivo]
encontrado = False
for nome, tipo, preco in alimentos:
    if busca == nome:
        print(f"Alimento encontrado: {nome} ({tipo}) - R$ {preco}\n")
        encontrado = True
        break

if not encontrado:
    
    print("\nAlimento não encontrado.\nAlimentos disponíveis:")
    for nome, tipo, preco in alimentos:
        print(f"- {nome} ({tipo}) - R$ {preco}\n")
        
#CADASTRAR PEDIDO (criar, editar, e excluir pedidos + adicionar e remover da lista)
print("faca o seu cadastro do seu pedido")
nome_usuario = input("Digite seu nome: ") # nome de quem está fazendo o pedido
pedido = input("confirme o alimento escolhido: ")
# abra a lista de alimentos lê todas as linhas
#  vai ser separada por "|"
with open("alimentos.txt", "r") as arq:
    alimentos = [linha.strip().split("|") for linha in arq]
#percorre pela minha lista de alimentos
for nome, tipo, preco in alimentos:
    if pedido == nome: # aquele está verificando se o alimento digitado está no arquivo
        with open("pedidos.txt", "a") as ped: # se tiver abre o arquivo de pedidos e add 
            ped.write(f"{nome_usuario}|{nome}|{tipo}|{preco}\n")
        print(f" Pedido realizado com sucesso: {nome} ({tipo}) - R$ {preco}\n") # mostra q o pedidio foi realizado 
        break
else:
    print("Alimento não encontrado.") # se o pedido não for encontrado vai mostrar essa mensagem

   # AVALIACAO DO PEDIDO 
    #DE 0 A 5 ESTRELAS!
    print("aviliacao")
    
avaliacao = input("Nos avalie de 0 a 5 estrelas: ")

print(f"Obrigado pela sua avaliação de {avaliacao} estrelas! ")