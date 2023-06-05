# Objeto de Heroi
class Heroi:
    def __init__(self, chave, primeiroNome, sobrenome, nomeHeroi, poder, fraqueza, cidade, profissao):
        self.chave = chave # chave numerica pode ter até 3 digitos
        self.primeiroNome = primeiroNome # primero nome do heroi (até 15 chars)
        self.sobrenome = sobrenome # seu sobrenome (até 15 chars)
        self.nomeHeroi = nomeHeroi # nome do Heroi, alias (até 15 chars)
        self.poder = poder # poder (até 15 chars)
        self.fraqueza = fraqueza # fraqueza (até 20 chars)
        self.cidade = cidade # cidade que defende (até 20 chars)
        self.profissao = profissao # profissao da sua identidade secreta (até 20 chars)
# ...
# demais metodos

    def __str__(self):
        return f"{self.chave}|{self.primeiroNome}|{self.sobrenome}|{self.nomeHeroi}|{self.poder}|{self.fraqueza}|{self.cidade}|{self.profissao}"

    @property
    def chave(self):
        return self._chave

    @chave.setter
    def chave(self, chave):
        self._chave = chave

    @property
    def primeiroNome(self):
        return self._primeiroNome

    @primeiroNome.setter
    def primeiroNome(self, primeiroNome):
        self._primeiroNome = primeiroNome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def nomeHeroi(self):
        return self._nomeHeroi

    @nomeHeroi.setter
    def nomeHeroi(self, nomeHeroi):
        self._nomeHeroi = nomeHeroi

    @property
    def poder(self):
        return self._poder
    
    @poder.setter
    def poder(self, poder):
        self._poder = poder

    @property
    def fraqueza(self):
        return self._fraqueza
    
    @fraqueza.setter
    def fraqueza(self, fraqueza):
        self._fraqueza = fraqueza

    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def profissao(self):
        return self._profissao
    
    @profissao.setter
    def profissao(self, profissao):
        self._profissao = profissao
