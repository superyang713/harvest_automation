from datetime import date

from harvest import Harvest
from enums import Project, Task


def main():
    username = ""
    password = ""

    harvest = Harvest(username, password)
    harvest.date = date.today()
    harvest.project = Project.INTERNAL
    harvest.task = Task.MEETING
    harvest.note = "Kick off meeting"
    harvest.duration = "0:30"


if __name__ == "__main__":
    main()
