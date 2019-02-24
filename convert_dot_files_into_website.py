import subprocess
from glob import glob


def main():
    # Load the Graph Page template
    template = open('src/single_graph_template.html').read()

    # For all the DOT files
    dot_files = glob('dot_files/*.dot')
    for dot_file in dot_files:
        # Generate an SVG
        filename = dot_file.split('/')[1].split('.')[0]
        subprocess.call(
            ['dot', '-Tsvg', '-o', f'src/svgs/{filename}.svg', dot_file]
        )

        # Generate an HTML file from the Template
        graph_html = template.replace(
            '{{ svg_file_path }}',
            f'../svgs/{filename}.svg')

        output_file = open(f'src/generated_html/{filename}.html', 'w+')
        output_file.write(graph_html)
        output_file.close()


if __name__ == '__main__':
    main()
