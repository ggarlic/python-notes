out/slides.pdf: slides.tex
	mkdir -p out
	xelatex --output-directory=out slides.tex

view: out/slides.pdf
	open out/slides.pdf

clean:
	rm -rf out
