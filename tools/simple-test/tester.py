import yaml
import json
import sys
from jsonschema import validate

schema_path = sys.argv[1]
sample_path = sys.argv[2]

with open(sample_path, 'r') as sample_data:
    with open(schema_path, 'r') as schema_data:
        schema_dict = yaml.safe_load(schema_data)
        sample_dict = json.load(sample_data)
        validate(instance=sample_dict, schema=schema_dict)
