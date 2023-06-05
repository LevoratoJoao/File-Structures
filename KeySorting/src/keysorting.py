from Herois import Heroi
import sortAlgorithm as sort
import sys

def leituraDelimitador(f, heroi):
	for line in f.readlines()[1:]:
		reading = line.strip().split("|")
		try:
			chave = reading[0]
			primeiroNome =  reading[1]
			sobrenome = reading[2]
			nomeHeroi = reading[3]
			poder = reading[4]
			fraqueza = reading[5]
			cidade = reading[6]
			profissao = reading[7]
		except IndexError:
				print(f"\nError: IndexError at game {reading}\nThe wrong parameter of this game will be set as None in the data base\n")
				chave, primeiroNome, sobrenome, nomeHeroi, poder, fraqueza, cidade, profissao = None, None, None, None, None, None, None, None
		heroi.append(Heroi(int(chave), primeiroNome, sobrenome, nomeHeroi, poder, fraqueza, cidade, profissao))
	return heroi

def savingFile(herois, output, firstLine):
	output.write(f"SIZE={firstLine[0]} top={firstLine[1]} QTDE={firstLine[2]} SORT={firstLine[3]} ORDER={firstLine[4]}")
	for heroi in herois:
		output.write(f"\n{heroi}")

def keySorting(firstLine, heroi, output):
	if firstLine[3] == 'Q':
		herois = sort.quickSort(heroi, firstLine[4])
		savingFile(herois, output, firstLine)
	elif firstLine[3] == 'M':
		herois = sort.mergeSort(heroi, firstLine[4])
		savingFile(herois, output, firstLine)
	elif firstLine[3] == 'H':
		herois = sort.heapSort(heroi, firstLine[4])
		savingFile(herois, output, firstLine)
	elif firstLine[3] == 'I':
		herois = sort.insertionSort(heroi, firstLine[4])
		savingFile(herois, output, firstLine)
	elif firstLine[3] == 'H':
		herois = sort.heapSort(heroi, firstLine[4])
		savingFile(herois, output, firstLine)
	elif firstLine[3] == 'B':
		herois = sort.bubbleSort(heroi, firstLine[4])
		savingFile(herois, output, firstLine)
	elif firstLine[3] == 'S':
		herois = sort.selectionSort(heroi, firstLine[4])
		savingFile(herois, output, firstLine)
	else:
		print("Error: invalid sort")
		output.write("Arquivo Invalido!")

def getFirstLine(f):
	firstLine = f.readline().split()
	data = []
	for i in firstLine:
		data.append(i.split('=')[1])
	return data

if __name__ == "__main__":
	path = sys.argv[1]
	out = sys.argv[2]
	try:
		f = open(sys.argv[1], "r")
	except FileNotFoundError:
		print("Error: file does not exist")
		raise FileNotFoundError
	output = open(sys.argv[2], "w")
	firstLine = getFirstLine(f)
	heroi = leituraDelimitador(f, heroi=[])
	if not firstLine:
		print("Error: file is empty")
		output.write("Arquivo Invalido!")
		output.close()
		f.close()
		exit()
	if not heroi:
		print("Error: no data in the file")
		output.write("Arquivo Invalido!")
		output.close()
		f.close()
		exit()
	keySorting(firstLine, heroi, output)
	output.close()
	f.close()