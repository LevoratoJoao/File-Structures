import sys
from Game import Game

def leituraDelimitador(f, game):
    for line in f:
        reading = line.strip().split("|")
        print(reading)
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
        game.append(Game(nome, genero, plataforma, str(ano), classificacao, str(preco), midia, str(tamanho), produtora))
        nome, produtora, genero, plataforma, ano, classificacao, preco, midia, tamanho = None, None, None, None, None, None, None, None, None
    return game

def escritaDelimitador(f, game):
    for i in range(0, len(game)):
        f.write(f"# {game[i].nome}|{game[i].produtora}|{game[i].genero}|{game[i].plataforma}|{game[i].ano}|{game[i].classificacao}|{game[i].preco}|{game[i].midia}|{game[i].tamanho}|")

def escritaQtdeCamps(f, game):
    for i in range(0, len(game)):
        if game[i].getNumberOfParameters() == 9:
            f.write(f"{game[i].nome}|{game[i].produtora}|{game[i].genero}|{game[i].plataforma}|{game[i].ano}|{game[i].classificacao}|{game[i].preco}|{game[i].midia}|{game[i].tamanho}|")
        else: 
            print(f"Object {i + 1} doesnt have the right size of fields")

def escritaQtdeBytesComeco(f, game):
    for i in range(0, len(game)):
        f.write(f"{game[i].getSize()}{game[i].nome}|{game[i].produtora}|{game[i].genero}|{game[i].plataforma}|{game[i].ano}|{game[i].classificacao}|{game[i].preco}|{game[i].midia}|{game[i].tamanho}|")

def escritaTamanhosFixos(file, game):
    for i in range(0, len(game)):
        file.write(f"{game[i].nome[:50]}|{game[i].produtora[:35]}|{game[i].genero[:25]}|{game[i].plataforma[:16]}|{game[i].ano[:4]}|{game[i].classificacao[:15]}|{game[i].preco[:10]}|{game[i].midia[:10]}|{game[i].tamanho[:5]}|")

def definePaths(argv):
    filePath = argv[1]
    outputOnePath = argv[2]
    outputTwoPath = argv[3]
    outputThreePath = argv[4]
    outputFourPath = argv[5]
    return filePath, outputOnePath, outputTwoPath, outputThreePath, outputFourPath

def openingFiles(paths):
    outOne = open(paths[1], "w")
    outTwo = open(paths[2], "w")
    outThree = open(paths[3], "w")
    outFour = open(paths[4], "w")
    return outOne, outTwo, outThree, outFour

def closingFiles(outputFiles):
    for i in range(0, len(outputFiles)):
        outputFiles[i].close()

def main():
    paths = definePaths(sys.argv)
    try:
        f = open(paths[0], "r").readlines()
    except FileNotFoundError:
            print("Error: file does not exist")
            raise FileNotFoundError

    game = leituraDelimitador(f, game=[])
    # game.sort(key = lambda x: x.nome)  - sort the games by name using lambda function

    outputFiles = openingFiles(paths)

    escritaTamanhosFixos(outputFiles[0], game)
    escritaQtdeBytesComeco(outputFiles[1], game)
    escritaQtdeCamps(outputFiles[2], game)
    escritaDelimitador(outputFiles[3], game)

    closingFiles(outputFiles)

if __name__ == "__main__":
    main()