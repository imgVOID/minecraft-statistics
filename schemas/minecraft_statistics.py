from pydantic import BaseModel
from datetime import datetime


class LauncherData(BaseModel):
    nickname: str
    ads_source: str
    launched_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "nickname": "Minecraft nickname",
                "ads_source": "ADs source's ID",
                "launched_at": datetime.utcnow(),
            }
        }
