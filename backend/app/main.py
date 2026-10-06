from fastapi import FastAPI

from backend.app.api.countries import router as countries_router


app = FastAPI(
    title="GlobeScope API",
    description="Global Country Intelligence API",
    version="1.0.0"
)


app.include_router(countries_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to GlobeScope API",
        "status": "running"
    }