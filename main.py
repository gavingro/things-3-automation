# Use this program in your text editor to create spaced repetition to-do's.
# Fill in your Lecture Notes Title (Header), Class (Things Project) Name, and
#       description to add to each to-do.

# Then, when you're ready, run the script.

from things_classes import ThingsStudyScheduler

lecture_notes_title = """L1 - Working with Vectors"""
class_title_project = """Review: MATH 152 - Linear Algebra"""
notion_url = (
    """https://www.notion.so/L1-Working-with-Vectors-8a06aa5ef5074ea7ab4bd3992ca7dfff"""
)
notion_url = notion_url.replace("https:", "notion:")

study_test = ThingsStudyScheduler(lecture_notes_title, class_title_project, notion_url)


if __name__ == "__main__":
    study_test.schedule_study_reminders()
