import requests
import pandas as pd
import streamlit as st
import plotly.express as px
from textwrap import dedent


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="GlobeScope",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

BACKEND_URL = "http://127.0.0.1:8000"


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(
    dedent(
        """
        <style>
        /* =========================
           GLOBAL
        ========================= */
        .stApp {
            background: #0b0f14;
            color: #f8fafc;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        .block-container {
            max-width: 1540px;
            padding-top: 0.75rem;
            padding-bottom: 2rem;
            padding-left: 1.25rem;
            padding-right: 1.25rem;
        }

        [data-testid="stVerticalBlock"] {
            gap: 0.48rem;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #171d27 0%, #10151d 100%);
            border-right: 1px solid #273140;
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 1rem;
        }

        /* =========================
           SIDEBAR
        ========================= */
        .brand {
            padding: 0.15rem 0 1rem 0;
        }

        .brand-title {
            color: #f8fafc;
            font-size: 1.45rem;
            font-weight: 800;
            letter-spacing: -0.035em;
        }

        .brand-subtitle {
            color: #94a3b8;
            font-size: 0.84rem;
            margin-top: -0.1rem;
            padding-left: 1.95rem;
        }

        .sidebar-copy {
            color: #cbd5e1;
            line-height: 1.45;
            font-size: 0.9rem;
        }

        /* =========================
           SECTION HEADINGS
        ========================= */
        .section-heading {
            display: flex;
            align-items: center;
            gap: 0.42rem;
            margin-top: 0.62rem;
            margin-bottom: 0.28rem;
        }

        .section-icon {
            font-size: 1.25rem;
        }

        .section-text {
            color: #f8fafc;
            font-size: 1.08rem;
            font-weight: 800;
            letter-spacing: -0.025em;
        }

        /* =========================
           COUNTRY HEADER
        ========================= */
        .country-title {
            color: #f8fafc;
            font-size: 1.85rem;
            line-height: 1.05;
            font-weight: 850;
            letter-spacing: -0.04em;
        }

        .country-official {
            color: #cbd5e1;
            font-size: 1rem;
            margin-top: 0.22rem;
        }

        .country-meta {
            color: #e2e8f0;
            font-size: 0.91rem;
            line-height: 1.65;
            margin-top: 0.5rem;
        }

        .country-code-line {
            color: #cbd5e1;
            margin-top: 0.2rem;
        }

        /* =========================
           CARDS
        ========================= */
        .card-label {
            color: #94a3b8;
            font-size: 0.77rem;
            font-weight: 650;
        }

        .card-value {
            color: #f8fafc;
            font-size: 1.16rem;
            font-weight: 800;
            line-height: 1.15;
            margin-top: 0.18rem;
        }

        .card-value-large {
            color: #f8fafc;
            font-size: 1.38rem;
            font-weight: 850;
            line-height: 1.15;
            margin-top: 0.15rem;
        }

        .card-secondary {
            color: #94a3b8;
            font-size: 0.78rem;
            margin-top: 0.22rem;
        }

        .symbol-icon {
            font-size: 1.35rem;
            line-height: 1;
            margin-bottom: 0.35rem;
        }

        .symbol-label {
            color: #94a3b8;
            font-size: 0.7rem;
        }

        .symbol-value {
            color: #f8fafc;
            font-size: 0.9rem;
            font-weight: 750;
            margin-top: 0.12rem;
            line-height: 1.2;
        }

        /* =========================
           LEADERSHIP
        ========================= */
        .leader-card-title {
            color: #94a3b8;
            font-size: 0.74rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.045em;
        }

        .leader-name {
            color: #f8fafc;
            font-size: 1.35rem;
            font-weight: 850;
            line-height: 1.05;
            margin-top: 0.12rem;
        }

        .leader-role {
            color: #cbd5e1;
            font-size: 0.88rem;
            margin-top: 0.22rem;
        }

        .leader-since {
            color: #94a3b8;
            font-size: 0.76rem;
            margin-top: 0.3rem;
        }

        .leader-source {
            color: #64748b;
            font-size: 0.67rem;
            margin-top: 0.35rem;
        }

        /* =========================
           COMPACT DASHBOARD CARDS
        ========================= */
        .mini-leader-card {
            border: 1px solid #2b3543;
            border-radius: 12px;
            background: #0f141b;
            padding: 0.6rem;
            min-height: 142px;
        }

        .mini-leader-title {
            color: #94a3b8;
            font-size: 0.64rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .mini-leader-name {
            color: #f8fafc;
            font-size: 0.94rem;
            font-weight: 850;
            line-height: 1.1;
            margin-top: 0.18rem;
        }

        .mini-leader-role {
            color: #cbd5e1;
            font-size: 0.72rem;
            margin-top: 0.18rem;
        }

        .mini-leader-since {
            color: #94a3b8;
            font-size: 0.65rem;
            margin-top: 0.42rem;
        }

        .mini-leader-source {
            color: #64748b;
            font-size: 0.58rem;
            margin-top: 0.35rem;
            line-height: 1.25;
        }

        .symbol-html-card {
            border: 1px solid #2b3543;
            border-radius: 10px;
            background: #0f141b;
            min-height: 96px;
            height: 96px;
            padding: 0.6rem;
            box-sizing: border-box;
        }

        .symbol-html-card .symbol-icon {
            font-size: 1.25rem;
            margin-bottom: 0.28rem;
        }

        .symbol-html-card .symbol-label {
            color: #94a3b8;
            font-size: 0.64rem;
            line-height: 1.1;
        }

        .symbol-html-card .symbol-value {
            color: #f8fafc;
            font-size: 0.78rem;
            font-weight: 800;
            line-height: 1.15;
            margin-top: 0.16rem;
        }

        .compact-country {
            padding-top: 0.25rem;
        }

        .compact-country-flag {
            margin-bottom: 0.38rem;
        }

        .country-hero-card {
            border: 1px solid #273140;
            border-radius: 14px;
            background: linear-gradient(145deg, #101720 0%, #0d1219 100%);
            padding: 0.85rem 0.95rem;
            min-height: 178px;
        }

        .country-hero-card img {
            border-radius: 9px;
        }

        .top-leader-wrap {
            margin-top: 0.1rem;
        }

        .top-leader-card {
            border: 1px solid #273140;
            border-radius: 12px;
            background: #0e141b;
            padding: 0.58rem;
            min-height: 146px;
        }

        .top-leader-card [data-testid="stImage"] {
            margin-top: 0;
        }

        .top-leader-card img {
            border-radius: 9px;
        }

        .top-leader-description {
            color: #94a3b8;
            font-size: 0.68rem;
            line-height: 1.35;
            margin-top: 0.25rem;
        }

        .dashboard-rule {
            height: 1px;
            background: #202a36;
            margin: 0.55rem 0 0.35rem 0;
        }

        /* =========================
           FOOTER
        ========================= */
        .footer {
            border-top: 1px solid #26303d;
            margin-top: 1.2rem;
            padding-top: 1rem;
            text-align: center;
            color: #64748b;
            font-size: 0.72rem;
        }

        /* =========================
           STREAMLIT BUTTONS / INPUTS
        ========================= */
        .stButton > button {
            border-radius: 9px;
            font-weight: 750;
        }

        [data-testid="stMetricLabel"] {
            color: #94a3b8 !important;
        }

        [data-testid="stMetricValue"] {
            color: #f8fafc !important;
        }

        [data-testid="stExpander"] {
            border-color: #273140;
            background: #111720;
        }

        /* Keep cards visually tight */
        div[data-testid="stHorizontalBlock"] {
            gap: 0.65rem;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 10px;
        }

        @media (max-width: 900px) {
            .block-container {
                padding-left: 0.9rem;
                padding-right: 0.9rem;
            }

            .country-title {
                font-size: 1.65rem;
            }
        }
        </style>
        """
    ),
    unsafe_allow_html=True,
)


