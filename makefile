all:
	touch thesis.out
	rm thesis.out
	touch thesis.bbl
	rm thesis.bbl
	touch thesis.aux
	rm thesis.aux
	pdflatex thesis.tex
	bibtex thesis.aux
	pdflatex thesis.tex
	pdflatex thesis.tex
