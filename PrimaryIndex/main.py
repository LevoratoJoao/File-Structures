#------------------------------------------------------
#------------------------------------------------------

from primaryIndex import IndicePrimario

#------------------------------------------------------
# funcao main no python
#------------------------------------------------------

if __name__ == "__main__":
	print("oi")

	estrutura = IndicePrimario()
	# construtor 
	achou = estrutura.pesquisaRegistro("ARMA32013")
	print(achou)
	estrutura.insereRegistro("Borderlands 2|Gearbox Software|RPG|Multiplataforma|2020|Mature 17+|119.90|Ambos|94.38")

	# destruir (chamado implicitamente pelo python)

#------------------------------------------------------
#------------------------------------------------------
