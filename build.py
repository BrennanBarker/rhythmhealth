import json
from pathlib import Path
from string import Template

content_glob = Path('content').glob('*')

content = {}
for file in content_glob:
    namespace = file.name.split('.')[0]
    with open(file) as f:
        variables = json.load(f)
    for var, val in variables.items():
        content['_'.join([namespace, var])] = val

templates_path = Path('templates')
templates_glob = templates_path.glob('*')

site_path = Path('docs')

for template in templates_glob:
    with open(template) as f:
        template_string = Template(f.read())
    filled_template = template_string.substitute(**content)
    with open(site_path.joinpath(template.name), 'w') as f:
        f.write(filled_template)
