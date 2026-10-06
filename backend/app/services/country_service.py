import os

import requests
from dotenv import load_dotenv

from backend.app.models.country import (
    BorderCountry,
    Country,
    EconomicData,
    HistoricalData
)


load_dotenv()


# ==================================================
# API CONFIGURATION
# ==================================================

REST_COUNTRIES_BASE_URL = (
    "https://api.restcountries.com/countries/v5"
)

WORLD_BANK_BASE_URL = (
    "https://api.worldbank.org/v2"
)

API_KEY = os.getenv(
    "REST_COUNTRIES_API_KEY"
)


# ==================================================
# REST COUNTRIES HEADERS
# ==================================================

def get_headers():

    return {
        "Authorization": f"Bearer {API_KEY}"
    }


# ==================================================
# GET COUNTRY BY NAME
# ==================================================

def get_country_by_name(
    country_name: str
):

    if not API_KEY:

        raise RuntimeError(
            "REST_COUNTRIES_API_KEY is not configured"
        )


    url = (
        f"{REST_COUNTRIES_BASE_URL}/names.common/"
        f"{country_name}"
    )


    response = requests.get(
        url,
        headers=get_headers(),
        timeout=10
    )


    if response.status_code != 200:

        return None


    result = response.json()


    countries = (
        result
        .get("data", {})
        .get("objects", [])
    )


    if not countries:

        return None


    data = countries[0]


    country = Country(

        name=data["names"]["common"],

        official_name=data["names"]["official"],

        alpha_2=data["codes"].get(
            "alpha_2"
        ),

        alpha_3=data["codes"].get(
            "alpha_3"
        ),

        capital=(
            data["capitals"][0]["name"]
            if data.get("capitals")
            else None
        ),

        population=data.get(
            "population"
        ),

        area=(
            data["area"]["kilometers"]
            if data.get("area")
            else None
        ),

        region=data.get(
            "region"
        ),

        subregion=data.get(
            "subregion"
        ),

        currency=(
            data["currencies"][0]["name"]
            if data.get("currencies")
            else None
        ),

        currency_code=(
            data["currencies"][0]["code"]
            if data.get("currencies")
            else None
        ),

        languages=[
            language["name"]
            for language in data.get(
                "languages",
                []
            )
        ],

        flag=data.get(
            "flag",
            {}
        ).get("url_png"),

        timezones=data.get(
            "timezones",
            []
        ),

        borders=data.get(
            "borders",
            []
        ),

        latitude=data.get(
            "coordinates",
            {}
        ).get("lat"),

        longitude=data.get(
            "coordinates",
            {}
        ).get("lng"),

        government_type=data.get(
            "government_type"
        )
    )


    return country


# ==================================================
# GET COUNTRY BY ALPHA-3 CODE
# ==================================================

def get_country_by_code(
    alpha_3: str
):

    if not API_KEY:

        raise RuntimeError(
            "REST_COUNTRIES_API_KEY is not configured"
        )


    url = (
        f"{REST_COUNTRIES_BASE_URL}/codes.alpha_3/"
        f"{alpha_3}"
    )


    response = requests.get(
        url,
        headers=get_headers(),
        timeout=10
    )


    if response.status_code != 200:

        return None


    result = response.json()


    countries = (
        result
        .get("data", {})
        .get("objects", [])
    )


    if not countries:

        return None


    return countries[0]


# ==================================================
# GET BORDER COUNTRIES
# ==================================================

def get_border_countries(
    country_name: str
):

    country = get_country_by_name(
        country_name
    )


    if country is None:

        return None


    border_countries = []


    for border_code in country.borders or []:

        data = get_country_by_code(
            border_code
        )


        if data is None:

            continue


        border_country = BorderCountry(

            name=data["names"]["common"],

            alpha_2=data["codes"].get(
                "alpha_2"
            ),

            alpha_3=data["codes"].get(
                "alpha_3"
            ),

            flag=data.get(
                "flag",
                {}
            ).get("url_png")
        )


        border_countries.append(
            border_country
        )


    return border_countries


