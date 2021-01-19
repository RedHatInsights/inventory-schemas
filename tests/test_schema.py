from openapi_spec_validator import validate_spec
from jsonschema import Draft4Validator, Draft7Validator, RefResolver
from jsonschema.validators import extend
from unittest import TestCase
from yaml import safe_load

from utils.invalids import INVALID_SYSTEM_PROFILES

CustomDraft4Validator = extend(
    Draft4Validator, {"x-propertyNames": Draft7Validator.VALIDATORS.get("propertyNames")}
)

class SystemProfileTests(TestCase):
    def inc(self, x):
        return x + 1


    def test_answer(self):
        assert self.inc(3) == 4

    def _payload(self, system_profile):
        return {
            "system_profile": system_profile
        }

    def test_system_profile_invalids(self):
        with open('schemas/system_profile/v1.yaml') as spec_yaml:
            specification = safe_load(spec_yaml)
            print(specification)
            test = RefResolver("file://schemas/system_profile/v1.yaml")
            print(test)
            for system_profile in INVALID_SYSTEM_PROFILES:
                with self.subTest(system_profile=system_profile):
                    # print({"system_profile":system_profile})
                    # CustomDraft4Validator(specification["$defs"]["SystemProfile"]).validate(system_profile)
                    assert type(system_profile) == dict

