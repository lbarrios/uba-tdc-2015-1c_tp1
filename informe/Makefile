BINDIR=bin
TRASH=informe.aux informe.log informe.out informe.toc informe.idx informe.fdb_latexmk


.PHONY: all clean

all: $(BINDIR)/informe.pdf

# El latex se compila dos veces seguidas, la primera es para que se arme bien el índice.
TEX_PARAMS= -interaction=nonstopmode
$(BINDIR)/informe.pdf: informe.tex
		( pdflatex $(TEX_PARAMS) informe.tex && clear &&\
		pdflatex $(TEX_PARAMS) informe.tex ) || (echo 'ERROR.'&&rm informe.pdf)
		@mv informe.pdf $(BINDIR)
		@(evince $(BINDIR)/informe.pdf)||(xdg-open $(BINDIR)/informe.pdf)||\
		(xpdf $(BINDIR)/informe.pdf)||(echo "ERROR: Abrir el pdf manualmente")
	
clean:
		rm -f $(BINDIR)/informe.pdf
		rm -f $(TRASH)
