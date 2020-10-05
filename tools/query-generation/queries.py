class SelectQueries:
    def string_max_length(self, field_name, max_length):
        query = f"SELECT reporter, CASE WHEN system_profile_facts->>'{field_name}' is null THEN 'null' WHEN LENGTH(system_profile_facts->>'{field_name}') < {max_length} THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"
        return query

    def string_match_regex(self, field_name, regex_pattern):
        query = f"SELECT reporter, CASE WHEN system_profile_facts->>'{field_name}' is null THEN 'n/a' WHEN (system_profile_facts->>'{field_name}') ~ '{regex_pattern}' THEN 'pass' ELSE 'fail' END case_result, count(id) FROM hosts GROUP BY reporter, case_result;"
        return query
