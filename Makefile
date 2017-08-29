# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python3 -msphinx
SPHINXPROJ    = QISKit SDK
SOURCEDIR     = rst
BUILDDIR      = _build

.PHONY: help generate doc

# # Catch-all target: route all unknown targets to Sphinx using the new
# # "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# %: Makefile
# 	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# .PHONY: doc


%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Dependencies need to be installed on the Anaconda virtual environment.
create_env:
	conda create -y -n QISKitenv python=3

env:
	bash -c "source activate QISKitenv;pip install -U -r requires.txt"

run:
	open ./_build/html/index.html

test:
	pip install -U -r requires.txt
	python3 -m unittest discover -v

doc:
	make html
	make run

clean:
	make clean
