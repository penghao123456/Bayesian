GIT=git
FILES=__init__.py
PYTHON=python3
ORIGIN=origin

commit:$(FILES)
	-$(GIT) add * .gitignore
	$(GIT) commit

push:commit
	$(GIT) push $(ORIGIN) main
