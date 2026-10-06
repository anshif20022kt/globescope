from typing import Optional

from pydantic import BaseModel


class NationalProfile(BaseModel):

    country: str

    states: Optional[int] = None

    union_territories: Optional[int] = None

    national_animal: Optional[str] = None

    national_bird: Optional[str] = None

    national_flower: Optional[str] = None

    national_tree: Optional[str] = None

    national_emblem: Optional[str] = None

    national_calendar: Optional[str] = None


class HistoricalPlace(BaseModel):

    name: str

    country: str

    state: Optional[str] = None

    city: Optional[str] = None

    category: Optional[str] = None

    description: Optional[str] = None

    unesco_year: Optional[int] = None

    latitude: float

    longitude: float

    source: Optional[str] = None