# ==========================================================
# HELPERS
# ==========================================================

def render_html(content):
    """Render HTML without indentation being interpreted as a code block."""
    st.markdown(dedent(content), unsafe_allow_html=True)


def api_get(endpoint, params=None, timeout=30):
    try:
        response = requests.get(
            f"{BACKEND_URL}{endpoint}",
            params=params,
            timeout=timeout,
        )

        if response.status_code == 200:
            return response.json()

        return None

    except requests.RequestException:
        return None


@st.cache_data(ttl=3600, show_spinner=False)
def load_image_bytes(url):
    """Download remote images before giving them to Streamlit."""
    if not url:
        return None

    try:
        response = requests.get(
            url,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0 GlobeScope/1.0"},
        )
        response.raise_for_status()
        return response.content

    except requests.RequestException:
        return None


def show_image(url, width=150):
    image = load_image_bytes(url)

    if image:
        st.image(image, width=width)
        return True

    return False


def format_large_number(value):
    if value is None:
        return "N/A"

    try:
        value = float(value)

        if value >= 1_000_000_000_000:
            return f"{value / 1_000_000_000_000:.2f}T"

        if value >= 1_000_000_000:
            return f"{value / 1_000_000_000:.2f}B"

        if value >= 1_000_000:
            return f"{value / 1_000_000:.2f}M"

        return f"{value:,.0f}"

    except (ValueError, TypeError):
        return str(value)


