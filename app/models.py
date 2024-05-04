from typing import Pattern
from pydantic import BaseModel, PositiveInt, Field

crops = ["barley", "hops", "wheat"]


def list_to_regex(strs: list[str]) -> Pattern:
    f'^({"|".join(strs)})$'


class Farm(BaseModel):
    id: PositiveInt
    crop: str = Field(pattern=list_to_regex(crops))