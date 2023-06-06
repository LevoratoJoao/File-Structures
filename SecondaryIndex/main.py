#------------------------------------------------------
#------------------------------------------------------

from IndiceSecundario import IndiceSecundario

#------------------------------------------------------
# funcao main no python
#------------------------------------------------------

if __name__ == "__main__":

	estrutura = IndiceSecundario("/home/joaolevorato/programacao/File-Structures/SecondaryIndex/tests/exercicio1.txt")
	# construtor
	estrutura.pesquisarRegistro("2015")
	# destruir (chamado implicitamente pelo python)


#------------------------------------------------------
#------------------------------------------------------
