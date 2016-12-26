all:
	make -C doc doxy html
pdf:
	make -C doc doxy latexpdf
clean:
	rm -rf output
	rm -rf doc/xml
