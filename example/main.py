from datetime import date

from harvest import Harvest


class Project:
    INTERNAL = "Internal -- Project"


class Task:
    CERTIFICATION = "2. Internal -- Certifications"
    MEETING = "2. Internal -- Meeting"
    RND = "2. Internal -- R&D"
    TRAINING = "2. Internal -- Internal Training"


def main():
    username = ""
    password = ""

    harvest = Harvest(username, password)
    harvest.date = date.today()
    harvest.project = Project.INTERNAL
    harvest.task = Task.MEETING
    harvest.note = "Kick off meeting"
    harvest.duration = "0:30"
    harvest.submit()


if __name__ == "__main__":
    main()
