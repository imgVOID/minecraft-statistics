from fastapi import APIRouter
from re import escape
from database.sqlite_utils_sync import db
from schemas.minecraft_statistics import LauncherData

router_minecraft_statistics = APIRouter(
    redirect_slashes=False,
    prefix="/api",
    tags=["minecraft_statistics"],
)


@router_minecraft_statistics.post("/launcher_data")
async def launcher_data(data: LauncherData):
    db.write_login_attempt(
        escape(data.nickname), escape(data.ads_source), data.launched_at.isoformat()
    )
    return data