def format_currency(value):
    if value is None:
        return "N/A"

    try:
        value = float(value)

        if value >= 1_000_000_000_000:
            return f"${value / 1_000_000_000_000:.2f}T"

        if value >= 1_000_000_000:
            return f"${value / 1_000_000_000:.2f}B"

        if value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"

        return f"${value:,.0f}"

    except (ValueError, TypeError):
        return "N/A"


def section_title(icon, title):
    render_html(
        f"""
        <div class="section-heading">
            <span class="section-icon">{icon}</span>
            <span class="section-text">{title}</span>
        </div>
        """
    )


def metric_card(label, value, icon=None, secondary=None):
    with st.container(border=True):
        if icon:
            render_html(f'<div class="symbol-icon">{icon}</div>')

        render_html(
            f"""
            <div class="card-label">{label}</div>
            <div class="card-value-large">{value}</div>
            """
        )

        if secondary:
            render_html(
                f'<div class="card-secondary">{secondary}</div>'
            )


def symbol_card(icon, label, value):
    render_html(
        f"""
        <div class="symbol-html-card">
            <div class="symbol-icon">{icon}</div>
            <div class="symbol-label">{label}</div>
            <div class="symbol-value">{value or "N/A"}</div>
        </div>
        """
    )


# ==========================================================
# INDIA LEADERSHIP FALLBACK
# ==========================================================
# Your current FastAPI /leader endpoint returns 404.
# The frontend therefore keeps India leadership available
# until the backend route is repaired.

INDIA_LEADERS = [
    {
        "country": "India",
        "title": "Prime Minister",
        "name": "Narendra Modi",
        "role": "Prime Minister of India",
        "since": "9 June 2024",
        "description": (
            "Took oath as Prime Minister for a third consecutive term "
            "on 9 June 2024."
        ),
        "image": (
            "https://commons.wikimedia.org/wiki/Special:FilePath/"
            "The_official_portrait_of_Shri_Narendra_Modi%2C_"
            "the_Prime_Minister_of_the_Republic_of_India.jpg"
        ),
        "source": "Prime Minister's Office, Government of India",
    },
    {
        "country": "India",
        "title": "President",
        "name": "Droupadi Murmu",
        "role": "President of India",
        "since": "25 July 2022",
        "description": (
            "Sworn in as the 15th President of India on 25 July 2022."
        ),
        "image": (
            "https://commons.wikimedia.org/wiki/Special:FilePath/"
            "Droupadi_Murmu_POI_official_portrait.jpg?width=600"
        ),
        "source": "President's Secretariat, Government of India",
    },
]


def get_leadership(country_name):
    """
    Prefer the backend endpoint.
    If it is unavailable, use the India fallback.
    """
    backend_leader = api_get(
        f"/countries/{country_name}/leader"
    )

    if backend_leader:
        if isinstance(backend_leader, list):
            return backend_leader

        if isinstance(backend_leader, dict):
            return [backend_leader]

    if country_name.strip().lower() == "india":
        return INDIA_LEADERS

    return []


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    render_html(
        """
        <div class="brand">
            <div class="brand-title">🌍 GlobeScope</div>
            <div class="brand-subtitle">Country Intelligence</div>
        </div>
        """
    )

    st.markdown("### Explore")

    render_html(
        """
        <div class="sidebar-copy">
            Search for a country to explore its geography,
            culture, economy and history.
        </div>
        """
    )

    country_input = st.text_input(
        "Country name",
        value="India",
        placeholder="e.g. India, Japan, Canada",
        key="country_input",
    )

    search_button = st.button(
        "🔎 Search Country",
        use_container_width=True,
        type="primary",
    )

    st.divider()

    view_mode = st.radio(
        "View Mode",
        ["Country Details", "Compare Countries"],
        index=0,
    )

    if view_mode == "Country Details":
        st.caption("Explore a single country")
    else:
        st.caption("Compare two countries")

    st.divider()

    st.markdown("### Navigation")
    st.write("🌍 Home")
    st.write("ℹ️ About")
    st.write("📚 Data Sources")
    st.write("◉ GitHub")

    st.caption(
        "Powered by FastAPI + REST Countries + World Bank"
    )


