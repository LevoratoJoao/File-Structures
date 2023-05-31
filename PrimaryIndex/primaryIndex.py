#------------------------------------------------------
# Tabela de indice primario
#------------------------------------------------------

import os

#------------------------------------------------------
#------------------------------------------------------

class IndicePrimario:

	# atributos
	# 1. arquivo de dados (escrita/leitura), [r+]
	__arquivoDados = None
	# 2. arquivo tabela de idx primario (escrita/leitura) []
	__arquivoIdxPrimario = None
	# 3. tabela de indices
	__tabelaIndices = list()

	# A: construtor
	def __init__(self):
     	# path = '/home/joaolevorato/programacao/File-Structures/PrimaryIndex/arqDados.txt'
		self.__arquivoDados = open("/media/a2419890/home/File-Structures/PrimaryIndex/arqDados.txt", "r+") # abrir o arquivo de dados (arquivo existente)
		# arquivo de idx primario
		if(os.path.isfile("arqIdxPrimario.txt")):
			print("Existe arquivo de indice primario")
			self.__arquivoIdxPrimario = open("PrimaryIndex/arqIdxPrimario.txt", "r+")
			# TODO: carregar/criar tabela com base no arquivo de idx
			RRN = 0
   			for line in self.__arquivoIdxPrimario.readlines().split():
				print(line)
				chave = self.criaChaveCanonica(line) # criar chave, RRN
				self.__tabelaIndices.append((chave, RRN)) # add tupla na tabela de indices
				RRN+=1
		else: # - se nao existir, criar arquivo (vazio)
			print("Nao existe arquivo de indice primario")
			self.__arquivoIdxPrimario = open("PrimaryIndex/arqIdxPrimario.txt", "a+")
			RRN = 0
			# - percorrer o arquivo linha por linha
			for line in self.__arquivoDados.readlines()[1:]:
				chave = self.criaChaveCanonica(line) # criar chave, RRN
				self.__tabelaIndices.append((chave, RRN)) # add tupla na tabela de indices
				RRN+=1
			# (chave, RRN) -> tupla[0]
			self.__tabelaIndices.sort(key=lambda a: a[0]) # ordenar a tabela
			for i in range(0, len(self.__tabelaIndices)):
				print(self.__tabelaIndices[i])

	def criaChaveCanonica(self, registro):
		x = registro.split('|')
		chavePrimaria = x[0] + x[4]
		chavePrimaria = chavePrimaria.upper().replace(' ', '')
		return chavePrimaria

	# B: destrutor
	def __del__(self):
		self.__arquivoIdxPrimario.seek(0)
		for i in range(0, len(self.__tabelaIndices)):
			self.__arquivoIdxPrimario.write(f"{self.__tabelaIndices[i][0]} {self.__tabelaIndices[i][1]}\n")
		self.__arquivoDados.close()
		self.__arquivoIdxPrimario.close()
	# fecha o arquivo de dados
	# arquivo de indices
	# 	- gravar a tabela no arquivo, fecha o arquivo

	#---------------------
	# C: Insercao (registro)
	#---------------------
	def insereRegistro(self, registro):
		pass
	#	calcular chave primaria do registro
	#   procurar na tabela (RAM) se a chave ja existe
	#   se a chave ja existir: nao faz nada!
	#   senao:
	#       verificar se tem espaco vago no arquivo (header, TOP)
	#       RNN <- se tiver espaco vago: reuso
	#       RNN <- se nao tiver: append
	#       add na tabela (chave, RNN)
	#       reordena a tabela

	#---------------------
	# D: Pesquisa (chave)
	#---------------------
	def pesquisaRegistro(self, chave) :
		pass
	#	confere na tabela (chave == alguem?), busca binaria
	#   se nao existe na tabela: nao faz nada
	#   se existe na tabela (chave, RRN)
	#   vai no arquivo de dados (RRN)
	#   retorna o registro



#------------------------------------------------------
#------------------------------------------------------