from datetime import datetime
from database.sqlite_utils_sync import db
from data.config import config


# scheduled action, more information in the main.py file
async def save_statistics_dump(*args):
    date_time = (datetime.now().strftime("%m.%Y"), datetime.now().strftime("%d"))
    path = f'{config.STATISTICS_MAIN_PATH}/{date_time[0]}'
    db.backup_activity(path, date_time)
