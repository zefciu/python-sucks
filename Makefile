python-sucks.pdf: python-sucks.latex styles.tex exceptions.tex abc-inherit.tex abc-register.tex inheritance-super.tex inheritance-explicit.tex Makefile
	latex -output-format=pdf python-sucks.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

exceptions.tex: exceptions.py Makefile
	pygmentize -l py -o exceptions.tex exceptions.py

abc-inherit.tex: abc-inherit.py Makefile
	pygmentize -l py -o abc-inherit.tex abc-inherit.py

abc-register.tex: abc-register.py Makefile
	pygmentize -l py -o abc-register.tex abc-register.py

inheritance-super.tex: inheritance-super.py Makefile
	pygmentize -l py -o inheritance-super.tex inheritance-super.py

inheritance-explicit.tex: inheritance-explicit.py Makefile
	pygmentize -l py -o inheritance-explicit.tex inheritance-explicit.py
