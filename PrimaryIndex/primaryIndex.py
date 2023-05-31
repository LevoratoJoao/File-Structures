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

	#---------------------
	# A: construtor
	#---------------------
	def __init__(self):
		self.__arquivoDados = open("/home/joaolevorato/programacao/File-Structures/PrimaryIndex/arqDados.txt", "r+")
		# abrir o arquivo de dados (arquivo existente)
		# arquivo de idx primario
		if(os.path.isfile("arqIdxPrimario.txt")):
			print("Existe arquivo de indice primario")
			self.__arquivoIdxPrimario = open("arqIdxPrimario.txt", "r+")
			# TODO: carregar/criar tabela com base no arquivo de idx
			RRN = 0
			for line in self.__arquivoDados.readlines()[1:]:
				print(line)
				# - criar chave, RRN
				chave = self.criaChaveCanonica(line)
				print("-------------")
				print(chave)
				print(RRN)
				self.__tabelaIndices.append((chave, RRN))
					# - add tupla na tabela de indices
				RRN+=1
		else:
			# - se nao existir, criar arquivo (vazio)
			print("Nao existe arquivo de indice primario")
			self.__arquivoIdxPrimario = open("arqIdxPrimario.txt", "a+")
				# - tabela de indices e vazia
				# - percorrer o arquivo linha por linha
			RRN = 0
			for line in self.__arquivoDados.readlines()[1:]:
				# - criar chave, RRN
				chave = self.criaChaveCanonica(line)
				self.__tabelaIndices.append((chave, RRN))
				# - add tupla na tabela de indices
				RRN+=1

			for i in range(0, len(self.__tabelaIndices)):
				print(self.__tabelaIndices[i])
			# - ordenar a tabela
			# (chave, RRN) -> tupla[0]
			self.__tabelaIndices.sort(key=lambda a: a[0])
			# print(self.__tabelaIndices)
			for i in range(0, len(self.__tabelaIndices)):
				print(self.__tabelaIndices[i])

	def criaChaveCanonica(self, registro):
		x = registro.split('|')
		print(x)
		chavePrimaria = x[0] + x[4]
		chavePrimaria = chavePrimaria.upper().replace(' ', '')
		return(chavePrimaria)

	#---------------------
	# B: destrutor
	#---------------------
	def __del__(self):
		pass
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