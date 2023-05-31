import sys
from Game import Game
import re

# Funcao para controle de erros nos parametros de cada game -> caso um dos campos esteja errado por exemplo
# Atribui None aos valores inteiros que estao incorretos
def exceptionHandling(reading):
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
    game = Game(nome, genero, plataforma, str(ano), classificacao, str(preco), midia, str(tamanho), produtora)
    return game

def buildKey(nome, ano):
    nome = nome.replace(" ", "")
    key = nome.upper() + str(ano)
    return key

def procuraRegistro(keySearch, game):
    for i in range(0, len(game)):
        keyGame = buildKey(game[i].nome, game[i].ano)
        if keySearch == keyGame:
            return True, i
    return False, None

def adicionaRegistro(op, game, firstLine):
    op[1] = op[1].lstrip('0123456789.- ') # Alguns games comecavam com numeros nos nomes de forma incorreta, isso preve este erro (lstrip - remove o que for passado por parametro)
    keySearch = buildKey(op[1], op[5])
    find = procuraRegistro(keySearch, game)
    if find[0] == False:
        if firstLine[1] == -1:
            game.append(exceptionHandling(op[1:]))
            firstLine[0] = firstLine[0] + 1
        else:
            index = [int(x) for x in re.findall(r'-?\d+\.*', game[firstLine[1]].nome[0:3])] # Regex para extrair o numero a ser novo TOP (tem formas mais simples mas queria brincar com regex)
            game[firstLine[1]] = exceptionHandling(op[1:])
            # Atualizacao da firstLine:
            firstLine[0] = firstLine[0] + 1
            firstLine[1] = index[0]
    else:
        print(f"Game {op[1]} already exist in the data base\n")

def removerRegistro(op, game, firstLine):
    find = list(procuraRegistro(op[1], game))
    if find[0] == True:
        game[find[1]].nome = game[find[1]].nome.replace(game[find[1]].nome[:len(str(firstLine[1])) + 2], f"*{firstLine[1]}|") # sobrescreve o registro a ser "removido" (replace com um parametro ja sendo o nome com a quantia correta de bytes a ser sobrescrito)
        firstLine[1] = find[1]
        firstLine[0] = firstLine[0] - 1
    else:
        print(f"Game {op[1]} doesnt exist in the data base\n")

# A funcao storageCompaction também foi usada para salvar o arquivo temp
def storageCompaction(otp1, tmp1, firstLine, game):
    otp = open(otp1, "w")
    tmp = open(tmp1, "w")
    otp.write(f"REG.N={firstLine[0]} TOP={firstLine[1]}\n")
    tmp.write(f"REG.N={firstLine[0]} TOP={firstLine[1]}\n")
    for i in range(0, len(game)):
        if not ("*" in game[i].nome):
            # __repr__ = representacao padrao do objeto
            otp.write(f"{game[i].__repr__()}\n")
            tmp.write(f"{game[i].__repr__()}\n")
        else:
            tmp.write(f"{game[i].__repr__()}\n")
    otp.close()
    tmp.close()

def main():
    with open(sys.argv[1], "r") as fileOne, open(sys.argv[2], "r") as fileTwo:
        games = list(fileOne.readlines())
        op = list(fileTwo.readlines())

    tmp = open(sys.argv[3], "w")
    tmp.seek(0)
    firstLine = [int(x) for x in re.findall(r'-?\d+\.*', games[0])] # Regex para extrair apenas os numeros da primeira linha -> REG.N e TOP (-?\d = encontra tanto numeros negativos quanto positivos, \.* procura mais de um match)
    game = []
    for value in games[1:]:
        reading = value.strip().split("|") # Separa os campos dos registros
        game.append(exceptionHandling(reading))

    for i in range(0, len(op)): # Percorre as operacoes
        opRead = op[i].strip().split(",")
        opRead[1] = opRead[1].strip()
        if op[i][0] == "i":
            adicionaRegistro(opRead, game, firstLine)
        elif op[i][0] == "d":
            removerRegistro(opRead, game, firstLine)
    storageCompaction(sys.argv[4], sys.argv[3], firstLine, game)

if __name__ == "__main__":
    main()