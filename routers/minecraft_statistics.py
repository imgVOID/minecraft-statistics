import websockets
from datetime import datetime
from fastapi import APIRouter
from re import escape
from database.sqlite_utils_sync import db
from schemas.minecraft_statistics import DataLauncher, DataVandals

router_minecraft_statistics = APIRouter(
    redirect_slashes=False,
    tags=["minecraft_statistics"],
)


@router_minecraft_statistics.post("/send_data_launcher")
async def launcher_data(data: DataLauncher):
    db.write_login_attempt(
        escape(data.username), escape(data.ads_source), data.launched_at.isoformat()
    )
    return data


@router_minecraft_statistics.post("/send_data_vandals")
async def launcher_data(data: DataVandals = ""):
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(data.json())
        print(f"Vandal detected! {datetime.now().isoformat()}")
    return data
