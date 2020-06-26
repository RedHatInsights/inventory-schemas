# Cloud Platform Inventory Schemas #

This is a place to store API specifications and schemas for the [Host Inventory]. Currently it is used only for [System
Profile].

This is an initial draft and any technical details may change over time. Published early to allow work and discussion on
the actual System Profile shape.

## Technical Details ##

[System Profile] specification is written in YAML containing a [JSON Schema]. All entities are under _$def_ root key, internal references (_$ref_) use relative referencing (_#/$def/entity_).

Document version is reflected in the filename (_v1.yaml_) and under _$version_ root key. _$id_ is a file name used in
the Host Inventory.

## To do ##

- [ ] Write more to do items


[Host Inventory]: https://github.com/RedHatInsights/insights-host-inventory/
[System Profile]: schemas/system_profile/
[JSON Schema]: https://json-schema.org/
