# ForecastItinerary
A WIP Django web application that tracks trips and queries the National Weather Service for weather conditions on a given trip day.

## Stack

- Python 3.14
- Django
- SQLite
- [National Weather Service API](https://www.weather.gov/documentation/services-web-api)

## Setup

```bash
git clone https://github.com/jahelt/forecast-itinerary.git
cd forecast-itinerary

python -m venv .venv
.venv\Scripts\activate.bat      # Unix/MacOS: source .venv/bin/activate

python -m pip install Django    # Check with: django-admin --version

python manage.py migrate
python manage.py runserver
```

The app runs at `http://127.0.0.1:8000/`