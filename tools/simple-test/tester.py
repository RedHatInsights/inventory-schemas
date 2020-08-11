from sys import argv

from json import load as json_load
from jsonschema import validate as jsonschema_validate
from yaml import safe_load as yaml_safe_load

schema_path = argv[1]
sample_path = argv[2]

with open(sample_path, 'r') as sample_data:
    with open(schema_path, 'r') as schema_data:
        schema_dict = yaml_safe_load(schema_data)
        sample_dict = json_load(sample_data)
        jsonschema_validate(instance=sample_dict, schema=schema_dict)
