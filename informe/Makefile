BINDIR=bin
TRASH=informe.aux informe.log informe.out informe.toc informe.idx


.PHONY: all clean

all: $(BINDIR)/informe.pdf

# El latex se compila dos veces seguidas, la primera es para que se arme bien el índice.
TEX_PARAMS= -interaction=nonstopmode

informe.pdf: informe.tex
		( pdflatex $(TEX_PARAMS) informe.tex && clear &&\
		pdflatex $(TEX_PARAMS) informe.tex ) || (echo 'ERROR.'&&rm informe.pdf)

$(BINDIR)/informe.pdf: informe.pdf
		@mv informe.pdf $(BINDIR)
		@(xdg-open $(BINDIR)/informe.pdf) || (echo "Abrir el pdf manualmente")

clean:
		rm -f $(BINDIR)/informe.pdf
		rm -f $(TRASH)
