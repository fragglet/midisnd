
DEUTEX=deutex

midisnd.wad : wadinfo.txt
	rm -f $@
	$(DEUTEX) -build wadinfo.txt $@

wadinfo.txt: midisnd.py
	python midisnd.py

