default:
	@echo "\"make upload\"?"

README: README.md
	pandoc README.md -o README
	python setup.py check -r -s || exit 1

upload: setup.py README
	python setup.py sdist upload --sign

clean:
	rm -f README
