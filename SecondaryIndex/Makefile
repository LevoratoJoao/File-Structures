test:
	for number in 1 2 3 4; do \
		python3 src/main.py $$number database/dataset.txt tests/arqIdxPrimario$$number.txt tests/arqIdxSecundario$$number.txt tests/arqSaidaDados$$number.txt; \
	done

clean:
	rm -rf src/__pycache__
