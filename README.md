# Cloud Platform Inventory Schemas #

This is a place to store API specifications and schemas for the [Host Inventory]. Currently it is used only for [System
Profile].

This is an initial draft and any technical details may change over time. Published early to allow work and discussion on
the actual System Profile shape.

## Technical Details ##

[System Profile] specification is written in YAML containing an [OpenAPI 3.0](https://swagger.io/specification/) definition schema. All entities are under _$def_ root key, internal references (_$ref_) use relative referencing (_#/$def/entity_).

Document version is reflected in the filename (_v1.yaml_) and under _$version_ root key. _$id_ is a file name used in
the Host Inventory.


## Process For Merging Schema Changes ##

1. Once a pull request is opened to update a pre-existing field and all the requested changes are resolved, someone from [RedHatInsights/host-based-inventory-comitters team](https://github.com/orgs/RedHatInsights/teams/host-based-inventory-committers) should open a merge request with [App-SRE](https://gitlab.cee.redhat.com/service/app-interface/-/tree/master/data/services/insights/host-inventory/queries) to query the database for potential impact to the HBI reporters.
   
2. The person from HBI team will analyze the data returned from the App-SRE job and produce a report similiar to to the following and post it in the pull request thread.

    | Reporters | Result | Count |
    | --- | --- | --- |
    | ingress | Pass | 10 |
    | ingress | Fail | 2 |
    | puptoo | Pass | 37 |
    | puptoo | Fail | 42 |


3. If the report seems satisfactory and if there are no more concerns, someone from the HBI team will merge the PR.

4. However, in the event that the report is unsatisfactory, e.g. a high number of failures from one or multiple reporters, coordination must happen between the person who opened the PR, the HBI team and the stakeholder from the reporter(s) with the failures. During the conversation a decision must be made whether to change the PR or to update the reporter with the failures.

5. If the pull request was opened to add a new field rather than update a pre-existing one, no report like the one above needs to be generated and someone from the HBI team can merge it if there are no concerns.

6. Once a PR to update the system profile schema is merged, the representative from the HBI team who merged the PR can go ahead and open a PR in the HBI repository to reflect those changes if no such PR has already been opened in the HBI repository.

### Stakeholders ###

* RHSM - [Kevin Howell](https://github.com/kahowell)
* Yupana - [Chris Duryee](https://github.com/beav)
* Puptoo - [Stephen Adams](https://github.com/stevehnh)
* BU - [Jerome Marc](https://github.com/jeromemarc)

## To do ##

- [ ] Write more to do items


[Host Inventory]: https://github.com/RedHatInsights/insights-host-inventory/
[System Profile]: schemas/system_profile/
[OpenAPI 3.0]: https://swagger.io/specification/
