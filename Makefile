.PHONY: build open run

run: build open
	python3 -m http.server

open:
	open "http://0.0.0.0:8000/src/generated_html/"

build:
	python3 convert_dot_files_into_website.py
