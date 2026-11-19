from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

FORECAST_DATA = {
    "moscow": [
        {"date": "2026-11-20", "temp": -2, "condition": "cloudy"},
        {"date": "2026-11-21", "temp": -4, "condition": "snow"},
        {"date": "2026-11-22", "temp": -1, "condition": "clear"},
        {"date": "2026-11-23", "temp": 0, "condition": "cloudy"},
        {"date": "2026-11-24", "temp": -3, "condition": "snow"},
        {"date": "2026-11-25", "temp": -5, "condition": "clear"},
        {"date": "2026-11-26", "temp": -4, "condition": "cloudy"},
    ],
    "tomsk": [
        {"date": "2026-11-20", "temp": -12, "condition": "snow"},
        {"date": "2026-11-21", "temp": -15, "condition": "clear"},
        {"date": "2026-11-22", "temp": -10, "condition": "cloudy"},
        {"date": "2026-11-23", "temp": -8, "condition": "snow"},
        {"date": "2026-11-24", "temp": -14, "condition": "clear"},
        {"date": "2026-11-25", "temp": -16, "condition": "clear"},
        {"date": "2026-11-26", "temp": -11, "condition": "cloudy"},
    ],
    "london": [
        {"date": "2026-11-20", "temp": 9, "condition": "rain"},
        {"date": "2026-11-21", "temp": 11, "condition": "cloudy"},
        {"date": "2026-11-22", "temp": 10, "condition": "rain"},
        {"date": "2026-11-23", "temp": 8, "condition": "clear"},
        {"date": "2026-11-24", "temp": 9, "condition": "cloudy"},
        {"date": "2026-11-25", "temp": 12, "condition": "clear"},
        {"date": "2026-11-26", "temp": 10, "condition": "rain"},
    ],
}


@app.get("/")
def index():
    return FileResponse("static/index.html")


@app.get("/about")
def about():
    return FileResponse("static/about.html")


@app.get("/api/status")
def status():
    return {"status": "ok"}


@app.get("/api/forecast/{city}")
def get_forecast(city: str, days: str = "3"):
    try:
        days_int = int(days)
    except ValueError:
        raise HTTPException(status_code=400, detail="Days must be an integer")

    if not (1 <= days_int <= 7):
        raise HTTPException(status_code=400, detail="Days must be between 1 and 7")

    city_forecast = FORECAST_DATA.get(city.lower())
    if not city_forecast:
        raise HTTPException(status_code=404, detail="City not found")

    return city_forecast[:days_int]


app.mount("/", StaticFiles(directory="static"), name="static")
