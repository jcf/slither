import pytest
from pydantic import ValidationError

from .models import Farm, crops


def test_valid_crops():
    for crop in crops:
        farm = Farm(id=1, crop=crop)
        assert farm.crop == crop


def test_invalid_crop():
    for invalid in [None, "", "chocolate"]:
        with pytest.raises(ValidationError):
            Farm(id=1, crop=invalid)