# ==================================================
# WORLD BANK INDICATOR
# ==================================================

def get_world_bank_indicator(
    country_code: str,
    indicator: str
):

    url = (
        f"{WORLD_BANK_BASE_URL}/country/"
        f"{country_code}/indicator/"
        f"{indicator}"
    )


    params = {
        "format": "json",
        "per_page": 100
    }


    response = requests.get(
        url,
        params=params,
        timeout=15
    )


    if response.status_code != 200:

        return []


    result = response.json()


    if not isinstance(result, list):

        return []


    if len(result) < 2:

        return []


    return result[1]


# ==================================================
# LATEST ECONOMIC DATA
# ==================================================

def get_economic_data(
    country_name: str
):

    country = get_country_by_name(
        country_name
    )


    if country is None:

        return None


    alpha_2 = country.alpha_2


    if not alpha_2:

        return None


    indicators = {

        "gdp":
            "NY.GDP.MKTP.CD",

        "gdp_per_capita":
            "NY.GDP.PCAP.CD",

        "gdp_growth":
            "NY.GDP.MKTP.KD.ZG",

        "inflation":
            "FP.CPI.TOTL.ZG",

        "unemployment":
            "SL.UEM.TOTL.ZS"
    }


    economic_values = {}

    latest_year = None


    for name, indicator in indicators.items():

        data = get_world_bank_indicator(
            alpha_2,
            indicator
        )


        value = None


        for item in data:

            if item.get("value") is not None:

                value = item["value"]


                if latest_year is None:

                    latest_year = int(
                        item["date"]
                    )


                break


        economic_values[name] = value


    return EconomicData(

        country=country.name,

        year=latest_year,

        gdp=economic_values["gdp"],

        gdp_per_capita=economic_values[
            "gdp_per_capita"
        ],

        gdp_growth=economic_values[
            "gdp_growth"
        ],

        inflation=economic_values[
            "inflation"
        ],

        unemployment=economic_values[
            "unemployment"
        ]
    )


# ==================================================
# HISTORICAL DATA
# ==================================================

def get_historical_data(
    country_name: str
):

    country = get_country_by_name(
        country_name
    )


    if country is None:

        return None


    alpha_2 = country.alpha_2


    if not alpha_2:

        return None


    indicators = {

        "population":
            "SP.POP.TOTL",

        "gdp":
            "NY.GDP.MKTP.CD",

        "gdp_per_capita":
            "NY.GDP.PCAP.CD",

        "gdp_growth":
            "NY.GDP.MKTP.KD.ZG",

        "inflation":
            "FP.CPI.TOTL.ZG",

        "unemployment":
            "SL.UEM.TOTL.ZS"
    }


    indicator_data = {}


    for name, indicator in indicators.items():

        data = get_world_bank_indicator(
            alpha_2,
            indicator
        )


        indicator_data[name] = {

            int(item["date"]): item["value"]

            for item in data

            if item.get("value") is not None
        }


    all_years = set()


    for values in indicator_data.values():

        all_years.update(
            values.keys()
        )


    historical_data = []


    for year in sorted(
        all_years,
        reverse=True
    ):

        historical_data.append(
            HistoricalData(

                year=year,

                population=indicator_data[
                    "population"
                ].get(year),

                gdp=indicator_data[
                    "gdp"
                ].get(year),

                gdp_per_capita=indicator_data[
                    "gdp_per_capita"
                ].get(year),

                gdp_growth=indicator_data[
                    "gdp_growth"
                ].get(year),

                inflation=indicator_data[
                    "inflation"
                ].get(year),

                unemployment=indicator_data[
                    "unemployment"
                ].get(year)
            )
        )


    return historical_data
# ==================================================
# COUNTRY COMPARISON
# ==================================================

def compare_countries(
    country1_name: str,
    country2_name: str
):

    country1 = get_economic_data(
        country1_name
    )

    country2 = get_economic_data(
        country2_name
    )


    if country1 is None:

        return None


    if country2 is None:

        return None


    return {
        "country1": country1,
        "country2": country2
    }