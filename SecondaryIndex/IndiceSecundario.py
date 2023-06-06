import os
import re
class IndiceSecundario:

	# atributos da tabela de indice secundario

	# construtor da ed
	def __init__(self, arquivo="None"):
		self.arquivoIndiceSecundario = None
		self.tabelaIndiceSecundario = list()
		self.tabelaIndicePrimario = list()
		#  Abrir o arquivo de dados (sempre ecxiste!)
		self.arquivoDados = open(arquivo, "r+")
		# Inicializacao 01: estrutura vazia
		if os.path.isfile("SecondaryIndex/arqIdxSecundario.txt"):
			self.arquivoIndiceSecundario = open("SecondaryIndex/arqIdxSecundario.txt", "r+")
			self.arquivoIndicePrimario = open("SecondaryIndex/arqIdxPrimario.txt", "a+")
			# Inicializacao 02: estrutura a partir do arquivo
			# caso contrario (arquivo), cria Indice com base no arquivo
			# arquivoTemp (2nd) -> arquivoTemp (1st)
			#	1. abrir o arquivo Temp (2nd)
			#   2. abrir o arquivo Temp (1st)
			#	3. percorrer os arquivos (0:N-1)
			#		linha arq temp 2st (chaveSecundaria, chavePrimaria)
			#			3.a) inserir na tabela Ind Secundario
			#	    linha arq temp 1st (chavePrimaria, RRN)
			#			3.b) inserir na tabela Ind Primario
		else: # iniciar uma estrutura do zero
			#	1. Criar arquivo temporario Primario e Secundario
			self.arquivoIndiceSecundario = open("SecondaryIndex/arqIdxSecundario.txt", "a+")
			self.arquivoIndicePrimario = open("SecondaryIndex/arqIdxPrimario.txt", "a+")
			RRN = 0
			# 2. percorrer o arquivo de dados (registro)
			for line in self.arquivoDados.readlines()[1:]:
				chave = self.criaChaveCanonica(line)
				# 2.a) montar a chave secundaria
				self.tabelaIndiceSecundario.append((chave[1], chave[0])) # 2.e) add na tabela Ind Secundario, tupla secundaria
				# 2.b) montar a chave primaria
				self.tabelaIndicePrimario.append((chave[0], RRN)) # 2.d) add na tabela Ind Primario, tupla primaria
				RRN+=1 # 2.c) RRN / byte offset
			self.tabelaIndicePrimario.sort(key=lambda a: a[0]) # 3. Ordenar Tabela Ind Primario, com base na chave primaria
			self.tabelaIndiceSecundario.sort(key=lambda a: a[0]) # 4. Ordernar Tabela Ind Secundario, com base na chave secundaria

	def criaChaveCanonica(self, registro):
		x = registro.split('|')
		chavePrimaria = x[0] + x[4]
		chavePrimaria = chavePrimaria.upper().replace(' ', '')
		return chavePrimaria, x[4]

	def __del__(self):
		# arquivo de indices
		# gravar a tabela no arquivo, fecha o arquivo
		self.arquivoDados.seek(0)
		self.arquivoIndicePrimario.seek(0)
		self.arquivoIndiceSecundario.seek(0)
		for i in range(0, len(self.tabelaIndicePrimario)):
			self.arquivoIndicePrimario.write(f"{self.tabelaIndicePrimario[i][0]} {self.tabelaIndicePrimario[i][1]}\n")
			self.arquivoIndiceSecundario.write(f"{self.tabelaIndiceSecundario[i][0]} {self.tabelaIndiceSecundario[i][1]}\n")
		# fecha o arquivo de dados
		self.arquivoDados.close()
		self.arquivoIndicePrimario.close()

	def inserirRegistro(self, registro):
		chaveRegistro = self.criaChaveCanonica(registro)
		# TODO: procurar registro
		primeiraLinha = [int(x) for x in re.findall(r'-?\d+\.*', self.arquivoDados.readlines()[0])]
		# TODO: if com achou
		if primeiraLinha[1] == -1:
			self.arquivoDados.write(f"\n{registro}")
			self.tabelaIndicePrimario.append((chaveRegistro[0], primeiraLinha[0]))
			primeiraLinha[0] = primeiraLinha[0] + 1
			self.tabelaIndiceSecundario.append((chaveRegistro[1], chaveRegistro[0]))
			self.tabelaIndicePrimario.sort(key=lambda a: a[0])
			self.tabelaIndiceSecundario.sort(key=lambda a: a[0])
		else:
			pass

	def removerRegistro(self, chave):
		pass

	def pesquisarRegistro(self, chaveSecundaria):
		self.__arquivoDados.seek(0)
		# 1- Nao achou
		# vai procurar a chaveSecundaria na Tabela ind Secu
		if chaveSecundaria in self.tabelaIndiceSecundario:
			#registro = self.arquivoDados.readlines()[int(self.tabelaIndicePrimario[i][1]) + 1]
			return
		else:
			pass
		# Se nao achastes: retornar Falso
		# Senao (existe)
		#	2. Lista com tuplas (1 ou + tuplas)
		#	3. Para cada tupla na lista:
		#		(chavePrim, chaveSec)
		#		3.a) usar chavePrim p descobrir o RRN
		#			consultar na Tabela de Indice Primario
		#		3.b) no arquivo de dados (RRN) -> registro
		#		3.c) add registro em uma lista de retorno
		#	4. retorna os registros (lista)


	def updateRegistro(self, registro):
		pass

	def consultarCabecalho(self):
		# retornar os meta dados do cabecalho
		pass




























