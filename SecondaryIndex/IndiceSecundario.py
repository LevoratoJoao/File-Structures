class IndiceSecundario:

	# atributos da tabela de indice secundario
	__arquivoDados = None
	__arquivoIndicePrimario = None
	__arquivoIndiceSecundario = None
	__tabelaIndiceSecundario = list() 
	__tabelaIndicePrimario = list()

	# construtor da ed
	def __init__(self, campo, arquivo=None):
	
		#  Abrir o arquivo de dados (sempre ecxiste!)
		self.__arquivoDados = open("arqDados.txt", "r+")
		# Inicializacao 01: estrutura vazia
		# se arquivo for = None: tenho estrutura vazia, 
		# iniciar uma estrutura do zero
		#	1. Criar arquivo temporario Primario e Secundario
		#	2. percorrer o arquivo de dados (registro)
		# 		2.a) montar a chave secundaria
		#       2.b) montar a chave primaria
		#       2.c) RRN / byte offset
		#       idx primario -> (chave primaria, RRN)
		#       idx secundario -> (chave secundaria, chave primaria)
		#       2.d) add na tabela Ind Primario, tupla primaria
		#		2.e) add na tabela Ind Secundario, tupla secundaria
		#	3. Ordenar Tabela Ind Primario, com base na chave primaria 
		#   4. Ordernar Tabela Ind Secundario, com base na chave secundaria

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

		pass

	def __del__(self):
		# destrutor (fecha os arquivos)
		#TODO: manter os arquivos temporarios ordenados
		# save da ed
		pass

	def inserirRegistro(self, registro):
		pass

	def removerRegistro(self, chave):
		pass 

	def pesquisarRegistro(self, chaveSecundaria):
		# duas opcoes (achou e nao achou)
		# 1- Nao achou
		# vai procurar a chaveSecundaria na Tabela ind Secu
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

		pass

	def updateRegistro(self, registro):
		pass

	def consultarCabecalho(self):
		# retornar os meta dados do cabecalho
		pass




























