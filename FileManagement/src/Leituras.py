from Game import Game

# Funcao para controle de erros nos parametros de cada game -> caso um dos campos esteja errado por exemplo
# Atribui None aos valores inteiros que estao incorretos
def ExceptionHandling(reading, game):
    try:
        nome = reading[0]
        produtora =  reading[1]
        genero = reading[2]
        plataforma = reading[3]
        try:
            ano = int(reading[4])
        except ValueError:
            ano = None
            print(f"\nError: ValueError at game {reading[0]} - {reading[4]}\nThe wrong parameter of this game will be set as None in the data base\n")
        classificacao = reading[5]
        preco = reading[6]
        midia = reading[7]
        try:
            tamanho = float(reading[8])
        except ValueError:
            tamanho = None
            print(f"\nError: ValueError at game {reading[0]} - {reading[8]}\nThe wrong parameter of this game will be set as None in the data base\n")
    except IndexError:
        print(f"\nError: IndexError at game {reading}\nThe wrong parameter of this game will be set as None in the data base\n")
        tamanho = None
    game.append(Game(nome, genero, plataforma, str(ano), classificacao, str(preco), midia, str(tamanho), produtora))
    return game

# Leitura padrao do arquivo games.txt
def leituraPadrao(f, game):
    for line in f:
        reading = line.strip().split("|")
        game = ExceptionHandling(reading, game)
    return game

def leituraDelimitador(f, game):
    line = f[0].split("#")
    line.pop(0) # Remove o primeiro item da lista (#)
    while range(0, len(line)):
        reading = line[0].split("|")
        reading.pop()
        game = ExceptionHandling(reading, game)
        line.pop(0) # Funciona como uma pilha só que reversa, remove o primeiro apos ser lido
    return game

# Esta funcao por ter tamanhos fixos nas variaveis esta separada e zera (None) todos os valores ao final para a nova leitura de linha
def leituraTamanhosFixos(f, game):
    for line in f:
        reading = line.strip().split("|")
        try:
            nome = reading[0][:50]
            produtora =  reading[1][:35]
            genero = reading[2][:25]
            plataforma = reading[3][:16]
            try:
                ano = int(reading[4][:4])
            except ValueError:
                ano = None
                print(f"\nError: ValueError at game {reading[0]} - {reading[4]}\nThe wrong parameter of this game will be set as None in the data base\n")
            classificacao = reading[5][:15]
            preco = reading[6][:10]
            midia = reading[7][:10]
            try:
                tamanho = float(reading[8][:5])
            except ValueError:
                tamanho = None
                print(f"\nError: ValueError at game {reading[0]} - {reading[8]}\nThe wrong parameter of this game will be set as None in the data base\n")
        except IndexError:
            print(f"\nError: IndexError at game {reading}\nThe wrong parameter of this game will be set as None in the data base\n")
        game.append(Game(nome, genero, plataforma, str(ano), classificacao, str(preco), midia, str(tamanho), produtora))
        nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho = None, None, None, None, None, None, None, None, None
    return game

def leituraQtdeBytesComeco(f, game):
    for line in f:
        n = ""
        for i in line:
            if i.isdigit() == True: # percorre enquanto i for um digito
                n = n + i # Contatena os numeros da primeira linha
            else:
                break
        reading = line.lstrip('0123456789').split("|")[:int(n)] # Exclui os primeiros numeros e le a quantidade de bytes desejada
        reading.pop() # Exclui a linha a + lida
        game = ExceptionHandling(reading, game)
    return game

def leituraQtdeCamps(f, game, n):
    for line in f:
        count = line.count("|") # Faz a contagem de parametros (campos) nas linhas
        if count == n:
            reading = line.strip().split("|")
            game = ExceptionHandling(reading, game)
        else:
            print(f"Error: the game {line}should have 9 fields in the data base\n")
    return game