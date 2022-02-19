import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from routers.minecraft_statistics import router_minecraft_statistics
from scheduled.minecraft_statistics import save_statistics_dump
from config import config


app = FastAPI(docs_url='/api/minecraft/docs', redoc_url='/api/minecraft/redoc')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router_minecraft_statistics, prefix="/api/minecraft/statistics")


@app.on_event('startup')
def init_data():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        save_statistics_dump, config.SCHEDULER_TIMINGS["statistics_dump"]["trigger"],
        **config.SCHEDULER_TIMINGS["statistics_dump"]["datetime"]
    )
    scheduler.start()


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True, debug=False, log_level="info")
