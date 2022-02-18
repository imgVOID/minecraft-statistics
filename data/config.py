from os import sep


class Globals:
    __slots__ = {
        "STATISTICS_MAIN_PATH", "SCHEDULER_TIMINGS", "SCHEDULED_TASKS_IDS"
    }

    def __init__(self):
        self.STATISTICS_MAIN_PATH = f'{sep.join(__file__.split(sep)[:-2])}{sep}data{sep}history_activity'
        self.SCHEDULER_TIMINGS = {
            "statistics_dump": {
                "name": "Launcher statistics dump",
                "trigger": "cron",
                "datetime": {"hour": 23, "minute": 59, "second": 10}  # must be everyday
            },
        }


config = Globals()
