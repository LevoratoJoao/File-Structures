# --------------------------------
# --------------------------------
class Game:
    # construtor do objeto Game
    def __init__(self, nome=None, genero=None, plataforma=None,
        ano=None, classificacao=None, preco=None, midia=None,
        tamanho=None, produtora=None):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        self.produtora = produtora
    
    def __repr__(self):
        if(not self.selfNone(self.nome)):
            return '' + self.nome + '|' + self.genero + '|' + self.plataforma + '|' + self.ano + '|' + self.classificacao + '|' + self.preco + '|' + self.midia + '|' + self.tamanho + '|' + self.produtora + ''
        else:
            return "None"

    def getSize(self):
        size = len(self.nome) + len(self.genero) + len(self.plataforma) + len(self.ano) + len(self.classificacao) + len(self.preco) + len(self.midia) + len(self.tamanho) + len(self.produtora)
        return size

    def getNumberOfParameters(self):
        count = 0
        if self.nome != "None":
            count += 1
        if self.genero != "None":
            count += 1
        if self.plataforma != "None":
            count += 1
        if self.ano != "None":
            count += 1
        if self.classificacao != "None":
            count += 1
        if self.preco != "None":
            count += 1
        if self.midia != "None":
            count += 1
        if self.tamanho != "None":
            count += 1
        if self.produtora != "None":
            count += 1
        return count

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def plataforma(self):
        return self._plataforma
    
    @plataforma.setter
    def plataforma(self, plataforma):
        self._plataforma = plataforma
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def classificacao(self):
        return self._classificacao
    
    @classificacao.setter
    def classificacao(self, classificacao):
        self._classificacao = classificacao

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def midia(self):
        return self._midia
    
    @midia.setter
    def midia(self, midia):
        self._midia = midia

    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho

    @property
    def produtora(self):
        return self._produtora
    
    @produtora.setter
    def produtora(self, produtora):
        self._produtora = produtora

# --------------------------------
# --------------------------------
