# Use this personal study scheduler for now until we figure Alfred out.
# Fill in your Lecture Notes Title, Class (Things Project) Name, and Notion Link

# Then, when you're ready, run the script.

from things_classes import ThingsStudyScheduler

lecture_notes_title = (
    """L13 - Discrete Random Variables and Linear Combinations (3.4)"""
)
class_title_project = """Review: STAT 101 - Introduction to Statistics"""
notion_url = """https://www.notion.so/L13-Discrete-Random-Variables-and-Linear-Combinations-3-4-b2cd25095f4c40f6be2225401b86eacd"""
notion_url = notion_url.replace("https:", "notion:")

study_test = ThingsStudyScheduler(lecture_notes_title, class_title_project, notion_url)


if __name__ == "__main__":
    study_test.schedule_study_reminders()
