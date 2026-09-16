PYTHON ?= python3

.PHONY: paper verify clean

paper:
	$(PYTHON) scripts/build_paper.py

verify:
	$(PYTHON) code/verify_reproduction.py

clean:
	rm -rf tmp/pdfs
	rm -f paper/main.aux paper/main.log paper/main.out paper/main.toc
