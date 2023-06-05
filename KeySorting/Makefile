test:
	for number in 1 2 3 4 5 6 7 8; do \
		python3 src/keysorting.py tests/inputs/input$$number.txt output$$number.txt ; \
	done

clean:
	rm -rf src/__pycache__
	for number in 1 2 3 4 5 6 7 8; do \
		rm -rf output$$number.txt ; \
	done
