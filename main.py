#!/usr/bin/env python
 
import os
from jinja2 import Environment, FileSystemLoader

# determine the current file path
PATH = os.path.dirname(os.path.abspath(__file__))

# create an environment for the template files
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    # uses the file name of the template, and a dictionary of context variables to render the template using jinja
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
 
def create_index_html():
    # example function to use the context variables to render a template to an output file
    fname = "output.html"
    urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    context = {
        'urls': urls
    }
    #
    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html)

def main():
    # call your function
    create_index_html()
 
########################################
 
if __name__ == "__main__":
    main()