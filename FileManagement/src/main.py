import sys
from Game import Game
import Leituras as read
import Escritas as write

# Funcao para definir caminho dos arquivos
def definePaths(argv):
    filePath = argv[1]
    outputOnePath = argv[2]
    outputTwoPath = argv[3]
    outputThreePath = argv[4]
    outputFourPath = argv[5]
    return filePath, outputOnePath, outputTwoPath, outputThreePath, outputFourPath

# Funcao para abertura dos arquivos
def openingFiles(paths):
    outOne = open(paths[1], "w")
    outTwo = open(paths[2], "w")
    outThree = open(paths[3], "w")
    outFour = open(paths[4], "w")
    return outOne, outTwo, outThree, outFour

# Funcao para fechar todos os arquivos usados
def closingFiles(outputFiles):
    for i in range(0, len(outputFiles)):
        outputFiles[i].close()

def main():
    paths = definePaths(sys.argv) # List de paths
    game = [] # Lista de games
    try:
        f = open(paths[0], "r").readlines()
    except FileNotFoundError:
            print("Error: file does not exist")
            raise FileNotFoundError
    # Identificacao de qual caso de leitura foi usado
    if paths[0] == "DataBases/games.txt":
        game = read.leituraPadrao(f, game)
    elif paths[0] == "DataBases/outputOne.txt":
        game = read.leituraTamanhosFixos(f, game)
    elif paths[0] == "DataBases/outputTwo.txt":
        game = read.leituraQtdeBytesComeco(f, game)
    elif paths[0] == "DataBases/outputThree.txt":
        game = read.leituraQtdeCamps(f, game, n=9)
    elif paths[0] == "DataBases/outputFour.txt":
        game = read.leituraDelimitador(f, game)

    # game.sort(key = lambda x: x.nome)  - sort the games by name using lambda function

    outputFiles = openingFiles(paths)

    write.escritaTamanhosFixos(outputFiles[0], game)
    write.escritaQtdeBytesComeco(outputFiles[1], game)
    write.escritaQtdeCamps(outputFiles[2], game)
    write.escritaDelimitador(outputFiles[3], game)

    closingFiles(outputFiles)

if __name__ == "__main__":
    main()