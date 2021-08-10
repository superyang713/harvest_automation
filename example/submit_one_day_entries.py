import time
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
    _date = date.today()
    update_one_day(harvest, _date)


def update_one_day(harvest: Harvest, date):
    entries = [
        {
            "project": Project.INTERNAL,
            "task": Task.RND,
            "note": "Create a project for automating harvest.",
            "duration": "3:30"
        },
        {
            "project": Project.INTERNAL,
            "task": Task.MEETING,
            "note": "Kickoff meeting.",
            "duration": "0:30"
        },
        {
            "project": Project.INTERNAL,
            "task": Task.RND,
            "note": "Code review for automation package",
            "duration": "1:00"
        },
        {
            "project": Project.INTERNAL,
            "task": Task.TRAINING,
            "note": "Practice bigquery SQL",
            "duration": "1:30"
        },
        {
            "project": Project.INTERNAL,
            "task": Task.CERTIFICATION,
            "note": "Learn GCP and AWS for professional certificate exams",
            "duration": "1:30"
        },
    ]
    for entry in entries:
        entry["date"] = date
        update_one_entry(harvest, **entry)


def update_one_entry(
        harvest: Harvest,
        date,
        project,
        task,
        note,
        duration):
    harvest.date = date
    harvest.project = project
    harvest.task = task
    harvest.note = note
    harvest.duration = duration
    harvest.submit()
    time.sleep(5)


if __name__ == "__main__":
    main()
