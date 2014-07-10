forms.pdf: python-sucks.latex styles.tex exceptions.tex Makefile
	latex -output-format=pdf python-sucks.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

exceptions.tex: exceptions.py Makefile
	pygmentize -l py -o exceptions.tex exceptions.py
