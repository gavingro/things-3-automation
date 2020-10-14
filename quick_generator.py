# Use this personal study scheduler for now until we figure Alfred out.
# Fill in your Lecture Notes Title, Class (Things Project) Name, and Notion Link

# Then, when you're ready, run the script.

from things_classes import ThingsStudyScheduler

lecture_notes_title = """L10 - Higher Derivatives and Trig Derivatives"""
class_title_project = """Review: MATH 116 - Calculus 1 - The Mathematics of Change"""
notion_url = """https://www.notion.so/L10-Higher-Derivatives-and-Trig-Derivatives-5a059b3025084c079a18f3d5c39a4064"""
notion_url = notion_url.replace("https:", "notion:")

study_test = ThingsStudyScheduler(lecture_notes_title, class_title_project, notion_url)


if __name__ == "__main__":
    study_test.schedule_study_reminders()
