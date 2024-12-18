from fastapi import FastAPI
from app.api.commands import add_player
from app.api.queries import get_players
from app.db import init_db
from app.tasks.scheduler import TaskScheduler
import uvicorn
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI(title="PlayMetrics API")

# Include routers
app.include_router(add_player.router)
app.include_router(get_players.router)

@app.on_event("startup")
async def startup_event():
    # Initialize database
    init_db()
    
    # Start scheduler
    scheduler = TaskScheduler()
    scheduler.start()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)