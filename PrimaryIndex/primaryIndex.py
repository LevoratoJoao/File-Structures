import linecache
import re
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
		 # path = '/media/a2419890/home/File-Structures/PrimaryIndex/arqDados.txt'
		self.__arquivoDados = open("/home/joaolevorato/programacao/File-Structures/PrimaryIndex/arqDados.txt", "r+") # abrir o arquivo de dados (arquivo existente)
		if(os.path.isfile("PrimaryIndex/arqIdxPrimario.txt")): # arquivo de idx primario
			self.__arquivoIdxPrimario = open("PrimaryIndex/arqIdxPrimario.txt", "r+")
			for line in self.__arquivoIdxPrimario.readlines():
				chave, RRN = line.split()
				self.__tabelaIndices.append((chave, RRN)) # add tupla na tabela de indices
		else: # se nao existir, criar arquivo (vazio)
			print("Nao existe arquivo de indice primario")
			self.__arquivoIdxPrimario = open("PrimaryIndex/arqIdxPrimario.txt", "a+")
			RRN = 0
			# percorrer o arquivo linha por linha
			for line in self.__arquivoDados.readlines()[1:]:
				chave = self.criaChaveCanonica(line) # criar chave, RRN
				self.__tabelaIndices.append((chave, RRN)) # add tupla na tabela de indices
				RRN+=1
			# (chave, RRN) -> tupla[0]
			self.__tabelaIndices.sort(key=lambda a: a[0]) # ordenar a tabela

	def imprimeTabelaIndices(self):
		for element in self.__tabelaIndices:
			print(element)

	def criaChaveCanonica(self, registro):
		x = registro.split('|')
		chavePrimaria = x[0] + x[4]
		chavePrimaria = chavePrimaria.upper().replace(' ', '')
		return chavePrimaria

	# B: destrutor
	def __del__(self):
		# arquivo de indices
		# gravar a tabela no arquivo, fecha o arquivo
		self.__arquivoIdxPrimario.seek(0)
		for i in range(0, len(self.__tabelaIndices)):
			self.__arquivoIdxPrimario.write(f"{self.__tabelaIndices[i][0]} {self.__tabelaIndices[i][1]}\n")
		# fecha o arquivo de dados
		self.__arquivoDados.close()
		self.__arquivoIdxPrimario.close()

	# C: Insercao (registro)
	def insereRegistro(self, registro):
		chaveRegistro = self.criaChaveCanonica(registro) # calcular chave primaria do registro
		achou = self.pesquisaRegistro(chaveRegistro) # procurar na tabela (RAM) se a chave ja existe
		self.__arquivoDados.seek(0)
		primeiraLinha = [int(x) for x in re.findall(r'-?\d+\.*', self.__arquivoDados.readlines()[0])] # Regex para extrair apenas os numeros da primeira linha -> REG.N e TOP (-?\d = encontra tanto numeros negativos quanto positivos, \.* procura mais de um match)
		if achou == None:
			if primeiraLinha[1] == -1: # verificar se tem espaco vago no arquivo (header, TOP)
				# RNN <- se nao tiver: append
				self.__arquivoDados.write(f"\n{registro}")
				self.__tabelaIndices.append((chaveRegistro, primeiraLinha[0]))
				primeiraLinha[0] = primeiraLinha[0] + 1
				self.__tabelaIndices.sort(key=lambda a: a[0]) # ordenar a tabela
			else:
				# RNN <- se tiver espaco vago: reuso
				# index = [int(x) for x in re.findall(r'-?\d+\.*', self.__tabelaIndices) if x == 14] # Regex para extrair o numero a ser novo TOP (tem formas mais simples mas queria brincar com regex)
				index = [x for x in range(0, len(self.__tabelaIndices)) if int(self.__tabelaIndices[x][1]) == 14]
				self.__tabelaIndices[index] = registro
				self.__arquivoDados.write(f"\n{registro}")
				# Atualizacao da primeiraLinha:
				primeiraLinha[0] = primeiraLinha[0] + 1
				primeiraLinha[1] = index[0]
				self.__tabelaIndices.sort(key=lambda a: a[0])
		else:
			print(f"{registro} already exist in the data base\n")
		#       reordena a tabela

	def removerRegistro(self, chave):
		achou = self.pesquisaRegistro(chave)
		if achou == None:
			return
		else:
			achou = achou.replace(achou[:len(str(firstLine[1])) + 2], f"*{firstLine[1]}|") # sobrescreve o registro a ser "removido" (replace com um parametro ja sendo o nome com a quantia correta de bytes a ser sobrescrito)
        firstLine[1] = find[1]
        firstLine[0] = firstLine[0] - 1
	# D: Pesquisa (chave)
	def pesquisaRegistro(self, chave):
		self.__arquivoDados.seek(0)
		# confere na tabela (chave == alguem?), busca binaria
		for i in range(0, len(self.__tabelaIndices)):
			# se existe na tabela (chave, RRN)
			if chave == self.__tabelaIndices[i][0]:
				# vai no arquivo de dados (RRN) retorna o registro
				registro = self.__arquivoDados.readlines()[int(self.__tabelaIndices[i][1]) + 1]
				return registro
		return None