# PlayMetrics

A CQRS-based sports data analytics backend using FastAPI and PostgreSQL.

## Features

- CQRS architecture with separate command and query endpoints
- PostgreSQL database with SQLAlchemy ORM
- Automated data fetching from TheSportsDB API
- Scheduled tasks using APScheduler
- RESTful API using FastAPI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ifarouk/playmetrics.git
cd playmetrics
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure PostgreSQL:
- Create a database named 'playmetrics'
- Update the DATABASE_URL in app/db/__init__.py if needed

5. Run the application:
```bash
python main.py
```

The API will be available at http://localhost:8000

## API Endpoints

- POST `/commands/add-player`: Add a new player
- GET `/queries/get-players`: Retrieve all players

## Documentation

API documentation is available at http://localhost:8000/docs when the server is running.