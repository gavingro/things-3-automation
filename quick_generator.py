# Use this personal study scheduler for now until we figure Alfred out.
# Fill in your Lecture Notes Title, Class (Things Project) Name, and Notion Link

# Then, when you're ready, run the script.

from things_classes import ThingsStudyScheduler

lecture_notes_title = """L2 - Limit Rules and Solving Limits Algebraically (2.3)"""
class_title_project = """Review: MATH 116 - Calculus 1 - The Mathematics of Change"""
notion_url = """notion://www.notion.so/L2-Limit-Rules-and-Solving-Limits-Algebraically-2-3-84effbf12c1b40928991c0fa9f6d558f"""

study_test = ThingsStudyScheduler(lecture_notes_title, class_title_project, notion_url)


if __name__ == "__main__":
    study_test.schedule_study_reminders()
