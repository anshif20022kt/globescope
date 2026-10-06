from typing import List, Optional

from backend.app.models.leadership import CountryLeader


# ==========================================================
# INDIA LEADERSHIP
# ==========================================================

INDIA_LEADERS = [

    CountryLeader(
        country="India",
        title="Prime Minister",
        name="Narendra Modi",
        role="Prime Minister of India",
        image=(
            "https://www.pmindia.gov.in/"
            "wp-content/uploads/2025/12/02.jpg"
        ),
        since="9 June 2024",
        description=(
            "Narendra Modi took oath as Prime Minister "
            "for a third consecutive term on 9 June 2024."
        ),
        source=(
            "Prime Minister's Office, "
            "Government of India"
        ),
    ),

    CountryLeader(
        country="India",
        title="President",
        name="Droupadi Murmu",
        role="President of India",
        image=(
            "https://commons.wikimedia.org/wiki/Special:FilePath/"
            "Droupadi_Murmu_POI_official_portrait.jpg"
            "?width=600"
        ),
        since="25 July 2022",
        description=(
            "Droupadi Murmu was sworn in as the "
            "15th President of India on 25 July 2022."
        ),
        source=(
            "President's Secretariat, "
            "Government of India"
        ),
    ),

]


# ==========================================================
# LEADER LOOKUP
# ==========================================================

def get_country_leaders(
    country_name: str
) -> Optional[List[CountryLeader]]:

    if not country_name:
        return None

    normalized_name = (
        country_name.strip().lower()
    )

    if normalized_name == "india":
        return INDIA_LEADERS

    return None


# ==========================================================
# BACKWARD COMPATIBILITY
# ==========================================================
# This keeps the old function available in case another
# part of the project still imports get_country_leader().

def get_country_leader(
    country_name: str
) -> Optional[CountryLeader]:

    leaders = get_country_leaders(
        country_name
    )

    if not leaders:
        return None

    return leaders[0]