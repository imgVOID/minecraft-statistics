from aiosqlite import connect
from datetime import datetime
from pandas import read_sql
from os import makedirs
from sqlite3 import connect, PARSE_COLNAMES


class SQLite:
    __slots__ = {'__conn', '__cur', '__groups', 'name', '_backup_parent_dir'}

    def __init__(self, name):
        self.name = name
        self.__conn = connect(
            f'{name}.sqlite3', isolation_level=None, detect_types=PARSE_COLNAMES
        )
        self.__cur = self.__conn.cursor()
        self.__create_launcher_data_table()

    def __run_command(self, command):
        try:
            self.__cur.execute(command)
            self.__conn.commit()
        except Exception as e:
            return e

    def __create_launcher_data_table(self):
        sql_command = f'''
        CREATE TABLE IF NOT EXISTS 'launcher_data' (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        login varchar(30) NOT NULL, ads_source varchar(30) NOT NULL,
        launched_at timestamp);'''
        self.__run_command(sql_command)

    def __clear_launcher_data_table(self):
        return self.__run_command(
            f"""DELETE FROM 'launcher_data'"""
        )

    def write_login_attempt(self, nickname: str, ads_source: str, launched_at: datetime):
        self.__run_command(f"""
            INSERT OR IGNORE INTO 'launcher_data' (login,ads_source,launched_at)
            VALUES ("{nickname}", "{ads_source}", "{launched_at}")
            """)

    def backup_activity(self, path, date_time):
        data = read_sql(
            f"SELECT * FROM 'launcher_data'", self.__conn
        )
        try:
            makedirs(path)
        except FileExistsError:
            pass
        finally:
            data.to_csv(f'{path}/Day {date_time[1]}.csv', index=False)
            self.__clear_launcher_data_table()


db = SQLite(name="launcher_db")
