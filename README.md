# Travel Agency Website

Python Flask web application is designed for a travel agency, where it displays various tours and allows users to
filter tours by departure cities. The application retrieves tour data from an SQLite database and serves it through
multiple routes. The database stores information like tour titles, descriptions, pictures, departure cities, and more.

## Features
- Home Page (Index): Lists all available tours with essential details.
- Departure City Filter: Filters tours based on the user's selected departure city.
- Tour Details Page: Shows detailed information for a specific tour.
- SQLite Database: The app uses an SQLite database (tours.db) for storing tour details.

## Installation

```bash
git clone https://github.com/haldaniko/TravelAgency-FlaskWebsite.git
cd TravelAgency-FlaskWebsite

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

The Website will be available at `http://127.0.0.1:5000/`

## Demo 
![demo.png](screenshots%2Fdemo.png)
---
![demo2.png](screenshots%2Fdemo2.png)
