*.pdf: Plots_Temperatura.py data.txt
	python Plots_Temperatura.py
data.txt: DifusionTemperatura.c
	gcc DifusionTemperatura.c -o data.out
	./data.out> data.txt
