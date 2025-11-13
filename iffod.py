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


# PAGINA PRINCIPAL
print("BEM-VINDO AO FEIFOOD 🍔")
print("1 - Ver menu de alimentos")
print("2 - Sair")

# Pede para o usuário escolher uma opção
opcao = input("Escolha uma opção: ")

# Se o usuário escolher 1, vai ver o menu de alimentos
if opcao == "1":
    print("\nMENU DE ALIMENTOS")
    try: #comando p nao dar erro
        # Abre o arquivo de alimentos e lê todas as linhas
        with open("alimentos.txt", "r") as arquivo:
            alimentos = arquivo.readlines()
            
            # Se o arquivo estiver vazio, mostra que não há alimentos
            if not alimentos:
                print("Nenhum alimento disponível ainda.\n")
            else:
                # Percorre cada linha do arquivo e mostra os alimentos formatados
                for linha in alimentos:
                    partes = linha.strip().split("|")
                    if len(partes) == 3:
                        nome, tipo, preco = partes
                        print(f"- {nome} ({tipo}) - R$ {preco}")
    except FileNotFoundError:
        # Caso o arquivo alimentos.txt não exista
        print("Arquivo alimentos.txt não encontrado.\n")

# Se o usuário escolher 2, o programa encerra
elif opcao == "2":
    print("Saindo do feiFood... até logo!")
    exit()

# Caso o usuário digite uma opção inválida
else:
    print("Opção inválida! Encerrando o sistema.")
    exit()


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
email = input("Digite o seu e-mail: ").strip() # strip tira espaço extra
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
with open("alimentos.txt", "r") as arquivo:  #  cria uma lista de listas, separando por "|"
    alimentos = [linha.strip().split("|") for linha in arquivo]
encontrado = False # Cria uma variável de controle para saber se o alimento foi encontrado ou não
for nome, tipo, preco in alimentos: # Percorre cada alimento da lista
    if busca == nome:
        print(f"Alimento encontrado: {nome} ({tipo}) - R$ {preco}\n")
        encontrado = True
        break

if not encontrado:
    
    print("\nAlimento não encontrado.\nAlimentos disponíveis:")
    for nome, tipo, preco in alimentos:
        print(f"- {nome} ({tipo}) - R$ {preco}\n")
        
#CADASTRAR PEDIDO (criar, editar, e excluir pedidos + adicionar e remover da lista)
print("FAÇA SEU PEDIDO")
nome_usuario = input("Digite seu nome: ")
pedido = input("Digite o alimento que deseja pedir: ")
# abre a lista de alimentos e lê todas as linhas do arquivo
with open("alimentos.txt", "r") as arq:
    alimentos = [linha.strip().split("|") for linha in arq]
# percorre a lista de alimentos para verificar se o alimento digitado existe
for nome, tipo, preco in alimentos:
    if pedido == nome:  # se o alimento existir, coloca o pedido no arquivo
        with open("pedidos.txt", "a") as pededido: 
            pededido.write(f"{nome_usuario}|{nome}|{tipo}|{preco}\n")
        print(f"\nAlimento encontrado: {nome} ({tipo}) - R$ {preco}")
        # pergunta se quer continuar
        continuar = input("Deseja continuar com o pedido? (s/n): ").lower()
        if continuar == "s":
            # confirma o pedido e mostra mensagem
            print(f"\nPedido realizado com sucesso!\nVocê pediu: {nome} ({tipo}) - R$ {preco}\n")
            
            # AVALIAÇÃO DO PEDIDO (já existente no seu código)
            print("AVALIAÇÃO DO PEDIDO")
            avaliacao = input("Nos avalie de 0 a 5 estrelas: ")
            print(f"Obrigado pela sua avaliação de {avaliacao} estrelas!\n")
        else:
            print("Pedido cancelado.\n")
        break
else:
    # caso o alimento não exista, mostra mensagem de erro
    print("Alimento não encontrado.\n")


   # AVALIACAO DO PEDIDO 
    #DE 0 A 5 ESTRELAS!
    print("aviliacao")
    
avaliacao = input("Nos avalie de 0 a 5 estrelas: ")

print(f"Obrigado pela sua avaliação de {avaliacao} estrelas! ")
