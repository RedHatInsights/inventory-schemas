class SelectQueries:
    def string_max_length(self, field_name, max_length):
        query = f"SELECT reporter, CASE WHEN system_profile_facts->>'{field_name}' is null THEN 'null' WHEN LENGTH(system_profile_facts->>'{field_name}') < {max_length} THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"
        return query

    def string_match_regex(self, field_name, regex_pattern):
        query = f"SELECT reporter, CASE WHEN system_profile_facts->>'{field_name}' is null THEN 'n/a' WHEN (system_profile_facts->>'{field_name}') ~ '{regex_pattern}' THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"
        return query
    
    def arr_query(self, field_name, operation, value):
        if operation == "max-length":
            query = f"SELECT reporter, CASE WHEN system_profile_facts->>'{field_name}' is null THEN 'n/a' WHEN system_profile_facts @? '$.{field_name}[*] ? (@ like_regex \"^.{{0,{value}}}$\")' is true THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"
        if operation == "pattern":
            query = f"SELECT reporter, CASE WHEN system_profile_facts->>'{field_name}' is null THEN 'n/a' WHEN system_profile_facts @? '$.{field_name}[*] ? (@ like_regex \"{value}\")' is true THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"

        return query

    def nested_query(self, path, field_type, operation, value):
        path_objs = path.split('/')
        json_path = "$"

        for i, v in enumerate(path_objs):
            if i == len(path_objs) - 1 and field_type == 'arr':
                json_path += "."+v
            elif i == len(path_objs) - 1 and field_type == 'str':
                continue
            else:
                json_path += "."+v+"[*]"

        regex_exp = ""
        if field_type == 'str':
            if operation == 'max-length':
                regex_exp = f"{json_path} ? (@.{path_objs[-1]} like_regex \"^.{{0,{value}}}$\")"
            else:
                regex_exp = f"{json_path} ? (@.{path_objs[-1]} like_regex \""+value+"\")"

            query = f"SELECT reporter, CASE WHEN system_profile_facts @? '{json_path}.{path_objs[-1]}' is false THEN 'n/a' WHEN system_profile_facts @? '{regex_exp}' is true THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"

        if field_type == 'arr':
            if operation == 'max-length':
                regex_exp = f"{json_path} ? (@ like_regex \"^.{{0,{value}}}$\")"
            else:
                regex_exp = f"{json_path} ? (@ like_regex \""+value+"\")"
            
            query = f"SELECT reporter, CASE WHEN system_profile_facts @? '{json_path}' is false THEN 'n/a' WHEN system_profile_facts @? '{regex_exp}' is true THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"

        