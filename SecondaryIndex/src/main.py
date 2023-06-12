#------------------------------------------------------
#------------------------------------------------------

from IndiceSecundario import IndiceSecundario
import sys
#------------------------------------------------------
# funcao main no python
#------------------------------------------------------

def showTabelas(estrutura):
	print("\n-------------------------\nTABELA INDICE PRIMARIO: \n")
	print(f"{estrutura.showIndicePrimario()}")
	print("\n-------------------------\nTABELA INDICE SECUNDARIO: \n")
	print(f"{estrutura.showIndiceSecundario()}")

if __name__ == "__main__":
	# Exercicio 1 ------------------------------------------------------
	if int(sys.argv[1]) == 1:
		estrutura = IndiceSecundario(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
		showTabelas(estrutura)

	# Exercicio 2 ------------------------------------------------------
	if int(sys.argv[1]) == 2:
		estrutura = IndiceSecundario(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
		estrutura.inserirRegistro("Rocket League|Psyonix|Sports|Multiplataforma|2015|Everyone|Free|Digital|20.0")
		estrutura.inserirRegistro("Celeste|Extremely OK Games|Adventure|Multiplataforma|2018|Everyone|36.99|Digital|1.2")
		estrutura.inserirRegistro("Sifu|Sloclap|Acao e Aventura|Multiplataforma|2022|17+|75.99|Digital|22")
		estrutura.inserirRegistro("Fallout 4|Bethesda Game Studios|RPG|Multiplataforma|2015|Mature 17+|59.99|Ambos|36.23")
		estrutura.inserirRegistro("Arma 3|Bohemia Interactive|Simulacao|PC|2013|Mature 17+|29.99|Digital|40.57")
		estrutura.inserirRegistro("Final Fantasy X/X-2 Hd Remaster|Square Enix|RPG|Multiplataforma|2013|Teen|55.99|Ambos|37.0")
		estrutura.inserirRegistro("Bleach Brave Souls|KlabGames|Action RPG|Multiplataforma|2016|12+|00.00|Digital|5.0")

		showTabelas(estrutura)

	# Exercicio 3 ------------------------------------------------------
	if int(sys.argv[1]) == 3: 
		estrutura = IndiceSecundario(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
		estrutura.removerRegistro("The Binding of Isaac: Rebirth|Nicalis|Roguelike|PC|2014|Mature 17+|27.99|Digital|0.449")
		estrutura.removerRegistro("Bleach Brave Souls|KlabGames|Action RPG|Multiplataforma|2016|12+|00.00|Digital|5.0")
		estrutura.removerRegistro("Squad|Offworld Industries|Indie|PC|2020|Mature 17+|70.49|Digital|74.15")
		estrutura.removerRegistro("Rocket League|Psyonix|Sports|Multiplataforma|2015|Everyone|Free|Digital|20.0")
		estrutura.removerRegistro("Halo 4|343 Industries|FPS|Multiplataforma|2012|Mature 17+|49.00|Ambos|55.0")
		estrutura.removerRegistro("Blasphemous|Team17|Metroidvania|Multiplataforma|2019|Mature+18|57.99|Digital|0.85388")
		estrutura.removerRegistro("Final Fantasy XV|Square Enix|Action RPG|Multiplataforma|2016|Teen|125.00|Ambos|100.0")

		showTabelas(estrutura)

	# Exercicio 4 ------------------------------------------------------
	if int(sys.argv[1]) == 4:
		estrutura = IndiceSecundario(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
		
		estrutura.inserirRegistro("Final Fantasy XV|Square Enix|Action RPG|Multiplataforma|2016|Teen|125.00|Ambos|100.0")
		showTabelas(estrutura)
		
		estrutura.inserirRegistro("Final Fantasy VII Remake|Square Enix|Action RPG|Multiplataforma|2020|Teen|349.00|Ambos|100.0")
		showTabelas(estrutura)
		
		estrutura.inserirRegistro("Halo 5: Guardians|343 Industries|FPS|Xbox One/Series|2015|Teen|99.00|Ambos|60.0")
		showTabelas(estrutura)
		
		estrutura.inserirRegistro("Hollow Knight|Team Cherry|Metroidvania|Multiplataforma|2017|Everyone 10+|24.97|Digital|5.3")
		showTabelas(estrutura)
		
		estrutura.removerRegistro("Fallout 4|Bethesda Game Studios|RPG|Multiplataforma|2015|Mature 17+|59.99|Ambos|36.23")
		showTabelas(estrutura)
		
		estrutura.inserirRegistro("Squad|Offworld Industries|Indie|PC|2020|Mature 17+|70.49|Digital|74.15")
		showTabelas(estrutura)
		
		estrutura.removerRegistro("The Binding of Isaac: Rebirth|Nicalis|Roguelike|PC|2014|Mature 17+|27.99|Digital|0.449")
		showTabelas(estrutura)
		
		estrutura.inserirRegistro("Halo 4|343 Industries|FPS|Multiplataforma|2012|Mature 17+|49.00|Ambos|55.0")
		showTabelas(estrutura)
		
		estrutura.removerRegistro("Little Big Adventure 2|Adeline Software International|Action-adventure|PC|1997|Everyone|24.89|Digital|0.474")
		showTabelas(estrutura)
		
		estrutura.inserirRegistro("The Legend of Zelda: Breath of the Wild|Nintendo|Action-adventure|Switch|2017|Everyone 10+|199.90|Ambos|13.4")
		showTabelas(estrutura)