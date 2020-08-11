from sys import argv

from json import load as json_load
from jsonschema import validate as jsonschema_validate
from yaml import safe_load as yaml_safe_load

spec_path = argv[1]
sample_path = argv[2]

with open(sample_path) as sample_data, open(spec_path) as spec_data:
    sample_dict = json_load(sample_data)
    spec_dict = yaml_safe_load(spec_data)

schema_dict = {**spec_dict, "$ref": "#/$defs/SystemProfile"}
jsonschema_validate(instance=sample_dict, schema=schema_dict)
