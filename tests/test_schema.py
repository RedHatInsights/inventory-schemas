from openapi_spec_validator import validate_spec
from jsonschema import Draft4Validator, Draft7Validator, RefResolver
from jsonschema.validators import extend
from jsonschema.exceptions import ValidationError
import pytest
from unittest import TestCase
from yaml import safe_load

from utils.invalids import INVALID_SYSTEM_PROFILES
from utils.valids import VALID_SYSTEM_PROFILES

CustomDraft4Validator = extend(
    Draft4Validator, {"x-propertyNames": Draft7Validator.VALIDATORS.get("propertyNames")}
)

class SystemProfileTests(TestCase):
    def setUp(self):
        super().setUp()

        with open('schemas/system_profile/v1.yaml') as spec_yaml:
            self.specification = safe_load(spec_yaml)
            self.resolver = RefResolver.from_schema(self.specification)

    def test_system_profile_invalids(self):
        for system_profile in INVALID_SYSTEM_PROFILES:
            with self.subTest(system_profile=system_profile):
                with pytest.raises(ValidationError):
                    CustomDraft4Validator(self.specification["$defs"]["SystemProfile"], resolver=self.resolver).validate(system_profile)
    
    def test_system_profile_valids(self):
        for system_profile in VALID_SYSTEM_PROFILES:
            with self.subTest(system_profile=system_profile):
                CustomDraft4Validator(self.specification["$defs"]["SystemProfile"], resolver=self.resolver).validate(system_profile)

