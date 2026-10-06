from typing import List, Optional

from pydantic import BaseModel


class CountryLeader(BaseModel):
    country: str

    title: Optional[str] = None

    name: Optional[str] = None

    role: Optional[str] = None

    image: Optional[str] = None

    since: Optional[str] = None

    description: Optional[str] = None

    source: Optional[str] = None


class CountryLeadership(BaseModel):

    country: str

    leaders: List[CountryLeader]