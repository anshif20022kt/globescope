from typing import List, Optional

from backend.app.models.heritage import (
    HistoricalPlace,
    NationalProfile
)


# ==========================================================
# NATIONAL PROFILE DATA
# ==========================================================

INDIA_PROFILE = NationalProfile(

    country="India",

    states=28,

    union_territories=8,

    national_animal="Bengal Tiger",

    national_bird="Indian Peacock",

    national_flower="Lotus",

    national_tree="Banyan",

    national_emblem="Lion Capital of Ashoka (Sarnath Lion Capital)",

    national_calendar="Saka Calendar"
)


# ==========================================================
# HISTORICAL / HERITAGE PLACES
# ==========================================================

INDIA_HERITAGE_PLACES = [

    HistoricalPlace(
        name="Taj Mahal",
        country="India",
        state="Uttar Pradesh",
        city="Agra",
        category="Mughal Monument",
        description=(
            "A white marble mausoleum in Agra and one of India's "
            "most internationally recognized heritage monuments."
        ),
        unesco_year=1983,
        latitude=27.1751,
        longitude=78.0421,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Red Fort Complex",
        country="India",
        state="Delhi",
        city="New Delhi",
        category="Historic Fort",
        description=(
            "A major Mughal-era fort complex built in the 17th century "
            "as the palace fort of Shahjahanabad."
        ),
        unesco_year=2007,
        latitude=28.6562,
        longitude=77.2410,
        source="UNESCO / Ministry of Culture"
    ),

    HistoricalPlace(
        name="Qutb Minar and its Monuments",
        country="India",
        state="Delhi",
        city="New Delhi",
        category="Historic Monument",
        description=(
            "A historic architectural complex containing the Qutb Minar "
            "and associated monuments in southern Delhi."
        ),
        unesco_year=1993,
        latitude=28.5244,
        longitude=77.1855,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Buddhist Monuments at Sanchi",
        country="India",
        state="Madhya Pradesh",
        city="Sanchi",
        category="Buddhist Heritage",
        description=(
            "A group of Buddhist monuments including stupas, temples, "
            "pillars and monasteries dating from different historical periods."
        ),
        unesco_year=1989,
        latitude=23.4793,
        longitude=77.7397,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Ajanta Caves",
        country="India",
        state="Maharashtra",
        city="Aurangabad region",
        category="Rock-Cut Heritage",
        description=(
            "A group of Buddhist rock-cut caves famous for their "
            "ancient paintings, sculptures and architectural features."
        ),
        unesco_year=1983,
        latitude=20.5519,
        longitude=75.7033,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Ellora Caves",
        country="India",
        state="Maharashtra",
        city="Aurangabad region",
        category="Rock-Cut Heritage",
        description=(
            "A major rock-cut complex containing Buddhist, Hindu and "
            "Jain monuments constructed across several centuries."
        ),
        unesco_year=1983,
        latitude=20.0268,
        longitude=75.1780,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Group of Monuments at Hampi",
        country="India",
        state="Karnataka",
        city="Hampi",
        category="Historic City",
        description=(
            "The remains of the capital of the Vijayanagara Empire, "
            "including temples, royal structures, fortifications and water systems."
        ),
        unesco_year=1986,
        latitude=15.3350,
        longitude=76.4600,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Sun Temple, Konark",
        country="India",
        state="Odisha",
        city="Konark",
        category="Temple Architecture",
        description=(
            "A monumental temple complex designed in the form of "
            "the chariot of the Sun God."
        ),
        unesco_year=1984,
        latitude=19.8876,
        longitude=86.0945,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Group of Monuments at Mahabalipuram",
        country="India",
        state="Tamil Nadu",
        city="Mahabalipuram",
        category="Temple Architecture",
        description=(
            "A group of historic monuments and temples associated "
            "with the Pallava period along the Coromandel Coast."
        ),
        unesco_year=1984,
        latitude=12.6169,
        longitude=80.1920,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Fatehpur Sikri",
        country="India",
        state="Uttar Pradesh",
        city="Fatehpur Sikri",
        category="Historic City",
        description=(
            "A historic Mughal city built during the reign of "
            "Emperor Akbar in the 16th century."
        ),
        unesco_year=1986,
        latitude=27.0945,
        longitude=77.6679,
        source="UNESCO"
    ),

    HistoricalPlace(
        name="Archaeological Site of Nalanda Mahavihara",
        country="India",
        state="Bihar",
        city="Nalanda",
        category="Ancient University",
        description=(
            "An archaeological site associated with the ancient "
            "Nalanda Mahavihara monastic and educational institution."
        ),
        unesco_year=2016,
        latitude=25.1368,
        longitude=85.4439,
        source="UNESCO"
    )
]


# ==========================================================
# NATIONAL PROFILE
# ==========================================================

def get_national_profile(
    country_name: str
) -> Optional[NationalProfile]:

    if country_name.lower() == "india":

        return INDIA_PROFILE

    return None


# ==========================================================
# HERITAGE PLACES
# ==========================================================

def get_heritage_places(
    country_name: str
) -> Optional[List[HistoricalPlace]]:

    if country_name.lower() == "india":

        return INDIA_HERITAGE_PLACES

    return None