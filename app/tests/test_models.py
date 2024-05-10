import pytest
from pydantic import ValidationError

from app.models import Farm, crops


@pytest.mark.parametrize("crop", crops)
def test_valid_crops(crop: str) -> None:
    farm = Farm(id=1, crop=crop)
    assert farm.crop == crop


@pytest.mark.parametrize("invalid", [None, "", "chocolate"])
def test_invalid_crop(invalid: str) -> None:
    with pytest.raises(ValidationError):
        Farm(id=1, crop=invalid)
