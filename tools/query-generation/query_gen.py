import yaml
from collections import OrderedDict

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

'''
SELECT reporter, 
	CASE
		WHEN system_profile_facts->>'bios_release_date' is null THEN 'null'
		WHEN LENGTH(system_profile_facts->>'bios_release_date') < 7 THEN 'pass'
		ELSE 'fail'
	END case_result, count(id)
FROM hosts GROUP BY reporter, case_result;
'''

'''
SELECT reporter, 
	CASE
		WHEN system_profile_facts->>'os_kernel_version' is null THEN 'n/a'
		WHEN (system_profile_facts->>'os_kernel_version') ~ '^[a-z]' THEN 'pass'
		ELSE 'fail'
	END case_result, count(id)
FROM hosts GROUP BY reporter, case_result;
'''


def main():
    yaml.add_representer(Query, query_string_representer)
    config_yaml = yaml.dump(builder('random', 'SELECT BLAH BLAH BLAH;'), default_flow_style=False, sort_keys=False)

    yaml_file = open('generated-yamls/test_file.yaml', 'w')
    yaml_file.write('---\n')
    yaml_file.write(config_yaml)
    yaml_file.close()

if __name__ == '__main__':
    main()