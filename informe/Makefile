BINS = informe.pdf
BINDIR = bin


.PHONY: all clean


informe.pdf: informe.tex
		pdflatex $<
		mv $@ $(BINDIR)
		evince $(BINDIR)/$(BINS)
all: $(BINS)

clean:
		rm -f $(BINDIR)/$(BINS)
		rm -f informe.log
		rm -f informe.aux
