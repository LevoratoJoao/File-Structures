import sys
import re
import operator

class IndiceSecundario:

	# atributos da tabela de indice secundario

	# construtor da ed
	def __init__(self, dataset=None, arqIdxPrimario = None, arqIdxSecundario = None, arqSaidaDados = None):
		# Metodos:
		### Arquivos
		self.arquivoSaida = open(arqSaidaDados, "w+") # criei um arquivo de saida para não atrapalhar os testes
		if dataset == None or arqIdxPrimario == None or arqIdxSecundario == None or arqSaidaDados == None:
			print("Error: nao foi possivel acessar os arquivos")
			exit()
		self.arquivoDados = open(dataset, "r+")
		self.arquivoIndiceSecundario = open(arqIdxSecundario, "w+")
		self.arquivoIndicePrimario = open(arqIdxPrimario, "w+")
		### Tabelas
		self.tabelaIndiceSecundario = list()
		self.tabelaIndicePrimario = list()
		### Var utils
		self.cabecalho = [int(x) for x in re.findall(r'-?\d+\.*', self.arquivoDados.readline())]
		# Passando dados do arquivo de entrada para o de saida para que as operacoes sejam feitas
		self.arquivoDados.seek(0)
		for line in self.arquivoDados.readlines():
			self.arquivoSaida.write(f"{line}")
		self.arquivoDados.seek(0)
		RRN = 0
		# 2. percorrer o arquivo de dados (registro)
		for line in self.arquivoDados.readlines()[1:]:
			if line[0] != '*':
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
		for i in range(0, len(self.tabelaIndicePrimario)):
			self.arquivoIndicePrimario.write(f"{self.tabelaIndicePrimario[i][0]} {self.tabelaIndicePrimario[i][1]}\n")
			self.arquivoIndiceSecundario.write(f"{self.tabelaIndiceSecundario[i][0]} {self.tabelaIndiceSecundario[i][1]}\n")
		# fecha o arquivo de dados
		self.arquivoDados.close()
		self.arquivoIndicePrimario.close()
		self.arquivoIndiceSecundario.close()
		self.arquivoSaida.close()

	# Atualiza o arquivo de saida conforme dados vão sendo alterados
	def salvaArquivo(self, dados):
		self.arquivoSaida.seek(0)
		self.arquivoSaida.write(f"REG.N={self.cabecalho[0]} TOP={self.cabecalho[1]}\n")
		for i in dados:
			self.arquivoSaida.write(f"{i}")

	# Le os dados do arquivo de saida que contem as alteracoes
	def lerArquivo(self):
		self.arquivoSaida.seek(0)
		data = list(self.arquivoSaida.readlines()[1:])
		return data

	def inserirRegistro(self, registro):
		chaveRegistro = self.criaChaveCanonica(registro)
		busca = self.buscaRegistroPrimario(chaveRegistro) # procurar registro
		if busca == None:
			if self.cabecalho[1] == -1:
				# Adiciona nas tabelas
				self.tabelaIndicePrimario.append((chaveRegistro[0], self.cabecalho[0]))
				self.tabelaIndiceSecundario.append((chaveRegistro[1], chaveRegistro[0]))
				# Atualiza cabecalho
				self.cabecalho[0] = self.cabecalho[0] + 1
				# Ordena tabelas
				self.tabelaIndicePrimario.sort(key=lambda a: a[0])
				self.tabelaIndiceSecundario.sort(key=lambda a: a[0])
				# Carregando na memoria os dados e salvando no arquivo de sainda
				dados = self.lerArquivo()
				dados.append("\n"+registro)
				self.salvaArquivo(dados)
			else:
				dados = self.lerArquivo() # registros do arquivo
				novoTopo = [int(x) for x in re.findall(r'-?\d+\.*', dados[self.cabecalho[1]][0:3])]
				dados[self.cabecalho[1]] = registro
				# Atualizacao da primeiraLinha:
				self.cabecalho[0] = self.cabecalho[0] + 1
				self.cabecalho[1] = novoTopo[0]
				self.salvaArquivo(dados)
				# Atualizacao das tabelas
				self.tabelaIndicePrimario.append((chaveRegistro[0], self.cabecalho[0]))
				self.tabelaIndiceSecundario.append((chaveRegistro[1], chaveRegistro[0]))
				# Ordenacao das tabelas
				self.tabelaIndicePrimario.sort(key=lambda a: a[0])
				self.tabelaIndiceSecundario.sort(key=lambda a: a[0])
		else:
			print(f"{registro} ja existe na base de dados\n")

	def buscaRegistroPrimario(self, chave):
		self.arquivoDados.seek(0)
		# confere na tabela (chave == alguem?), busca binaria
		achou = self.binarySearch(chave[0])
		if achou is not None:
			return self.arquivoDados.readlines()[achou + 1], achou # retorna o registro e o RRN
		else:
			return None

	def removerRegistro(self, chave):
		chaveRegistro = self.criaChaveCanonica(chave)
		busca = self.buscaRegistroPrimario(chaveRegistro) # busca contem o registro e o RRN
		if busca is not None:
			dados = self.lerArquivo()
			# Atualiza o registro (na memoria) com o tamanho a ser alterado no comeco
			dados[busca[1]] = dados[busca[1]].replace(dados[busca[1]][:len(str(self.cabecalho[1])) + 2], f"*{self.cabecalho[1]}|")
			# Procura a chave nas tabelas
			for i in range(0, len(self.tabelaIndicePrimario)):
				if self.tabelaIndicePrimario[i][0] == chaveRegistro[0]:
					indicePrimario = i
				if self.tabelaIndiceSecundario[i][1] == chaveRegistro[0]:
					indiceSecundario = i
			# Remove a chave das tabelas
			self.tabelaIndicePrimario.pop(indicePrimario)
			self.tabelaIndiceSecundario.pop(indiceSecundario)
			# Atualiza o topo
			self.cabecalho[0] = self.cabecalho[0] - 1
			self.cabecalho[1] = busca[1]
			self.salvaArquivo(dados)
		else:
			print(f"Chave {chave} nao existe na base de dados\n")

	def binarySearch(self, chavePrimaria):
		menor = 0
		meio = 0
		maior = len(self.tabelaIndicePrimario) - 1
		while menor <= maior:
			meio = (maior + menor) // 2
			if self.tabelaIndicePrimario[meio][0] < chavePrimaria:
				menor = meio + 1
			elif self.tabelaIndicePrimario[meio][0] > chavePrimaria:
				maior = meio - 1
			else:
				return self.tabelaIndicePrimario[meio][1] # Retorna o RRN
		return None

	def pesquisarRegistro(self, chaveSecundaria):
		registroIguais = []
		# procura todos os registro iguais na tabela indice secundario
		for i in self.tabelaIndiceSecundario:
			if int(i[0]) == int(chaveSecundaria):
				registroIguais.append(i)
		chavePrimaria = []
		# procura na tabela de indice primario os reg da lista de registros iguais
		for i in registroIguais:
			chavePrimaria.append(self.binarySearch(i[1]))
		registrosArquivo = []
		# pegou rrn e procura no arquivo
		for i in chavePrimaria:
			self.arquivoDados.seek(0)
			registrosArquivo.append(self.arquivoDados.readlines()[i + 1])
		return registrosArquivo




























