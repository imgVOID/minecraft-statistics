from pydantic import BaseModel
from datetime import datetime


class DataLauncher(BaseModel):
    username: str
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


class DataVandals(BaseModel):
    username: str
    region_name: str

    class Config:
        schema_extra = {
            "example": {
                "username": "Minecraft nickname",
                "region_name": "Minecraft region name",
            }
        }
