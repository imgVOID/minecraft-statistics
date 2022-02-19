from os import sep


class Globals:
    __slots__ = {
        "STATISTICS_MAIN_PATH", "SCHEDULER_TIMINGS", "SCHEDULED_TASKS_IDS"
    }

    def __init__(self):
        self.STATISTICS_MAIN_PATH = f'{sep.join(__file__.split(sep)[:-1])}{sep}analytics{sep}history_activity{sep}'
        self.SCHEDULER_TIMINGS = {
            "statistics_dump": {
                "name": "Launcher statistics dump",
                "trigger": "cron",
                "datetime": {"hour": 23, "minute": 59, "second": 10}  # must be everyday
                # "trigger": "interval",
                # "datetime": {"seconds": 5}  # test
            },
        }


config = Globals()
