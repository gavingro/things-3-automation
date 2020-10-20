# Use this personal study scheduler for now until we figure Alfred out.
# Fill in your Lecture Notes Title, Class (Things Project) Name, and Notion Link

# Then, when you're ready, run the script.

from things_classes import ThingsStudyScheduler

lecture_notes_title = """L13 - Intro to Classes and Objects (S13 to 140)"""
class_title_project = (
    """Review: CPSC 1113 - Principles of Program Structure and Design"""
)
notion_url = """https://www.notion.so/L13-Intro-to-Classes-and-Objects-S13-to-140-73573deb6ee04801a031c7f34dd4c42c"""
notion_url = notion_url.replace("https:", "notion:")

study_test = ThingsStudyScheduler(lecture_notes_title, class_title_project, notion_url)


if __name__ == "__main__":
    study_test.schedule_study_reminders()
