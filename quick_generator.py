# Use this personal study scheduler for now until we figure Alfred out.
# Fill in your Lecture Notes Title, Class (Things Project) Name, and Notion Link

# Then, when you're ready, run the script.

from things_classes import ThingsStudyScheduler

lecture_notes_title = "L9 - The meaning of Caves"
class_title_project = "CAVE 490 - Spelunking"
notion_url = "notion://www.notion.so/Learning-Hub-5bd3f010c36c4a7c8302ea1658c9ffeb"

study_test = ThingsStudyScheduler(lecture_notes_title, class_title_project, notion_url)


if __name__ == __main__:
    study_test.schedule_study_reminders()
