from Game import Game

def escritaDelimitador(f, game):
    for i in range(0, len(game)):
        f.write(f"#{game[i].nome}|{game[i].produtora}|{game[i].genero}|{game[i].plataforma}|{game[i].ano}|{game[i].classificacao}|{game[i].preco}|{game[i].midia}|{game[i].tamanho}|")

def escritaQtdeCamps(f, game):
    for i in range(0, len(game)):
        if game[i].getNumberOfAttributes() == 9:
            f.write(f"{game[i].nome}|{game[i].produtora}|{game[i].genero}|{game[i].plataforma}|{game[i].ano}|{game[i].classificacao}|{game[i].preco}|{game[i].midia}|{game[i].tamanho}|\n")
        else:
            print(f"Object {i + 1} doesnt have the right size of fields")

def escritaQtdeBytesComeco(f, game):
    for i in range(0, len(game)):
        f.write(f"{game[i].getSize()}{game[i].nome}|{game[i].produtora}|{game[i].genero}|{game[i].plataforma}|{game[i].ano}|{game[i].classificacao}|{game[i].preco}|{game[i].midia}|{game[i].tamanho}|\n")

def escritaTamanhosFixos(file, game):
    for i in range(0, len(game)):
        file.write(f"{game[i].nome[:50]}|{game[i].produtora[:35]}|{game[i].genero[:25]}|{game[i].plataforma[:16]}|{game[i].ano[:4]}|{game[i].classificacao[:15]}|{game[i].preco[:10]}|{game[i].midia[:10]}|{game[i].tamanho[:5]}|\n")