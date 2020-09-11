# Use this personal study scheduler for now until we figure Alfred out.
# Fill in your Lecture Notes Title, Class (Things Project) Name, and Notion Link

# Then, when you're ready, run the script.

from things_classes import ThingsStudyScheduler

lecture_notes_title = """L2 - Model and Cost Function"""
class_title_project = """Review: Coursera - Machine Learning"""
notion_url = """notion://www.notion.so/L2-Model-and-Cost-Function-7537a38f34ac46808580753dbbf6d4ea"""

study_test = ThingsStudyScheduler(lecture_notes_title, class_title_project, notion_url)


if __name__ == "__main__":
    study_test.schedule_study_reminders()