# ==========================================================
# COUNTRY STATE
# ==========================================================

if "country" not in st.session_state:
    st.session_state.country = None

if "country_name" not in st.session_state:
    st.session_state.country_name = "India"


if search_button:

    requested_country = country_input.strip()

    if not requested_country:
        st.error("Please enter a country name.")
        st.stop()

    with st.spinner(f"Loading {requested_country}..."):

        result = api_get(
            f"/countries/{requested_country}"
        )

    if result:

        st.session_state.country = result
        st.session_state.country_name = requested_country

    else:

        st.error(
            "Country not found or FastAPI is not running. "
            "Please check the country name and backend."
        )
        st.stop()


if st.session_state.country is None:

    with st.spinner("Loading India..."):

        initial = api_get(
            "/countries/India"
        )

    if initial:

        st.session_state.country = initial
        st.session_state.country_name = "India"

    else:

        st.error(
            "GlobeScope could not connect to FastAPI. "
            "Run: uvicorn backend.app.main:app --reload"
        )
        st.stop()


country = st.session_state.country

country_name = country.get(
    "name",
    st.session_state.country_name,
)


# ==========================================================
# COMPARISON MODE
# ==========================================================

if view_mode == "Compare Countries":

    section_title(
        "⚖️",
        "Country Comparison",
    )

    st.caption(
        "Compare two countries side by side using the latest available "
        "economic indicators."
    )

    # ------------------------------------------------------
    # COUNTRY SELECTION
    # ------------------------------------------------------

    with st.container(border=True):

        c1, c2 = st.columns(
            2,
            gap="medium",
        )

        with c1:

            comparison_country1 = st.text_input(
                "Country 1",
                value="India",
                placeholder="e.g. India",
                key="comparison_country1",
            )

        with c2:

            comparison_country2 = st.text_input(
                "Country 2",
                value="Japan",
                placeholder="e.g. Japan",
                key="comparison_country2",
            )

        compare_button = st.button(
            "⚖️ Compare Countries",
            use_container_width=True,
            type="primary",
            key="run_comparison",
        )


    # ------------------------------------------------------
    # RESULTS
    # ------------------------------------------------------

    if compare_button:

        if not comparison_country1.strip() or not comparison_country2.strip():

            st.warning(
                "Please enter both country names."
            )
            st.stop()

        with st.spinner("Comparing countries..."):

            comparison = api_get(
                "/countries/compare",
                params={
                    "country1": comparison_country1.strip(),
                    "country2": comparison_country2.strip(),
                },
            )

            country1_info = api_get(
                f"/countries/{comparison_country1.strip()}"
            )

            country2_info = api_get(
                f"/countries/{comparison_country2.strip()}"
            )

        if not comparison:

            st.error(
                "Could not compare the selected countries. "
                "Check the country names and make sure FastAPI is running."
            )

        else:

            data1 = comparison.get("country1")
            data2 = comparison.get("country2")

            if not data1 or not data2:

                st.error(
                    "The comparison response did not contain both countries."
                )

            else:

                name1 = data1.get(
                    "country",
                    comparison_country1,
                )

                name2 = data2.get(
                    "country",
                    comparison_country2,
                )

                # --------------------------------------------------
                # COUNTRY HEADERS
                # --------------------------------------------------

                section_title(
                    "🌍",
                    "Countries",
                )

                left, right = st.columns(
                    2,
                    gap="medium",
                )

                with left:

                    with st.container(border=True):

                        flag1 = (
                            country1_info or {}
                        ).get("flag")

                        if flag1:

                            show_image(
                                flag1,
                                width=90,
                            )

                        st.subheader(
                            name1
                        )

                        official1 = (
                            country1_info or {}
                        ).get(
                            "official_name"
                        )

                        if official1:

                            st.caption(
                                official1
                            )

                        code1 = (
                            country1_info or {}
                        ).get("alpha_3")

                        if code1:

                            st.caption(
                                f"Code: {code1}"
                            )

                with right:

                    with st.container(border=True):

                        flag2 = (
                            country2_info or {}
                        ).get("flag")

                        if flag2:

                            show_image(
                                flag2,
                                width=90,
                            )

                        st.subheader(
                            name2
                        )

                        official2 = (
                            country2_info or {}
                        ).get(
                            "official_name"
                        )

                        if official2:

                            st.caption(
                                official2
                            )

                        code2 = (
                            country2_info or {}
                        ).get("alpha_3")

                        if code2:

                            st.caption(
                                f"Code: {code2}"
                            )


                # --------------------------------------------------
                # SIDE-BY-SIDE ECONOMIC SNAPSHOT
                # --------------------------------------------------

                section_title(
                    "📊",
                    "Economic Snapshot",
                )

                metrics = [
                    (
                        "GDP",
                        "gdp",
                        lambda x: format_currency(x),
                    ),
                    (
                        "GDP per Capita",
                        "gdp_per_capita",
                        lambda x: (
                            f"${float(x):,.0f}"
                            if x is not None
                            else "N/A"
                        ),
                    ),
                    (
                        "GDP Growth",
                        "gdp_growth",
                        lambda x: (
                            f"{float(x):.2f}%"
                            if x is not None
                            else "N/A"
                        ),
                    ),
                    (
                        "Inflation",
                        "inflation",
                        lambda x: (
                            f"{float(x):.2f}%"
                            if x is not None
                            else "N/A"
                        ),
                    ),
                    (
                        "Unemployment",
                        "unemployment",
                        lambda x: (
                            f"{float(x):.2f}%"
                            if x is not None
                            else "N/A"
                        ),
                    ),
                ]

                for label, key, formatter in metrics:

                    col1, col2 = st.columns(
                        2,
                        gap="medium",
                    )

                    with col1:

                        with st.container(
                            border=True
                        ):

                            render_html(
                                f"""
                                <div class="card-label">
                                    {name1} · {label}
                                </div>
                                <div class="card-value-large">
                                    {formatter(data1.get(key))}
                                </div>
                                """
                            )

                    with col2:

                        with st.container(
                            border=True
                        ):

                            render_html(
                                f"""
                                <div class="card-label">
                                    {name2} · {label}
                                </div>
                                <div class="card-value-large">
                                    {formatter(data2.get(key))}
                                </div>
                                """
                            )


                # --------------------------------------------------
                # COMPARISON TABLE
                # --------------------------------------------------

                section_title(
                    "📋",
                    "Indicator Table",
                )

                table_rows = []

                for label, key, formatter in metrics:

                    table_rows.append(
                        {
                            "Indicator": label,
                            name1: formatter(
                                data1.get(key)
                            ),
                            name2: formatter(
                                data2.get(key)
                            ),
                        }
                    )

                comparison_df = pd.DataFrame(
                    table_rows
                )

                st.dataframe(
                    comparison_df,
                    hide_index=True,
                    use_container_width=True,
                )


                # --------------------------------------------------
                # VISUAL COMPARISON
                # --------------------------------------------------

                section_title(
                    "📈",
                    "Visual Comparison",
                )

                metric_options = {
                    "GDP": "gdp",
                    "GDP per Capita": "gdp_per_capita",
                    "GDP Growth": "gdp_growth",
                    "Inflation": "inflation",
                    "Unemployment": "unemployment",
                }

                selected_metric = st.selectbox(
                    "Select comparison metric",
                    list(
                        metric_options.keys()
                    ),
                    key="comparison_metric",
                )

                metric_key = metric_options[
                    selected_metric
                ]

                chart_data = pd.DataFrame(
                    {
                        "Country": [
                            name1,
                            name2,
                        ],
                        "Value": [
                            data1.get(
                                metric_key
                            ),
                            data2.get(
                                metric_key
                            ),
                        ],
                    }
                ).dropna()

                if not chart_data.empty:

                    fig = px.bar(
                        chart_data,
                        x="Country",
                        y="Value",
                        text_auto=".2s",
                        title=selected_metric,
                    )

                    fig.update_layout(
                        template="plotly_dark",
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        margin=dict(
                            l=20,
                            r=20,
                            t=55,
                            b=20,
                        ),
                        xaxis_title=None,
                        yaxis_title=selected_metric,
                        hovermode="x unified",
                    )

                    fig.update_traces(
                        textposition="outside",
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True,
                        config={
                            "displayModeBar": True,
                        },
                    )

                else:

                    st.info(
                        f"No data is available for {selected_metric}."
                    )


