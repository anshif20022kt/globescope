from typing import List, Optional

from pydantic import BaseModel


# ==========================================================
# BORDER COUNTRY
# ==========================================================

class BorderCountry(BaseModel):
    name: str
    alpha_2: Optional[str] = None
    alpha_3: Optional[str] = None
    flag: Optional[str] = None


# ==========================================================
# ECONOMIC DATA
# ==========================================================

class EconomicData(BaseModel):
    country: str
    year: Optional[int] = None
    gdp: Optional[float] = None
    gdp_per_capita: Optional[float] = None
    gdp_growth: Optional[float] = None
    inflation: Optional[float] = None
    unemployment: Optional[float] = None


# ==========================================================
# HISTORICAL DATA
# ==========================================================

class HistoricalData(BaseModel):
    year: int
    population: Optional[float] = None
    gdp: Optional[float] = None
    gdp_per_capita: Optional[float] = None
    gdp_growth: Optional[float] = None
    inflation: Optional[float] = None
    unemployment: Optional[float] = None


# ==========================================================
# COUNTRY COMPARISON
# ==========================================================

class CountryComparison(BaseModel):
    country1: EconomicData
    country2: EconomicData


# ==========================================================
# COUNTRY
# ==========================================================

class Country(BaseModel):
    name: str
    official_name: Optional[str] = None

    alpha_2: Optional[str] = None
    alpha_3: Optional[str] = None

    capital: Optional[str] = None
    region: Optional[str] = None
    subregion: Optional[str] = None

    population: Optional[int] = None
    area: Optional[float] = None

    currency: Optional[str] = None
    currency_code: Optional[str] = None

    languages: Optional[List[str]] = None

    flag: Optional[str] = None

    timezones: Optional[List[str]] = None
    borders: Optional[List[str]] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    government_type: Optional[str] = None