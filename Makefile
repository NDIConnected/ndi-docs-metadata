all : Metadata.pdf

%.pdf : %.md
	pandoc -V geometry:margin=2cm -o $@ -t latex $<