# ==========================================================
# COUNTRY DETAILS
# ==========================================================

else:

    # ------------------------------------------------------
    # TOP HERO: COUNTRY IDENTITY + LEADERSHIP
    # ------------------------------------------------------

    left, right = st.columns(
        [1.0, 1.45],
        gap="medium",
    )

    with left:

        with st.container(border=True):

            hero_left, hero_info = st.columns(
                [0.62, 1.55],
                gap="medium",
            )

            with hero_left:
                flag = country.get("flag")
                if flag:
                    show_image(flag, width=105)

            with hero_info:
                render_html(
                    f"""
                    <div class="country-title">
                        🌍 {country.get("name", "Unknown Country")}
                    </div>
                    <div class="country-official">
                        {country.get("official_name", "N/A")}
                    </div>
                    <div class="country-meta">
                        🏛️ <b>Government:</b>
                        {country.get("government_type") or "N/A"}
                    </div>
                    <div class="country-code-line">
                        🔤 <b>Code:</b>
                        {country.get("alpha_2") or "N/A"} /
                        {country.get("alpha_3") or "N/A"}
                    </div>
                    """
                )

    with right:

        leaders = get_leadership(country_name)

        section_title(
            "👤",
            "Current Leadership",
        )

        if leaders:

            leader_cols = st.columns(
                min(len(leaders), 2),
                gap="small",
            )

            for index, leader in enumerate(leaders[:2]):

                with leader_cols[index]:

                    with st.container(border=True):

                        image_col, info_col = st.columns(
                            [0.72, 1.25],
                            gap="small",
                        )

                        with image_col:
                            leader_image = leader.get("image")
                            if not show_image(
                                leader_image,
                                width=86,
                            ):
                                st.caption("Photo unavailable")

                        with info_col:
                            render_html(
                                f"""
                                <div class="mini-leader-title">
                                    {leader.get("title", "Leader")}
                                </div>
                                <div class="mini-leader-name">
                                    {leader.get("name", "N/A")}
                                </div>
                                <div class="mini-leader-role">
                                    {leader.get("role", "")}
                                </div>
                                <div class="mini-leader-since">
                                    Since {leader.get("since", "N/A")}
                                </div>
                                """
                            )

                        if leader.get("description"):
                            render_html(
                                f"""
                                <div class="top-leader-description">
                                    {leader.get("description")}
                                </div>
                                """
                            )

        else:

            with st.container(border=True):
                st.info(
                    f"Leadership information is not currently available for {country_name}."
                )


    # ------------------------------------------------------
    # KEY INFORMATION
    # ------------------------------------------------------

    section_title(
        "🎯",
        "Key Information",
    )

    c1, c2, c3, c4 = st.columns(
        4,
        gap="medium",
    )

    with c1:

        metric_card(
            "Capital",
            country.get("capital") or "N/A",
            icon="🏛️",
        )

    with c2:

        metric_card(
            "Region",
            country.get("region") or "N/A",
            icon="🌍",
        )

    with c3:

        metric_card(
            "Population",
            format_large_number(
                country.get("population")
            ),
            icon="👥",
        )

    with c4:

        area = country.get(
            "area"
        )

        area_text = (
            f"{float(area):,.0f} km²"
            if area
            else "N/A"
        )

        metric_card(
            "Area",
            area_text,
            icon="📐",
        )


    # ------------------------------------------------------
    # CURRENCY + LANGUAGES
    # ------------------------------------------------------

    c1, c2 = st.columns(
        2,
        gap="medium",
    )

    with c1:

        with st.container(
            border=True
        ):

            currency = country.get(
                "currency"
            ) or "N/A"

            currency_code = country.get(
                "currency_code"
            ) or "N/A"

            render_html(
                f"""
                <div class="symbol-icon">💰</div>
                <div class="card-label">
                    Currency
                </div>
                <div class="card-value">
                    {currency}
                </div>
                <div class="card-secondary">
                    Code: {currency_code}
                </div>
                """
            )

    with c2:

        with st.container(
            border=True
        ):

            languages = country.get(
                "languages"
            ) or []

            language_text = (
                ", ".join(languages)
                if languages
                else "N/A"
            )

            render_html(
                f"""
                <div class="symbol-icon">💬</div>
                <div class="card-label">
                    Languages
                </div>
                <div class="card-value">
                    {language_text}
                </div>
                <div class="card-secondary">
                    Reported languages
                </div>
                """
            )


    # ------------------------------------------------------
    # NATIONAL PROFILE
    # ------------------------------------------------------

    profile = api_get(
        f"/countries/{country_name}/profile"
    )

    if profile:

        section_title(
            "🏛️",
            "National & Administrative Profile",
        )

        c1, c2 = st.columns(
            2,
            gap="medium",
        )

        with c1:

            metric_card(
                "States",
                profile.get(
                    "states"
                ) or "N/A",
            )

        with c2:

            metric_card(
                "Union Territories",
                profile.get(
                    "union_territories"
                ) or "N/A",
            )

        st.markdown(
            "#### 🇮🇳 National Symbols"
        )

        symbols = [
            (
                "🐅",
                "National Animal",
                profile.get(
                    "national_animal"
                ),
            ),
            (
                "🦚",
                "National Bird",
                profile.get(
                    "national_bird"
                ),
            ),
            (
                "🪷",
                "National Flower",
                profile.get(
                    "national_flower"
                ),
            ),
            (
                "🌳",
                "National Tree",
                profile.get(
                    "national_tree"
                ),
            ),
            (
                "🦁",
                "National Emblem",
                profile.get(
                    "national_emblem"
                ),
            ),
            (
                "📅",
                "National Calendar",
                profile.get(
                    "national_calendar"
                ),
            ),
        ]

        symbol_cols = st.columns(
            6,
            gap="small",
        )

        for index, symbol in enumerate(
            symbols
        ):

            icon, label, value = symbol

            with symbol_cols[index]:

                symbol_card(
                    icon,
                    label,
                    value,
                )


    # ------------------------------------------------------
    # BORDERS + HERITAGE
    # ------------------------------------------------------

    borders_data = api_get(
        f"/countries/{country_name}/borders"
    )

    heritage_data = api_get(
        f"/countries/{country_name}/heritage"
    )

    borders_col, heritage_col = st.columns(
        [0.92, 1.55],
        gap="medium",
    )

    with borders_col:

        section_title(
            "🌐",
            "Bordering Countries",
        )

        borders = (
            borders_data or {}
        ).get(
            "borders",
            [],
        )

        if borders:

            for start in range(
                0,
                len(borders),
                3,
            ):

                row = borders[
                    start:start + 3
                ]

                cols = st.columns(
                    len(row),
                    gap="small",
                )

                for col, border in zip(
                    cols,
                    row,
                ):

                    with col:

                        with st.container(
                            border=True
                        ):

                            border_flag = border.get(
                                "flag"
                            )

                            if border_flag:

                                show_image(
                                    border_flag,
                                    width=62,
                                )

                            render_html(
                                f"""
                                <div class="border-name">
                                    {border.get("name", "N/A")}
                                </div>
                                <div class="border-code">
                                    {border.get("alpha_2", "")}
                                    |
                                    {border.get("alpha_3", "")}
                                </div>
                                """
                            )

        else:

            st.info(
                "This country has no land borders."
            )


    with heritage_col:

        section_title(
            "🏛️",
            "Historical & Heritage Places",
        )

        places = (
            heritage_data or {}
        ).get(
            "places",
            [],
        )

        if places:

            heritage_df = pd.DataFrame(
                places
            )

            if not heritage_df.empty:

                fig = px.scatter_map(
                    heritage_df,
                    lat="latitude",
                    lon="longitude",
                    hover_name="name",
                    hover_data={
                        "state": True,
                        "city": True,
                        "category": True,
                        "unesco_year": True,
                        "description": True,
                        "latitude": False,
                        "longitude": False,
                    },
                    center={
                        "lat": float(
                            heritage_df[
                                "latitude"
                            ].mean()
                        ),
                        "lon": float(
                            heritage_df[
                                "longitude"
                            ].mean()
                        ),
                    },
                    zoom=3.8,
                    height=390,
                    map_style="open-street-map",
                )

                fig.update_traces(
                    marker={
                        "size": 13
                    }
                )

                fig.update_layout(
                    margin=dict(
                        l=0,
                        r=0,
                        t=0,
                        b=0,
                    ),
                    hoverlabel=dict(
                        font_size=12
                    ),
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True,
                    config={
                        "displayModeBar": True
                    },
                )

            with st.expander(
                "📚 View Heritage Directory"
            ):

                for place in places:

                    st.markdown(
                        f"**📍 {place.get('name', 'Unknown')}** — "
                        f"{place.get('city', 'N/A')}, "
                        f"{place.get('state', 'N/A')}"
                    )

                    st.caption(
                        f"{place.get('category', 'N/A')} "
                        f"• UNESCO: "
                        f"{place.get('unesco_year', 'N/A')}"
                    )

                    st.write(
                        place.get(
                            "description",
                            "No description available.",
                        )
                    )

                    st.divider()

        else:

            st.info(
                "Heritage data is not currently available."
            )


    # ------------------------------------------------------
    # ECONOMIC INTELLIGENCE
    # ------------------------------------------------------

    section_title(
        "📊",
        "Economic Intelligence",
    )

    economy = api_get(
        f"/countries/{country_name}/economy"
    )

    if economy:

        year = economy.get(
            "year"
        )

        if year:

            st.caption(
                f"Latest available data: {year}"
            )

        e1, e2, e3 = st.columns(
            3,
            gap="medium",
        )

        with e1:

            metric_card(
                "GDP",
                format_currency(
                    economy.get("gdp")
                ),
                icon="💰",
            )

        with e2:

            gdp_pc = economy.get(
                "gdp_per_capita"
            )

            metric_card(
                "GDP per Capita",
                (
                    f"${float(gdp_pc):,.0f}"
                    if gdp_pc is not None
                    else "N/A"
                ),
                icon="👤",
            )

        with e3:

            growth = economy.get(
                "gdp_growth"
            )

            metric_card(
                "GDP Growth",
                (
                    f"{float(growth):.2f}%"
                    if growth is not None
                    else "N/A"
                ),
                icon="📈",
            )

        e4, e5 = st.columns(
            2,
            gap="medium",
        )

        with e4:

            inflation = economy.get(
                "inflation"
            )

            metric_card(
                "Inflation",
                (
                    f"{float(inflation):.2f}%"
                    if inflation is not None
                    else "N/A"
                ),
                icon="🧾",
            )

        with e5:

            unemployment = economy.get(
                "unemployment"
            )

            metric_card(
                "Unemployment",
                (
                    f"{float(unemployment):.2f}%"
                    if unemployment is not None
                    else "N/A"
                ),
                icon="👥",
            )

    else:

        st.warning(
            "Economic data is currently unavailable."
        )


    # ------------------------------------------------------
    # HISTORICAL TRENDS
    # ------------------------------------------------------

    section_title(
        "📈",
        "Historical Economic & Population Trends",
    )

    history_data = api_get(
        f"/countries/{country_name}/history"
    )

    if history_data:

        records = history_data.get(
            "records",
            [],
        )

        if records:

            history_df = pd.DataFrame(
                records
            ).sort_values(
                "year"
            )

            indicator_labels = {
                "population": "Population",
                "gdp": "GDP",
                "gdp_per_capita": "GDP per Capita",
                "gdp_growth": "GDP Growth",
                "inflation": "Inflation",
                "unemployment": "Unemployment",
            }

            selected_indicator = st.selectbox(
                "Select indicator",
                list(
                    indicator_labels.keys()
                ),
                format_func=lambda x:
                    indicator_labels[x],
                key="history_indicator",
            )

            chart_df = history_df[
                [
                    "year",
                    selected_indicator,
                ]
            ].dropna()

            if not chart_df.empty:

                fig = px.line(
                    chart_df,
                    x="year",
                    y=selected_indicator,
                    markers=True,
                    title=indicator_labels[
                        selected_indicator
                    ],
                )

                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    margin=dict(
                        l=15,
                        r=15,
                        t=48,
                        b=15,
                    ),
                    xaxis_title="Year",
                    yaxis_title=indicator_labels[
                        selected_indicator
                    ],
                    hovermode="x unified",
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True,
                )

                with st.expander(
                    "📋 View historical data"
                ):

                    st.dataframe(
                        history_df,
                        use_container_width=True,
                    )

        else:

            st.info(
                "Historical records are unavailable."
            )

    else:

        st.info(
            "Historical data is currently unavailable."
        )


    # ------------------------------------------------------
    # GEOGRAPHY
    # ------------------------------------------------------

    section_title(
        "🗺️",
        "Geography",
    )

    latitude = country.get(
        "latitude"
    )

    longitude = country.get(
        "longitude"
    )

    if (
        latitude is not None
        and longitude is not None
    ):

        map_df = pd.DataFrame(
            {
                "latitude": [
                    latitude
                ],
                "longitude": [
                    longitude
                ],
            }
        )

        st.map(
            map_df,
            zoom=3,
        )

        g1, g2 = st.columns(2)

        with g1:

            st.caption(
                f"Subregion: "
                f"{country.get('subregion') or 'N/A'}"
            )

        with g2:

            timezones = (
                country.get(
                    "timezones"
                ) or []
            )

            st.caption(
                f"Timezones: "
                f"{', '.join(timezones) if timezones else 'N/A'}"
            )


# ==========================================================
# FOOTER
# ==========================================================

render_html(
    """
    <div class="footer">
        🌍 <b>GlobeScope</b> — Global Country Intelligence Dashboard
        <br>
        Built with Python • FastAPI • Streamlit • Plotly • REST APIs • World Bank
    </div>
    """
)
