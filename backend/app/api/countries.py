from fastapi import APIRouter, HTTPException

from backend.app.services.country_service import (
    compare_countries,
    get_border_countries,
    get_country_by_name,
    get_economic_data,
    get_historical_data
)

from backend.app.services.heritage_service import (
    get_heritage_places,
    get_national_profile
)


router = APIRouter(
    prefix="/countries",
    tags=["Countries"]
)


# ==================================================
# COUNTRY COMPARISON
# ==================================================

@router.get("/compare")
def compare_country_data(
    country1: str,
    country2: str
):

    comparison = compare_countries(
        country1,
        country2
    )

    if comparison is None:

        raise HTTPException(
            status_code=404,
            detail="One or both countries not found"
        )

    return comparison


# ==================================================
# NATIONAL & ADMINISTRATIVE PROFILE
# ==================================================

@router.get("/{country_name}/profile")
def get_national_profile_data(
    country_name: str
):

    profile = get_national_profile(
        country_name
    )

    if profile is None:

        raise HTTPException(
            status_code=404,
            detail="National profile not available"
        )

    return profile


# ==================================================
# HISTORICAL / HERITAGE PLACES
# ==================================================

@router.get("/{country_name}/heritage")
def get_heritage_data(
    country_name: str
):

    places = get_heritage_places(
        country_name
    )

    if places is None:

        raise HTTPException(
            status_code=404,
            detail="Heritage data not available"
        )

    return {
        "country": country_name,
        "count": len(places),
        "places": places
    }


# ==================================================
# COUNTRY INFORMATION
# ==================================================

@router.get("/{country_name}")
def get_country(
    country_name: str
):

    country = get_country_by_name(
        country_name
    )

    if country is None:

        raise HTTPException(
            status_code=404,
            detail="Country not found"
        )

    return country


# ==================================================
# BORDER COUNTRIES
# ==================================================

@router.get("/{country_name}/borders")
def get_borders(
    country_name: str
):

    borders = get_border_countries(
        country_name
    )

    if borders is None:

        raise HTTPException(
            status_code=404,
            detail="Country not found"
        )

    return {
        "country": country_name,
        "border_count": len(borders),
        "borders": borders
    }


# ==================================================
# LATEST ECONOMIC DATA
# ==================================================

@router.get("/{country_name}/economy")
def get_economy(
    country_name: str
):

    economic_data = get_economic_data(
        country_name
    )

    if economic_data is None:

        raise HTTPException(
            status_code=404,
            detail="Economic data not found"
        )

    return economic_data


# ==================================================
# HISTORICAL DATA
# ==================================================

@router.get("/{country_name}/history")
def get_history(
    country_name: str
):

    historical_data = get_historical_data(
        country_name
    )

    if historical_data is None:

        raise HTTPException(
            status_code=404,
            detail="Historical data not found"
        )

    return {
        "country": country_name,
        "records": historical_data
    }