from jinja2 import Environment, FileSystemLoader

import os

template_environment = Environment(
    loader=FileSystemLoader(os.path.abspath('templates')),
)
