import pytest
from pydantic import ValidationError

from .models import Farm, crops


@pytest.mark.parametrize("crop", crops)
def test_valid_crops(crop):
    farm = Farm(id=1, crop=crop)
    assert farm.crop == crop


@pytest.mark.parametrize("invalid", [None, "", "chocolate"])
def test_invalid_crop(invalid):
    with pytest.raises(ValidationError):
        Farm(id=1, crop=invalid)
