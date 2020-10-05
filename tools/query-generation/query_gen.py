import sys
import yaml
from collections import OrderedDict
from queries import SelectQueries
from datetime import datetime

class Query(str): pass

def query_string_representer(dumper, data):
    return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')


def builder(name, query):    
    config_dict = {
        '$schema': '/app-interface/app-interface-sql-query-1.yml',
        'labels': {},
        'name': f'{name}',
        'namespace': {
            '$ref': '/services/insights/host-inventory/namespaces/host-inventory-prod.yml'
        },
        'identifier': 'host-inventory-prod-readonly',
        'output': 'stdout',
        'query': Query(f'{query}\n')
    }
    return config_dict


def main(argv):
    yaml.add_representer(Query, query_string_representer)
    queries = SelectQueries()
    query = ''

    if len(argv) != 4:
        raise Exception(f'Not enough arguments was provided. Provided: {len(argv)}')
        return
    
    if argv[1] == 'str':
        if argv[2] == 'max_length':
            query = queries.string_max_length(argv[0], int(argv[3]))
        if argv[2] == 'pattern':
            query = queries.string_match_regex(argv[0], argv[3])
    
    if len(query) > 0:
        now = datetime.now()
        output_filename = now.strftime("%Y-%m-%d")+"-list-matches-"+argv[0]
        config_yaml = yaml.dump(builder(output_filename, query), default_flow_style=False, sort_keys=False)

        yaml_file = open('./generated-yamls/test_file.yaml', 'w')
        yaml_file.write('---\n')
        yaml_file.write(config_yaml)
        yaml_file.close()
        print(f"File {output_filename} was generated successfully")

if __name__ == '__main__':
    main(sys.argv[1:])
