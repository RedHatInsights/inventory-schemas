# Cloud Platform Inventory Schemas #

This is a place to store API specifications and schemas for the [Host Inventory]. Currently it is used only for [System
Profile].

This is an initial draft and any technical details may change over time. Published early to allow work and discussion on
the actual System Profile shape.

## Technical Details ##

[System Profile] specification is written in YAML containing an [OpenAPI 3.0](https://swagger.io/specification/) definition schema. All entities are under _$def_ root key, internal references (_$ref_) use relative referencing (_#/$def/entity_).

Document version is reflected in the filename (_v1.yaml_) and under _$version_ root key. _$id_ is a file name used in
the Host Inventory.

## Contributing ##

### System Profile ###

When contributing a new field to the system_profile schema, please ensure you complete the following steps:

1. Add the new field
2. Annotate the field
    - Add an example of the value(s) you expect to receive using the `example` keyword.
    - Add a description of the field. If the field should support `range` or `wildcard` operations when queried against, note that here.
3. Add filtering flags
    - If the field should NOT be indexed for filtering, add `x-indexed: false`. Defaults to `true` otherwise.
    - If the field should support wildcard operations in filtering, add `x-wildcard: true`. Defaults to `false` otherwise.
4. Validate the field
    - The field should have the strictest possible validation rules applied to it.
5. Add positive and negative test examples
    - Add examples of valid/invalid values in `tests/utils/valids` and `tests/utils/invalids` respectively.
6. Mirror the changes in HBI
    - Open another PR against `insights-host-inventory` and reflect the schema changes there.

## Process For Merging Schema Changes ##

1. Once a pull request is opened to update a pre-existing field and all the requested changes are resolved, someone from [RedHatInsights/host-based-inventory-comitters team](https://github.com/orgs/RedHatInsights/teams/host-based-inventory-committers) should open a merge request with [App-SRE](https://gitlab.cee.redhat.com/service/app-interface/-/tree/master/data/services/insights/host-inventory/queries) to query the database for potential impact to the HBI reporters.

2. The repository maintainers will analyze the data returned from the App-SRE job, produce a report similar to to the following, and post it in the pull request thread.

    | Reporters | Result | Count |
    | --- | --- | --- |
    | ingress | Pass | 10 |
    | ingress | Fail | 2 |
    | puptoo | Pass | 37 |
    | puptoo | Fail | 42 |

3. If the report seems satisfactory and there are no more concerns, a repository maintainer will merge the PR.

4. In the event that the report is unsatisfactory (e.g. it shows a high number of failures from one or multiple reporters), the PR owner must coordinate with the repository maintainers and the stakeholders from the reporter(s) that show failures. Together, they must decide whether to change the PR or to update the reporter(s).

5. If the pull request only adds new fields there is no need to generate a report since the database will not contain values to compare against for the new fields. A repository maintainer will help in getting consensus with the schema [Stakeholders](#stakeholders) before merging the PR.

6. Once the PR is merged, the HBI team member who merged it can open another PR in the HBI repository to reflect those changes.

### Stakeholders ###

- RHSM - [Kevin Howell](https://github.com/kahowell)
- Yupana - [Chris Duryee](https://github.com/beav)
- Puptoo - [Stephen Adams](https://github.com/stevehnh)
- BU - [Jerome Marc](https://github.com/jeromemarc)

[Host Inventory]: https://github.com/RedHatInsights/insights-host-inventory/
[System Profile]: schemas/system_profile/
[OpenAPI 3.0]: https://swagger.io/specification/
