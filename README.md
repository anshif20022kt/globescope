cat > README.md <<'EOF'
# 🌍 GlobeScope

### Global Country Intelligence Dashboard

GlobeScope is an interactive global country intelligence dashboard that allows users to explore detailed information about countries through a modern web interface.

The project combines FastAPI, Streamlit, REST APIs, World Bank data, Pydantic, and Plotly to provide country information, economic indicators, historical data, geographic information, and country comparison.

---

## 🚀 Features

- 🌍 Country Explorer
- 🏳️ Country flags and basic information
- 🏛️ Capital, region and subregion
- 👥 Population and area
- 💰 Currency information
- 🗣️ Languages
- 🕐 Timezones
- 🗺️ Bordering countries
- 📍 Geographic information
- 👤 Country leadership
- 💰 Economic intelligence
- 📈 Historical population and economic data
- 🏛️ National heritage and historical places
- ⚖️ Country comparison
- 📊 Interactive visualizations

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │      Frontend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       REST Countries      World Bank       Pydantic
           API                API             Models

🛠️ Tech Stack
Technology	Purpose
Python	Core programming language
FastAPI	Backend API
Streamlit	Interactive dashboard
Pydantic	Data validation
REST Countries API	Country information
World Bank API	Economic data
Pandas	Data processing
Plotly	Data visualization
Uvicorn	API server
Git	Version control
GitHub	Source code hosting


📁 Project Structure
globescope/
├── backend/
│   └── app/
│       ├── api/
│       │   └── countries.py
│       ├── models/
│       │   ├── country.py
│       │   ├── heritage.py
│       │   └── leadership.py
│       ├── services/
│       │   ├── country_service.py
│       │   ├── heritage_service.py
│       │   └── leadership_service.py
│       └── main.py
├── frontend/
│   └── app.py
├── database/
├── data/
├── tests/
├── .gitignore
├── requirements.txt
├── README.md
└── .env

⚙️ Installation
Clone the repository
git clone https://github.com/anshif20022kt/globescope.git
cd globescope

Create virtual environment
python -m venv .venv

Activate virtual environment
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt

🔐 Environment Variables
Create a .env file in the project root:
REST_COUNTRIES_API_KEY=your_api_key_here

Never commit your .env file to GitHub.
The .env file is protected by .gitignore.
▶️ Running the Application
FastAPI Backend
python -m uvicorn backend.app.main:app --reload

API:
http://127.0.0.1:8000

API documentation:
http://127.0.0.1:8000/docs

Streamlit Frontend
Open another terminal and run:
source .venv/bin/activate
streamlit run frontend/app.py

Dashboard:
http://localhost:8501

🔌 API Endpoints
GET /countries/{country_name}
GET /countries/{country_name}/borders
GET /countries/{country_name}/economy
GET /countries/{country_name}/history
GET /countries/{country_name}/heritage
GET /countries/{country_name}/leader
GET /countries/{country_name}/profile
GET /countries/compare

Interactive API documentation:
http://127.0.0.1:8000/docs

📊 Data Sources
GlobeScope currently integrates:
- REST Countries API
- World Bank API
- Project-specific data and service layers
🔒 Security
API credentials are stored locally using environment variables.
Never commit:
.env
.streamlit/secrets.toml

📌 Project Status
🚧 Active Development
GlobeScope is being developed as an advanced portfolio project focused on:
- Data Analytics
- Data Visualization
- REST API integration
- Backend development
- Interactive dashboards
- Economic data analysis
- Geographic intelligence
- Country comparison
Future development may include database integration, additional data sources, improved country coverage, authentication, deployment, and advanced analytics.
👨‍💻 Author
Muhammed Anshif KT
GitHub:
https://github.com/anshif20022kt/globescope
EOF
git add README.md && 
git commit -m "Expand project README" && 
git push origin main && 
git status

### What happens

That **single paste** will:

1. Replace the current `Is`
2. Write your **complete README**
3. Stage `README.md`
4. Commit it
5. Push it to GitHub
6. Show the final Git status

At the end, you should see:

```text
nothing to commit, working tree clean
