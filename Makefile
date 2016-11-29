all:
	make -C doc doxy html
clean:
	rm -rf output
	rm -rf doc/xml
